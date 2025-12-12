# Very small starter meaning engine. Extend with embeddings / rules later.
from .reasoning_graph import ReasoningGraph

class MeaningEngine:
    def __init__(self, graph: ReasoningGraph):
        self.graph = graph

    def propose_inferences(self):
        # Naive rule: connect consecutive claims as a sequence
        nodes = list(self.graph.g.nodes)
        for a, b in zip(nodes, nodes[1:]):
            # skip if edge exists
            if not self.graph.g.has_edge(a, b):
                self.graph.add_inference(a, b, rule="naive-sequence", confidence=0.6, author="ai")
