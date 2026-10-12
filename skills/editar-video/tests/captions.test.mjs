import test from 'node:test'; import assert from 'node:assert/strict';
import {fontForBeat,buildCaptions,CAPTION_STYLES} from '../runtime/captions.mjs';
test('eight treatments and semantic font roles',()=>{assert.equal(CAPTION_STYLES.length,8); assert.equal(fontForBeat({font_role:'emphasis'},{fonts:{base:'Inter',emphasis:'Sora'}}),'Sora');});
test('caption text escaped, timing preserved, foreground fallback explicit',()=>{const out=buildCaptions({words:[{id:'w1',text:'<não>',start_us:500000,end_us:1000000}],beats:[{id:'b1',word_ids:['w1'],caption:'embedded',font_role:'base'}],style:{fonts:{base:'Inter'}},framePlan:{width:640,height:360}}); assert.match(out.html,/&lt;não&gt;/); assert.match(out.html,/data-start="0.5"/); assert.equal(out.diagnostics[0].code,'embedded-fallback');});
