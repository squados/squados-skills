import {spawnSync} from 'node:child_process';
import {existsSync,readFileSync,writeFileSync} from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
export function findHyperframes() {
  const deps=process.env.EDITAR_VIDEO_NODE_HOME || root;
  const cli=path.join(deps,'node_modules','hyperframes','bin','hyperframes.mjs');
  if(!existsSync(cli)) throw new Error('Run scripts/setup.py first; HyperFrames is missing');
  return cli;
}
export function finalAudioArgs(video,audio,output,duration){return ['-hide_banner','-loglevel','error','-y','-i',video,'-i',audio,'-map','0:v:0','-map','1:a:0','-c:v','copy','-c:a','aac','-b:a','192k',...(duration?['-af','apad','-t',String(duration)]:['-shortest']),'-movflags','+faststart',output];}
export function canResume(previous,signature,quality){return previous.signature===signature&&previous.quality===quality;}
export function renderComposition(project,quality='preview') {
  if(!['preview','final'].includes(quality)) throw new Error('Invalid quality');
  const output=path.resolve(project,quality==='final'?'master.mp4':'preview.mp4');
  const rendered=path.resolve(project,quality==='final'?'visual-master.mp4':'visual-preview.mp4');
  const cli=findHyperframes();
  const cache=path.join(project,'.render-cache.json');
  const signature=process.env.EDITAR_VIDEO_RENDER_FINGERPRINT||readFileSync(path.join(project,'index.html'),'utf8');
  const previous=existsSync(cache)?JSON.parse(readFileSync(cache,'utf8')):{};
  const resume=canResume(previous,signature,quality);
  writeFileSync(cache,JSON.stringify({signature,quality}));
  for(const args of [['lint',project],['render',project,'--output',rendered,'--quality',quality==='final'?'delivery':'draft','--workers','1','--experimental-fast-capture=false','--no-best-effort',...(process.env.EDITAR_VIDEO_BROWSER_GPU==='1'?['--browser-gpu']:['--no-browser-gpu']),...(resume?['--resume']:[]),'--keep-segments','--frames-cache-dir',path.join(project,'.frame-cache')]]) {
    const result=spawnSync(process.execPath,[cli,...args],{stdio:'inherit',env:{...process.env,HF_SEGMENTED_CAPTURE:'true',DO_NOT_TRACK:'1'}});
    if(result.status!==0) throw new Error(`HyperFrames ${args[0]} failed (${result.status})`);
  }
  const audio=path.join(project,'assets','mix.wav');const voice=existsSync(audio)?audio:path.join(project,'assets','voice.wav');
  if(existsSync(voice)){
    const edit=path.join(project,'edit.json');const duration=existsSync(edit)?JSON.parse(readFileSync(edit,'utf8')).duration_us/1e6:undefined;
    const mux=spawnSync('ffmpeg',finalAudioArgs(rendered,voice,output,duration),{stdio:'inherit'});
    if(mux.status!==0)throw new Error('Final audio mux failed');
  }else{
    const mux=spawnSync('ffmpeg',['-hide_banner','-loglevel','error','-y','-i',rendered,'-c','copy',output],{stdio:'inherit'});
    if(mux.status!==0)throw new Error('Proof passthrough failed');
  }
  return {output};
}
if(process.argv[1]===fileURLToPath(import.meta.url)) renderComposition(path.resolve(process.argv[2]),process.argv[3]||'preview');
