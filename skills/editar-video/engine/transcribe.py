def transcribe(audio,model='base',language=None,glossary='',cache=None):
    from faster_whisper import WhisperModel
    from pathlib import Path
    if model=='base':
        from huggingface_hub import snapshot_download
        model=snapshot_download('Systran/faster-whisper-base',revision='ebe41f70d5b6dfa9166e2c581c45c9c0cfc57b66',cache_dir=str(cache),allow_patterns=['*.json','model.bin','vocabulary.txt'])
    elif not Path(model).is_dir():
        raise ValueError('Model must be frozen base or a local model directory')
    instance=WhisperModel(model,device='cpu',compute_type='int8',download_root=str(cache) if cache else None)
    segments,info=instance.transcribe(str(audio),language=language,word_timestamps=True,vad_filter=True,initial_prompt=glossary or None,beam_size=5)
    words=[]; sentences=[]
    for segment in segments:
        sentences.append({'start_us':round(segment.start*1e6),'end_us':round(segment.end*1e6),'text':segment.text})
        for word in segment.words or []:
            a,b=round(word.start*1e6),round(word.end*1e6)
            if b<=a: b=a+1000
            words.append({'id':f'w{len(words)+1}','text':word.word.strip(),'start_us':a,'end_us':b,'probability':word.probability})
    if not words: raise ValueError('No speech transcribed; inspect audio track or provide corrected transcript')
    return {'language':info.language,'language_probability':info.language_probability,'words':words,'sentences':sentences,'model':model,'device':'cpu-int8'}
