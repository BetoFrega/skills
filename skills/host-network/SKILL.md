---
name: host-network
description: Request host execution when sandbox network restrictions cause connection failures or misleading CLI authentication errors, including gh.
---

# Host Network

When a network command fails inside the sandbox, check whether DNS, connection, or permission errors explain the failure. Treat CLI reports of missing or invalid authentication as provisional when network access is restricted.

Use the execution tool's approved host-access mechanism. With `exec_command`, request `sandbox_permissions: "require_escalated"` with the specific command and a justification explaining the sandbox restriction and required destination. Execute after approval; if escalation is unavailable or denied, report the blocker and continue independent work.

For suspected authentication failures, first run a minimal read-only request on the host using existing credentials, such as `gh api user --jq .login`. A successful response confirms authentication; resume the authorized operation through approved host execution. Diagnose persistent host failures from their actual errors before requesting login or credential changes.

Host access preserves the original task scope and action permissions. Before retrying a write whose outcome is uncertain, reconcile remote state. Keep credentials out of output and chat.
