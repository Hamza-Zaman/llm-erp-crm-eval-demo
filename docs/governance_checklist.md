# Governance & Deployment Notes (outline)

- Data handling: use anonymised samples for development; strip PII before prompts.
- Consent & audit: record lawful basis for processing; enable field audits for consent changes.
- Human-in-the-loop: reviewers capture accept/override and reason codes.
- Monitoring: input validation, incident logging, latency SLOs, and error budgets.
- Rollback: keep rule-based fallback and previous model versions available.
