# Security by Design

Treat security as a requirement of every change that touches a trust boundary, and
decide it while designing.

- **Find the trust boundaries.** Before building, name where data or control crosses
  from a less trusted side: users, the network, other tenants, third-party services,
  uploaded files, model output. Name what an attacker gains if each one fails. Scale
  the effort to that exposure; an internal script needs less than a public endpoint.
- **Validate what crosses.** Validate and parse untrusted input at the boundary per
  Boundary Discipline. Encode output for its sink, and use parameterized queries and
  argument arrays instead of building SQL, shell, or HTML strings.
- **Deny by default.** Check authentication and authorization on the server for every
  request and every object; a UI check alone does not count. Defaults are closed, and errors fail
  closed.
- **Least privilege.** Give code, tokens, service accounts, and agents only the
  permissions and data the task needs, for only as long as it needs them.
- **Keep secrets out of artifacts.** Secrets and personal data stay out of source,
  logs, URLs, error messages, prompts, and tickets. Load secrets from the platform's
  secret store.
- **Use vetted mechanisms.** Prefer the framework's or platform's security features
  and maintained libraries over custom cryptography, sessions, or sanitizers. Treat a
  new dependency as code you run with your privileges.
- Fail Loud, Handle on Evidence decides how much handling to add; this principle
  decides what must be refused, even when the case is rare.

**Check:** for each boundary the change touches, name the untrusted input, where it is
validated, who is allowed through, and what the code can reach if that check is
bypassed. A boundary with no answer blocks delivery.
