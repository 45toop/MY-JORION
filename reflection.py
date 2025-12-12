class Reflector:
    def __init__(self, graph):
        self.graph = graph

    def explain_edge(self, u, v):
        edge = dict(self.graph.g.edges[u, v])
        src = self.graph.get_claim(u)["text"]
        tgt = self.graph.get_claim(v)["text"]
        return {
            "src": src,
            "tgt": tgt,
            "rule": edge.get("rule"),
            "confidence": edge.get("confidence"),
            "explanation": f"Because '{src}' leads to '{tgt}' via rule {edge.get('rule')}"
        }
