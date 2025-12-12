# Example plugin: small analyzer that counts tokens (naive)
def analyze_claim_text(text):
    toks = text.split()
    return {'token_count': len(toks)}
