"""Annotated corpus runner. Every case runs the shared CLI, not a parallel editing engine."""
import argparse,json,re,subprocess,sys
from pathlib import Path
from datetime import datetime
ROOT=Path(__file__).resolve().parents[1]

def run_corpus(corpus,output=None):
    corpus=Path(corpus).resolve();manifest=corpus/'manifest.json' if corpus.is_dir() else corpus
    cases=json.loads(manifest.read_text(encoding='utf-8-sig'))['cases']
    if not cases:raise ValueError('Corpus needs annotated cases')
    output=Path(output) if output else manifest.parent/('results-'+datetime.now().strftime('%Y%m%d-%H%M%S-%f'))
    output.mkdir(parents=True,exist_ok=False);results=[]
    for i,case in enumerate(cases):
        folder=output/(str(i+1)+'-'+re.sub('[^a-zA-Z0-9_-]','_',case['name']));folder.mkdir()
        project=folder/'project';logs=folder/'logs';logs.mkdir()
        def call(command,*args):
            completed=subprocess.run([sys.executable,str(ROOT/'scripts/run.py'),command,'--project',str(project),*map(str,args)],capture_output=True,text=True,encoding='utf-8',errors='replace')
            (logs/(command+'-'+str(len(list(logs.iterdir())))+'.log')).write_text(completed.stdout+'\n'+completed.stderr,encoding='utf-8')
            if completed.returncode:raise RuntimeError(completed.stderr)
            return json.loads(completed.stdout)
        try:
            opts=['--input',manifest.parent/case['input'],'--model',case.get('model','base')]
            if case.get('transcript'):opts+=['--transcript',manifest.parent/case['transcript']]
            if case.get('language'):opts+=['--language',case['language']]
            call('prepare',*opts)
            if case.get('expected_error'):raise AssertionError('Expected diagnostic failure, but prepare succeeded')
            if case.get('decisions'):(project/'decisions.json').write_bytes((manifest.parent/case['decisions']).read_bytes())
            call('apply')
            if case.get('storyboard'):(project/'storyboard.json').write_bytes((manifest.parent/case['storyboard']).read_bytes())
            call('compose');call('render','--quality','preview');call('render','--quality','final')
            qa=call('qa')
            if not qa['technical_passed']:raise AssertionError('Technical QA failed')
            call('export');text=(project/'transcript.txt').read_text(encoding='utf-8').casefold()
            if any(s.casefold() not in text for s in case.get('expected_text',[])):raise AssertionError('Annotated content missing from exported transcript')
            results.append({'case':case['name'],'passed':True,'review_status':qa['review_status']})
        except Exception as error:
            expected=case.get('expected_error')
            passed=isinstance(error,RuntimeError) and expected is not None and expected.casefold() in str(error).casefold()
            results.append({'case':case['name'],'passed':passed,'diagnostic':str(error)[-1800:]})
    report={'passed':all(r['passed'] for r in results),'cases':results,'output':str(output),'editorial_approval':False}
    (output/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    return report

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--corpus',required=True);parser.add_argument('--output');args=parser.parse_args()
    result=run_corpus(args.corpus,args.output);print(json.dumps(result,ensure_ascii=False,indent=2));raise SystemExit(not result['passed'])
