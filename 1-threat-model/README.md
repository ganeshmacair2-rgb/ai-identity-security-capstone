# 01 - Threat Model
Method: STRIDE applied to an LLM agent (user input, retrieved documents, tools, secrets, outbound network).
| ID | Threat | STRIDE | OWASP LLM | Asset |
|---|---|---|---|---|
| T1 | Direct prompt injection triggers exfiltration | T/I | LLM01 | Customer data |
| T2 | Indirect injection via retrieved documents | T/I | LLM01 | Customer data |
| T3 | System prompt leaks embedded API key | I | LLM07 | LLM API key |
| T4 | Over-privileged agent identity performs destructive action | E | LLM06 | Databases |
| T5 | Agent trusts forged authority claims | S | LLM09 | Funds |
