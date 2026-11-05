"""Scan material Lean source, check probe coverage, and inspect final axiom output.

Run: py -3 formalization/validate.py (standard library only).
This diagnostic complements, and never substitutes for, the Lean build.
"""
from pathlib import Path
import json
import re


def mask(text):
    """Mask nested comments, quoted identifiers and literal strings positionally."""
    out = list(text)
    i = 0
    while i < len(text):
        end = i
        if text.startswith('--', i):
            end = text.find('\n', i)
            if end < 0: end = len(text)
        elif text.startswith('/-', i):
            end, depth = i + 2, 1
            while end < len(text) and depth:
                if text.startswith('/-', end): depth += 1; end += 2
                elif text.startswith('-/', end): depth -= 1; end += 2
                else: end += 1
        elif text[i] == '«':
            end = text.find('»', i + 1)
            end = len(text) if end < 0 else end + 1
        else:
            raw = re.match(r'r(#+)?"', text[i:]) if text[i] == 'r' else None
            if raw:
                close = '"' + (raw.group(1) or '')
                end = text.find(close, i + len(raw.group(0)))
                end = len(text) if end < 0 else end + len(close)
            elif text[i] == '"':
                end = i + 1
                while end < len(text):
                    if text[end] == '\\': end += 2
                    elif text[end] == '"': end += 1; break
                    else: end += 1
        if end > i:
            for k in range(i, min(end, len(text))):
                if out[k] not in '\r\n': out[k] = ' '
            i = end
        else: i += 1
    return ''.join(out)


root = Path(__file__).resolve().parent
sources = sorted(root.glob('*.lean'))
hits, declarations = [], []
for path in sources:
    code = mask(path.read_text(encoding='utf-8-sig'))
    for m in re.finditer(r'\b(sorry|admit|axiom|unsafe|native_decide|sorryAx)\b', code):
        hits.append({'file': path.name, 'line': code.count('\n',0,m.start())+1,
                     'token': m.group(0)})
    declarations += ['ConjectureA1.'+n for n in
                     re.findall(r'\b(?:lemma|theorem)\s+([\w\']+)', code)]
probe = mask((root/'AxiomAudit.lean').read_text(encoding='utf-8'))
missing = [d for d in declarations if f'#print axioms {d}' not in probe]
log = (root/'evidence/lake-build.log').read_text(encoding='utf-8-sig')
axioms = {}
for d in declarations:
    m = re.search(r"'"+re.escape(d)+r"' depends on axioms: \[([^\]]*)\]", log)
    if m: axioms[d] = [s.strip() for s in m.group(1).split(',') if s.strip()]
    elif f"'{d}' does not depend on any axioms" in log: axioms[d] = []
allowed = {'propext','Classical.choice','Quot.sound'}
bad = {d:a for d,a in axioms.items() if not set(a) <= allowed}
result = {'sources': [p.name for p in sources], 'forbidden_code_tokens': hits,
          'theorem_count': len(declarations), 'missing_axiom_probes': missing,
          'unreported_axiom_sets': sorted(set(declarations)-set(axioms)),
          'axioms': axioms, 'disallowed_axioms': bad,
          'lake_build_exit_zero': 'Build completed successfully' in log and 'EXIT=0' in log}
result['passed'] = (not hits and not missing and not bad and
                    len(axioms)==len(declarations) and result['lake_build_exit_zero'])
print(json.dumps(result, ensure_ascii=False, indent=2))
raise SystemExit(0 if result['passed'] else 1)
