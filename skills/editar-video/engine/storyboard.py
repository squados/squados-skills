from .contracts import Word,validate_storyboard

EFFECTS={'hold','emphasis','counter','comparison','checklist','steps','flow','chart','timeline','quote','definition','problem-solution','callout','interface','morph','concept-map','media-reveal','lower-third','recap'}
CAPTIONS={'block','active-word','karaoke','one-word','keyword','rail','impact','embedded'}
DIRECTIONS={
 'criador':{'fonts':{'base':'Inter','emphasis':'Sora','contrast':'Bebas Neue'},'accent':'#baff54','background':'#101217'},
 'editorial':{'fonts':{'base':'Inter','emphasis':'Fraunces','contrast':'Sora'},'accent':'#ffc678','background':'#181715'},
 'tecnologia':{'fonts':{'base':'Inter','emphasis':'Sora','contrast':'Roboto Mono'},'accent':'#73e5ff','background':'#0a1420'},
 'aula':{'fonts':{'base':'Nunito Sans','emphasis':'Sora','contrast':'Inter'},'accent':'#ffd35f','background':'#141a24'}
}
def default_storyboard(words,direction='criador'):
    beats=[];group=[]
    for word in words:
        group.append(word)
        if word['text'].endswith(('.', '!', '?')) or (word['end_us']-group[0]['start_us']>=3500000):
            beats.append(_beat(group,len(beats)));group=[]
    if group: beats.append(_beat(group,len(beats)))
    return {'direction':direction,'style':DIRECTIONS[direction],'beats':beats,'transitions':[]}
def _beat(group,index):
    return {'id':f'b{index+1}','word_ids':[w['id'] for w in group],'anchor_word_id':group[-1]['id'],'start_us':group[0]['start_us'],'end_us':group[-1]['end_us'],'intent':'statement','effect':'emphasis' if index%3==1 else 'hold','data':{'text':' '.join(w['text'] for w in group)},'caption':['active-word','keyword','block'][index%3],'font_role':['base','emphasis','contrast'][index%3],'region':'right','reason':'Conservative starter; agent reviews intent and replaces with a specific effect when supported.'}
def validate_project_storyboard(words,storyboard):
    typed=[Word(w['id'],w['text'],w['start_us'],w['end_us'],w.get('source_id',w['id'])) for w in words]
    validate_storyboard(typed,storyboard['beats'],storyboard['style']); by_id={w['id']:w for w in words}
    for beat in storyboard['beats']:
        if beat['effect'] not in EFFECTS or beat['caption'] not in CAPTIONS: raise ValueError('Unknown effect/caption')
        selected=[by_id[i] for i in beat['word_ids']]
        if beat['start_us']!=min(w['start_us'] for w in selected) or beat['end_us']!=max(w['end_us'] for w in selected): raise ValueError('Beat clock must come from words')
        if not beat.get('reason'): raise ValueError('Visual decision needs reason')
    return storyboard
