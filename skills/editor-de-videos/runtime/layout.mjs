export const esc=s=>String(s??'').replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;').replaceAll("'",'&#39;');
export const ident=s=>String(s).replace(/[^a-zA-Z0-9_-]/g,'_');
export function box(width,height,region='right',captionZone='bottom') {
  const pad=Math.round(Math.min(width,height)*.055);
  if(region==='full') return {x:pad,y:pad,w:width-2*pad,h:height*.56};
  const w=Math.min(width*.43,600);return {x:region==='left'?pad:width-pad-w,y:height*(captionZone==='top'?.37:.08),w,h:height*(captionZone==='top'?.43:.49)};
}
export function fitText(element,min=16,max=72) {
  element.style.fontSize=max+'px';
  while((element.scrollWidth>element.clientWidth+1||element.scrollHeight>element.clientHeight+1)&&max>min) element.style.fontSize=(--max)+'px';
  return max;
}
