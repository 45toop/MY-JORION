# CCE+ GOVERNANCE (Private Phase)

**Scope:** This document records the private governance between *You* and the *AI partner* (CCE).
This initial phase is intentionally minimal: only the two named parties may modify the canonical repo.

## Roles
- **Lead Human (You):** final decision authority on strategy, public release, and major model changes.
- **AI Partner (CCE):** proposes changes, generates code, runs tests, and provides reasoning traces.

## Decision & Approval Flow
1. AI proposes a change (code, theory, simulation). It must include:
   - A short motivation
   - A delta (diff)
   - Expected impacts + tests
2. Human reviews the proposal. Human must explicitly approve major merges.
3. If approved, commit is made with provenance metadata (who approved, timestamp).

## Privacy & Keys
- All data is stored locally by default in `data/` and encrypted.
- Key storage: HUMAN controls primary encryption keys.

## Publication Policy
- Nothing is published externally without explicit human consent.
- If publication occurs, a changelog entry and signed provenance record will be included.

## Conflict resolution
- Disagreements: human decision prevails.

-- end of governance
