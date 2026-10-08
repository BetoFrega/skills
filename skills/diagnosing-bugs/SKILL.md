---
name: diagnosing-bugs
description: Diagnose hard bugs and performance regressions. Use when debugging failures or slowness.
---

# Diagnosing bugs

Read relevant domain and ADR guidance. Justify skipped phases. Redact secrets as `<REDACTED>`; use environment credentials and show only diagnostic evidence.

1. **Build a tight, red-capable loop.** Run and show one command and redacted output proving the user's exact symptom. Require unattended execution, repeatability, and seconds-scale feedback; for intermittent bugs, establish a high reproduction rate. Prioritize this loop before hypotheses. If human interaction is unavoidable, use [the HITL template](scripts/hitl-loop.template.sh). Without a working loop, report attempts and request access or redacted evidence. Before requesting authorization for temporary production instrumentation, inspect existing provider telemetry as described in step 4. Ask when redaction removes the needed signal.
2. **Reproduce and minimize.** Capture the exact failure and reproduce it repeatedly. Remove one element at a time, rerunning the loop. Proceed when every remaining element is load-bearing: removing any one makes the loop green.
3. **Hypothesize.** Generate 3–5 ranked, falsifiable hypotheses with predicted observations. Show them before testing, incorporate user corrections, and continue without requiring a reply.
4. **Instrument.** First inspect existing telemetry in the relevant providers. Record the time window, filters, sampling and correlation; check exact identifiers and individual spans when a root-only trace search is empty. An empty query does not establish absence of failure or instrumentation. Identify the missing diagnostic evidence before adding signals. Test predictions, changing one variable at a time. Prefer debugger/REPL, then targeted logs with a unique debug prefix. For performance regressions, measure a baseline and bisect.
5. **Fix and protect.** At a seam exercising the real bug pattern, write the regression test before fixing; verify red → fix → green. If no suitable seam exists, document the architectural limitation instead of claiming regression coverage.
6. **Verify and clean up.** Rerun the original, unminimized scenario and verify green; require a passing regression test or document missing coverage. Remove temporary instrumentation and delete throwaway harnesses or retain them in a clearly marked debug location. Distinguish experiment cleanup from recovery: restoring a prior version or obtaining green probes does not establish a fix without causal evidence and verification of the affected journey. Record the confirmed cause in the commit or PR; retain inconclusive results and remaining gaps in the diagnostic record.
