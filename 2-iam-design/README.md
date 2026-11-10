# 02 - IAM Design for Agent Identities
1. One unique workload identity per agent (no shared accounts).
2. Short-lived tokens (15 min, OIDC) - no static API keys in prompts or code.
3. Secrets held in a vault; agents receive them just-in-time.
4. Least privilege: scopes `read`,`write` only; `delete`/`transfer` need human approval.
5. Lifecycle: provision -> quarterly review -> 90-day rotation -> decommission within 24h.
See `agent-identity-policy.json`.
