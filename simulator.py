# Very small discrete-event style simulator for "what-if" scenarios.
from datetime import datetime
import uuid

class Simulator:
    def __init__(self):
        self.events = []  # list of (time, action, metadata)

    def schedule(self, action_description, at_time=None, metadata=None):
        evt = {
            "id": str(uuid.uuid4()),
            "time": at_time.isoformat() if hasattr(at_time, 'isoformat') else (at_time or datetime.utcnow()).isoformat(),
            "action": action_description,
            "metadata": metadata or {}
        }
        self.events.append(evt)
        return evt

    def run(self, verbose=False):
        # naive run: iterate events in order of scheduled time
        self.events.sort(key=lambda e: e['time'])
        results = []
        for e in self.events:
            # perform action — here it's a stub: we just record what would happen
            outcome = {"event_id": e['id'], "action": e['action'], "time": e['time'], "outcome": "simulated"}
            results.append(outcome)
            if verbose:
                print(f"[SIM] {e['time']}: {e['action']} -> simulated")
        return results

    def clear(self):
        self.events = []
