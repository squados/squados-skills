export const TRANSITIONS=['cut','dissolve','match-graphic','wipe','slide','zoom-bridge'];
export function buildTransition(boundary,handles={}) {
  if(!TRANSITIONS.includes(boundary.type))throw new Error('Unknown transition');
  const duration_us=boundary.duration_us??300000;
  if(!Number.isFinite(boundary.at_us)||boundary.at_us<0||!Number.isFinite(duration_us)||duration_us<0||duration_us>1000000)throw new Error('Invalid transition clock');
  if(boundary.type!=='cut'&&(!Number.isFinite(handles.before_us)||!Number.isFinite(handles.after_us)||handles.before_us<duration_us/2||handles.after_us<duration_us/2))return {...boundary,type:'cut',duration_us:0,reason:'Insufficient handles; voice unchanged'};
  return {...boundary,duration_us:boundary.type==='cut'?0:duration_us};
}
