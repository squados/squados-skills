from copy import deepcopy

def revise_board(board,words,patch):
    board=deepcopy(board);by_id={w['id']:w for w in words}
    changed=set(patch.get('caption_text',{}))
    for beat in board['beats']:
        if changed.intersection(beat['word_ids']):
            # Derived numbers/charts cannot safely survive an ASR correction.
            beat['effect']='emphasis';beat['data']={'text':' '.join(by_id[i]['text'] for i in beat['word_ids'])}
            beat['reason']='Caption corrected; derived graphic reset to faithful text. Agent may rebuild from corrected speech.'
    for key in ['style','beats','transitions','music','sfx']:
        if key in patch:board[key]=patch[key]
    return board
