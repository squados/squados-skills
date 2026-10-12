import {esc,ident} from './layout.mjs';
export const CAPTION_STYLES=['block','active-word','karaoke','one-word','keyword','rail','impact','embedded'];
export const fontForBeat=(beat,style)=>style.fonts[beat.font_role]||style.fonts.base;
export function buildCaptions({words,beats,style,framePlan}) {
  let html='',animations=[];const diagnostics=[];const byId=new Map(words.map(w=>[w.id,w]));
  const width=framePlan.width,height=framePlan.height;const size=Math.round(Math.min(width,height)*.061);
  for(const beat of beats) {
    const list=beat.word_ids.map(id=>byId.get(id));if(list.some(w=>!w)) throw new Error('Caption word missing');
    let treatment=beat.caption||'active-word';if(!CAPTION_STYLES.includes(treatment)) throw new Error('Unknown caption treatment');
    if(treatment==='embedded'&&!framePlan.mask_src){diagnostics.push({code:'embedded-fallback',beat:beat.id});treatment='active-word';}
    const family=fontForBeat(beat,style);const start=list[0].start_us/1e6,end=list.at(-1).end_us/1e6;
    const groups=[];let group=[];
    for(const word of list){const limit=Math.max(12,Math.floor(width*.89/(size*.62))*2);if(group.length&&group.map(x=>x.text).join(' ').length+word.text.length+1>limit){groups.push(group);group=[];}group.push(word);if(group.length>=(treatment==='one-word'?1:treatment==='impact'?3:7)||/[.!?]$/.test(word.text)||group.length>=3&&/[,;:]$/.test(word.text)){groups.push(group);group=[];}}if(group.length)groups.push(group);
    groups.forEach((part,index)=>{
      const id='cap-'+ident(beat.id)+'-'+index;const a=part[0].start_us/1e6,b=part.at(-1).end_us/1e6;
      const rail=treatment==='rail';const keyword=treatment==='keyword';
      const position=framePlan.caption_zone==='top'?`top:${height*.12}px`:`bottom:${height*(treatment==='embedded'?.45:.12)}px`;
      const css=`position:absolute;left:${width*.055}px;${position};width:${width*.89}px;height:${size*2.5}px;display:flex;flex-wrap:wrap;align-content:center;justify-content:${rail?'flex-start':'center'};gap:${size*.22}px;text-align:center;font-family:'${esc(family)}';font-size:${size*(treatment==='impact'?1.28:1)}px;font-weight:800;line-height:1.12;color:white;text-shadow:0 2px 4px #000,0 0 12px #000;z-index:20;`;
      html+=`<div id="${id}" class="clip caption ${treatment}" data-start="${a}" data-duration="${b-a}" data-track-index="20" style="${css}">`;
      for(const word of part){const wid=id+'-'+ident(word.id); const focus=word.id===beat.anchor_word_id;html+=`<span id="${wid}" style="background:#101217;border-radius:6px;padding:2px 5px;${keyword&&focus?'font-size:1.25em;color:var(--accent);':''}${rail?'border-left:5px solid var(--accent);padding-left:12px;':''}">${esc(word.text)}</span>`;
        if(['active-word','karaoke','embedded'].includes(beat.caption||'active-word')) {
          animations.push({target:'#'+wid,from:{color:'#fff',scale:1},to:{color:style.accent||'#baff54',scale:1.06,duration:.065},at:word.start_us/1e6});
          if(treatment!=='karaoke') animations.push({target:'#'+wid,from:null,to:{color:'#fff',scale:1,duration:.065},at:Math.max(word.start_us/1e6,word.end_us/1e6-.065)});
        }
      }
      html+='</div>';animations.push({target:'#'+id,from:{opacity:0,y:12},to:{opacity:1,y:0,duration:Math.min(.12,(b-a)/3)},at:a});
      animations.push({target:'#'+id,from:null,to:{opacity:0,duration:Math.min(.08,(b-a)/3)},at:Math.max(a,b-.08)});
    });
  }
  return {html,animations,diagnostics};
}
