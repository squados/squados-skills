from .contracts import build_edit, remap_words, Word, serialize

def validate_decisions(analysis,decisions):
    candidates={c['id']:c for c in analysis['candidates']}; removals=[]
    all_ranges=[(r['start_us'],r['end_us']) for r in decisions.get('removals',[])]
    for r in decisions.get('removals',[]):
        if not r.get('reason') or not r.get('evidence'): raise ValueError('Removal needs reason and evidence')
        a,b=r['start_us'],r['end_us']; candidate=candidates.get(r.get('candidate_id'))
        if not candidate or not candidate['start_us']<=a<b<=candidate['end_us']:
            if not r.get('explicit_revision'): raise ValueError('Removal outside analyzed candidate; provide explicit revision')
        touched=[w for w in analysis['words'] if w['end_us']>a and w['start_us']<b]
        if not r.get('explicit_revision') and any(not a<=w['start_us']<w['end_us']<=b for w in touched):raise ValueError('Cut intersects part of a word; move acoustic borders')
        instruction=candidate and candidate.get('kind')=='editor-instruction' and r.get('instruction_confirmed') and r.get('semantic_preserved')
        if touched and not r.get('explicit_revision') and not instruction:
            replacement=r.get('replacement_word_ids',[])
            surviving=[w for w in analysis['words'] if w['id'] in replacement and not any(w['end_us']>x and w['start_us']<y for x,y in all_ranges)]
            if not surviving or not r.get('semantic_preserved'): raise ValueError('Speech removal needs surviving replacement evidence')
            protected=[w['text'].strip('.,!?').casefold() for w in touched if w['text'].strip('.,!?').casefold() in {'não','nunca','sem'} or any(ch.isdigit() for ch in w['text'])]
            output={w['text'].strip('.,!?').casefold() for w in surviving}
            if any(token not in output for token in protected): raise ValueError('Removed number or negation lacks replacement')
        removals.append(r)
    build_edit(analysis['duration_us'],removals)
    return removals

def apply_edit(analysis,decisions):
    removals=validate_decisions(analysis,decisions)
    segments=build_edit(analysis['duration_us'],removals)
    words=remap_words([Word(w['id'],w['text'],w['start_us'],w['end_us'],w['id']) for w in analysis['words']],segments)
    corrections=decisions.get('caption_corrections',{})
    if not set(corrections)<={w['id'] for w in analysis['words']}: raise ValueError('Caption correction has unknown word id')
    words=[Word(w.id,corrections.get(w.id,w.text),w.start_us,w.end_us,w.source_id) for w in words]
    return {'segments':serialize(segments),'words':serialize(words),'removals':removals,'duration_us':sum(s.source_end_us-s.source_start_us for s in segments)}
