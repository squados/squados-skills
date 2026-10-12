import difflib,re

def semantic_candidates(sentences,duration_us):
    proposed=[]
    for i,a in enumerate(sentences):
        neighbors=sentences[max(0,i-1):i+2]
        if re.match(r'^\s*(editor\b|edição\b|corta (?:isso|essa|este)|tira (?:isso|essa|este))',a['text'],re.I):
            proposed.append({'id':f'instruction-{i}','kind':'editor-instruction','start_us':max(0,a['start_us']-60000),'end_us':min(duration_us,a['end_us']+80000),'context':neighbors,'evidence':'Possible production instruction; distinguish quotation/content by actual audio and context'})
        if i+1==len(sentences):continue
        b=sentences[i+1]
        similarity=difflib.SequenceMatcher(None,a['text'].casefold(),b['text'].casefold()).ratio()
        correction=bool(re.search(r'\b(quer dizer|melhor dizendo|deixa eu repetir|vou repetir)\b',b['text'],re.I))
        if similarity>.45 or correction:
            end=min(b['start_us']-80000,a['end_us']+160000)
            if end>max(0,a['start_us']-60000):proposed.append({'id':f'retake-{i}','kind':'retake','start_us':max(0,a['start_us']-60000),'end_us':end,'context':[a,b],'evidence':'Related adjacent attempts; compare meaning and acoustic borders. Never automatic deletion'})
    return proposed
