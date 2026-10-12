import {esc,ident,box} from './layout.mjs';
export const MOTION_TYPES=['emphasis','counter','comparison','checklist','steps','flow','chart','timeline','quote','definition','problem-solution','callout','interface','morph','concept-map','media-reveal','lower-third','recap'];
const items=d=>{if(!Array.isArray(d.items)||!d.items.length)throw new Error('Effect requires items');return d.items.map(esc);};
export function buildEffect(beat,context) {
  const effect=beat.effect;if(effect==='hold')return {html:'',animations:[],diagnostics:[]};
  if(!MOTION_TYPES.includes(effect))throw new Error('Unknown motion effect');
  const d=beat.data||{};let content='';const text=esc(d.text||d.title),title=esc(d.title||'');
  switch(effect){
    case 'emphasis':content=`<div class="large accent">${text}</div><div class="rule"></div>`;break;
    case 'counter':if(!Number.isFinite(d.value))throw new Error('Counter requires value');content=`<strong class="number" data-count="${d.value}">${esc(d.value)}</strong><small>${esc(d.unit)}</small>`;break;
    case 'comparison':if(!d.before||!d.after)throw new Error('Comparison requires before/after');content=`<div class="columns"><div class="muted">${esc(d.before)}</div><span>→</span><div class="accent">${esc(d.after)}</div></div>`;break;
    case 'checklist':content=`<ul class="checklist">${items(d).map(x=>`<li>✓ ${x}</li>`).join('')}</ul>`;break;
    case 'steps':content=`<ol class="steps">${items(d).map((x,i)=>`<li><b>${i+1}</b>${x}</li>`).join('')}</ol>`;break;
    case 'flow':content=`<div class="flow">${items(d).map(x=>`<span>${x}</span>`).join('<b>↓</b>')}</div>`;break;
    case 'chart':if(!Array.isArray(d.values)||!d.values.length||d.values.some(x=>!Number.isFinite(x)))throw new Error('Chart requires values');content=`<div class="chart">${d.values.map((v,i)=>`<div class="bar-row"><span>${esc(d.labels?.[i]??i+1)}</span><b style="width:${Math.abs(v)/Math.max(1,...d.values.map(Math.abs))*70}%">${v}</b></div>`).join('')}</div>`;break;
    case 'timeline':content=`<div class="timeline">${items(d).map((x,i)=>`<div><i></i><small>${i+1}</small> ${x}</div>`).join('')}</div>`;break;
    case 'quote':content=`<blockquote>“${esc(d.quote||d.text)}”</blockquote><small>${esc(d.author||'')}</small>`;break;
    case 'definition':content=`<small>CONCEITO</small><h2>${title}</h2><p>${esc(d.text)}</p>`;break;
    case 'problem-solution':content=`<div class="problem">${esc(d.before)}</div><div class="solution">✓ ${esc(d.after)}</div>`;break;
    case 'callout':content=`<div class="callout"><svg width="70" height="40"><path d="M2 38 L50 5 L45 22 M50 5 L30 6" stroke="currentColor" stroke-width="4" fill="none"/></svg><p>${text}</p></div>`;break;
    case 'interface':content=`<div class="browser"><header>● ● ●</header><div>${title}</div>${items(d).map(x=>`<p class="ui-row">${x}</p>`).join('')}</div>`;break;
    case 'morph':content=`<div class="morph-shape"><span>${text}</span></div>`;break;
    case 'concept-map':content=`<div class="concept"><strong>${title}</strong><div class="nodes">${items(d).map(x=>`<span>${x}</span>`).join('')}</div></div>`;break;
    case 'media-reveal':{
      if(!d.src||!/^assets\/[a-zA-Z0-9_./ -]+$/.test(d.src)||d.src.includes('..'))throw new Error('Local media required');
      const video=/\.(mp4|mov|webm|mkv)$/i.test(d.src);const offset=d.in_us??0;
      if(!Number.isInteger(offset)||offset<0)throw new Error('Invalid media offset');
      const media=video?`<video id="broll-${ident(beat.id)}" class="clip" muted playsinline data-start="${beat.start_us/1e6}" data-duration="${(beat.end_us-beat.start_us)/1e6}" data-media-start="${offset/1e6}" data-track-index="6" src="${esc(d.src)}" style="width:100%;max-height:${Math.round((context.height||360)*.25)}px;object-fit:contain"></video>`:`<img src="${esc(d.src)}" style="width:100%;max-height:240px;object-fit:contain">`;
      content=`<figure>${media}<figcaption>${title}</figcaption></figure>`;break;
    }
    case 'lower-third':content=`<div class="lower-third"><strong>${esc(d.name)}</strong><small>${esc(d.role)}</small></div>`;break;
    case 'recap':content=`<small>RESUMO</small><h2>${title}</h2><div class="recap">${items(d).map(x=>`<p>• ${x}</p>`).join('')}</div>`;break;
  }
  const id='motion-'+ident(beat.id), a=beat.start_us/1e6,b=beat.end_us/1e6;const r=box(context.width||640,context.height||360,beat.region||'right',context.caption_zone);
  const videoMedia=effect==='media-reveal'&&/\.(mp4|mov|webm|mkv)$/i.test(d.src);
  const timing=videoMedia?'':`data-start="${a}" data-duration="${b-a}" data-track-index="10"`;
  const html=`<section id="${id}" class="${videoMedia?'':'clip '}motion motion-${effect}" ${timing} style="left:${r.x}px;top:${r.y}px;width:${r.w}px;height:${r.h}px">${content}</section>`;
  const animations=[{target:'#'+id,from:{opacity:0,y:22,scale:.94},to:{opacity:1,y:0,scale:1,duration:Math.min(.35,(b-a)/4),ease:'power3.out'},at:a},{target:'#'+id,from:null,to:{opacity:0,y:-8,duration:Math.min(.18,(b-a)/4)},at:Math.max(a,b-.18)}];
  if(['steps','checklist','flow','recap','timeline'].includes(effect))animations.push({target:`#${id} li, #${id} p, #${id} .flow span, #${id} .timeline div`,from:{opacity:0,x:18},to:{opacity:1,x:0,duration:.18,stagger:.12},at:a+.1});
  if(effect==='chart')animations.push({target:`#${id} .bar-row b`,from:{scaleX:0,transformOrigin:'left'},to:{scaleX:1,duration:.6,stagger:.1},at:a+.12});
  if(effect==='counter')animations.push({target:`#${id} .number`,from:{textContent:0},to:{textContent:d.value,snap:{textContent:Number.isInteger(d.value)?1:.01},duration:Math.min(.8,(b-a)*.4),ease:'power2.out'},at:a+.1});
  if(effect==='morph')animations.push({target:`#${id} .morph-shape`,from:{borderRadius:'50%'},to:{borderRadius:'12%',rotation:8,duration:Math.max(.1,(b-a)*.6)},at:a+.2});
  return {html,animations,bounds:r,diagnostics:[]};
}
