from .reasoning_graph import ReasoningGraph
import re

class ContextBuilder:
    def __init__(self, graph: ReasoningGraph):
        self.graph = graph

    def ingest_text(self, text, author="human"):
        # naive split into sentences; improvements: use spaCy / punctuation models
        sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if s.strip()]
        ids = []
        for s in sentences:
            nid = self.graph.add_claim(s, author=author)
            ids.append(nid)
        return ids
