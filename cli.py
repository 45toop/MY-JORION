from cce.reasoning_graph import ReasoningGraph
from cce.context_builder import ContextBuilder
from cce.meaning_engine import MeaningEngine
from cce.reflection import Reflector
from cce.theory_bank import TheoryBank
from cce.simulator import Simulator
from cce.provenance import ProvenanceStore
import json
import os

def main():
    print('CCE+ CLI (private prototype)\n---')
    g = ReasoningGraph()
    cb = ContextBuilder(g)
    me = MeaningEngine(g)
    rf = Reflector(g)
    tb = TheoryBank(path=os.path.join(os.getcwd(),'data','theories.json') if os.path.isdir('data') or True else None)
    sim = Simulator()
    prov = ProvenanceStore(db_path=os.path.join(os.getcwd(),'data','provenance.sqlite'))

    os.makedirs('data', exist_ok=True)

    print('Enter text (end with empty line):')
    lines = []
    while True:
        try:
            l = input()
        except EOFError:
            break
        if not l.strip():
            break
        lines.append(l)
    text = " ".join(lines).strip()
    if not text:
        print('No input provided. Exiting.')
        return
    ids = cb.ingest_text(text)
    me.propose_inferences()
    data = g.to_dict()
    print(json.dumps(data, indent=2))
    edges = data.get('edges', [])
    if edges:
        ex = rf.explain_edge(edges[0]['from'], edges[0]['to'])
        print('\nEXPLANATION SAMPLE:')
        print(json.dumps(ex, indent=2))
    # record provenance
    prov.record('ingest', {'text_sample': text[:200], 'claims': len(data.get('nodes',[]))})
    print('\nDone. Data stored locally in folder `data/` and provenance DB.')

if __name__ == '__main__':
    main()
