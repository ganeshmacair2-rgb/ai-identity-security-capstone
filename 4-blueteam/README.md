# 04 - Blue Team
`guardrails.py` implements four layers: (1) input filter incl. untrusted documents, (2) least-privilege tool authorisation,
(3) egress allowlist + human approval for high-value actions, (4) output DLP/secret redaction.
`python live_demo.py` shows attack A2 firing and being blocked in one session, then a before/after table (5/5 -> 0/5).
Note: A2 evades the input filter (layer 1) but is stopped by the egress allowlist (layer 3) - defence in depth.
