"""Named check entrypoint; unit suites require only Python's standard library."""
import argparse
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--suite',default='all')
    parser.add_argument('--e2e');parser.add_argument('--output')
    args=parser.parse_args()
    pattern='test_*.py' if args.suite=='all' else f'test_{args.suite}.py'
    suite=unittest.defaultTestLoader.discover(str(ROOT/'tests'),pattern=pattern)
    if not suite.countTestCases(): raise SystemExit('No tests found for requested suite')
    passed=unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()
    if passed and args.e2e:
        from e2e import run_corpus
        import json
        result=run_corpus(args.e2e,args.output);print(json.dumps(result,ensure_ascii=False,indent=2));passed=result['passed']
    raise SystemExit(not passed)

if __name__=='__main__': main()
