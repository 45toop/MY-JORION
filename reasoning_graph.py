import networkx as nx
import uuid
from datetime import datetime

class ReasoningGraph:
    def __init__(self):
        self.g = nx.DiGraph()

    def add_claim(self, text, author="human", metadata=None):
        node_id = str(uuid.uuid4())
        node = {
            "id": node_id,
            "text": text,
            "author": author,
            "created_at": datetime.utcnow().isoformat(),
            "metadata": metadata or {}
        }
        self.g.add_node(node_id, **node)
        return node_id

    def add_inference(self, src_id, tgt_id, rule=None, confidence=0.5, author="ai", metadata=None):
        edge = {
            "rule": rule or "unspecified",
            "confidence": float(confidence),
            "author": author,
            "created_at": datetime.utcnow().isoformat(),
            "metadata": metadata or {}
        }
        self.g.add_edge(src_id, tgt_id, **edge)

    def get_claim(self, node_id):
        return dict(self.g.nodes[node_id])

    def to_dict(self):
        nodes = [{**{"node_id": n}, **self.g.nodes[n]} for n in self.g.nodes]
        edges = [{**{"from": u, "to": v}, **self.g.edges[u, v]} for u, v in self.g.edges]
        return {"nodes": nodes, "edges": edges}
