import test from 'node:test';
import assert from 'node:assert/strict';
import {findHyperframes,renderComposition,finalAudioArgs,canResume} from '../runtime/render.mjs';
test('renderer resolves pinned installed CLI',()=>assert.match(findHyperframes(),/hyperframes[\\/]bin[\\/]hyperframes.mjs$/));
test('invalid quality rejected before spawning',()=>assert.throws(()=>renderComposition('missing','bogus'),/Invalid quality/));
test('final mux preserves separately mastered audio, duration and video',()=>{const args=finalAudioArgs('render.mp4','voice.wav','master.mp4');assert.deepEqual(args.slice(args.indexOf('-map'),args.indexOf('-map')+4),['-map','0:v:0','-map','1:a:0']);assert.ok(args.includes('copy'));});
test('draft cache cannot be resumed for delivery',()=>{assert.equal(canResume({signature:'s',quality:'preview'},'s','final'),false);assert.equal(canResume({signature:'s',quality:'final'},'s','final'),true);});
