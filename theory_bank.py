import json
from datetime import datetime
import uuid

class TheoryBank:
    """A minimal store for named theories, tests, and results."""
    def __init__(self, path=None):
        self.theories = {}  # name -> theory dict
        self.path = path

    def add_theory(self, name, description, author="human", hypotheses=None):
        tid = str(uuid.uuid4())
        item = {
            "id": tid,
            "name": name,
            "description": description,
            "hypotheses": hypotheses or [],
            "author": author,
            "created_at": datetime.utcnow().isoformat(),
            "tests": []
        }
        self.theories[name] = item
        self._maybe_persist()
        return item

    def add_test(self, theory_name, test_description, result=None):
        t = self.theories.get(theory_name)
        if t is None:
            raise KeyError(f"Theory {theory_name} not found")
        test = {
            "id": str(uuid.uuid4()),
            "description": test_description,
            "result": result,
            "created_at": datetime.utcnow().isoformat()
        }
        t["tests"].append(test)
        self._maybe_persist()
        return test

    def list_theories(self):
        return list(self.theories.values())

    def get_theory(self, name):
        return self.theories.get(name)

    def _maybe_persist(self):
        if not self.path:
            return
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(self.theories, f, indent=2)
