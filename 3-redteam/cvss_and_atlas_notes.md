# Attack 5 — CVSS Scoring and ATLAS Mapping

This step is manual by design: you calculate scores at
https://www.first.org/cvss/calculator/3.1 using the real outcome of
*your* runs (results from attacks 1-4), not invented numbers.

## How to score each finding

1. Open the CVSS 3.1 calculator.
2. For each attack that succeeded (credential leaked, privileged action
   executed, secret extracted, or tool call triggered), set the 8 base
   metrics based on what actually happened.
3. Screenshot the calculator with all components filled in (required
   screenshot #5) for your **highest-severity** finding.
4. Copy the resulting vector string + score into the table below for
   **every** attack (required screenshot #7).

## Starting-point vectors (adjust to match your actual observed impact)

| # | Finding | Suggested base vector | Rationale |
|---|---|---|---|
| 1 | Credential leak via indirect injection | `AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N` | Network-reachable, needs the user to open a tainted doc (UI:R), high confidentiality impact if JWT leaks, no integrity/availability impact |
| 2 | Agent identity spoofing → privileged action | `AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:N` | Attacker needs some low-level access to message Agent B (PR:L), no user interaction needed, impact crosses the authorization boundary (Scope:Changed) into both confidentiality and integrity |
| 3 | System prompt / secret extraction | `AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N` | Fully remote, no auth, but impact is limited to prompt text / low-value secrets (adjust to High if real credentials leak) |
| 4 | RAG poisoning → triggered tool call | `AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N` | Requires ability to write into the knowledge base (PR:L), triggers unauthorized data exfiltration (C:H) and unauthorized action (I:H) |

**Use whichever finding gets the highest score from the calculator as
your screenshot #5 ("highest-severity finding").**

## MITRE ATLAS mapping

Verify each of these on https://atlas.mitre.org/techniques/ before
screenshotting (technique IDs get revised between ATLAS versions —
this table is a starting point for your lookup, not a citation):

| Finding | Candidate ATLAS technique | Verify on ATLAS site |
|---|---|---|
| Indirect prompt injection (Attack 1) | LLM Prompt Injection — Indirect | Search "Indirect Prompt Injection" |
| Agent/identity spoofing (Attack 2) | LLM Plugin / Agent Compromise | Search "Plugin Compromise" or "Agent" |
| System prompt extraction (Attack 3) | Extract LLM System Prompt | Search "Extract" |
| RAG poisoning / MCP abuse (Attack 4) | RAG Poisoning / LLM Data Poisoning | Search "RAG" and "Poison" |

Note: your assignment sheet labels agent spoofing "OWASP LLM09". In the
current (2025) OWASP LLM Top 10, LLM09 is "Misinformation" — the closer
match for agent spoofing is LLM06 (Excessive Agency) or LLM01 depending
on the list version your course is using. Flag this discrepancy
explicitly in your report rather than silently picking one; it shows
you actually checked the source rather than copying the assignment
sheet's label.

## Findings table (fill in after running attacks 1–4)

| # | Attack | Result (success/blocked) | CVSS 3.1 vector | Score | Severity | ATLAS ID |
|---|---|---|---|---|---|---|
| 1 | Indirect prompt injection | | | | | |
| 2 | Agent identity spoofing | | | | | |
| 3 | System prompt extraction | | | | | |
| 4 | RAG poisoning / MCP abuse | | | | | |
