# AI Identity Security Capstone

Securing the identities of AI agents: threat model -> IAM design -> red team -> blue team -> policy.

| Folder | Project | Contents |
|---|---|---|
| `01-threat-model/` | P1 | Threat model for LLM agents and their identities |
| `02-iam-design/` | P2 | Agent identity architecture and least-privilege policy |
| `03-red-team/` | P3 | Five attacks against a mock agent (`run_attacks.py`) |
| `04-blue-team/` | P4 | Four-layer guardrails + `live_demo.py` |
| `05-policy/` | P5 | AI Identity Security Policy, compliance mapping, CTO walkthrough |

## Quick start
```bash
python 03-red-team/run_attacks.py     # baseline: 5/5 attacks succeed
python 04-blue-team/live_demo.py      # same attacks with guardrails: 0/5 succeed
```
No dependencies beyond Python 3.8+. All secrets are fake; the "agent" is a deterministic mock so results are reproducible.
