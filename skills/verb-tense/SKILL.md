---
name: verb-tense
description: Choose verb tense and mood by when each event happens and how certain it is. Use when writing or reviewing any text, and when a reader asks for a tense review.
---

Agents default to the simple present. The habit likely comes from technical genres
where the present is a convention regardless of time: docstrings, PR descriptions
and commits, test names, tutorials, and specs. Outside those conventions, the
present tells the reader that something is true now.

Before writing each verb, ask when the event happens and whether it is a fact, a
plan, a condition, or an option. Then pick the form that says so. Apply the same
rules in any language you write.

Test every present-tense verb: if the reader checked the system right now, would
the sentence be true? If not, the present is wrong.

## Available forms

- Simple, progressive, perfect, and perfect progressive, each in past, present, and
  future: "ran", "was running", "had run", "had been running", "will have run".
- Modals for conditions and possibility: would, could, might, should.
- The subjunctive: "if it were", "I suggest it be".
- Other languages have their own sets; Portuguese, for example, adds a future
  subjunctive. Use every form the language you write in offers.

## Errors to fix

1. Present for something already done. "I open the PR" when it is open: "I
   opened the PR". "CI passes" about one finished run: "CI passed".
2. Present for something that has not happened yet. "After merge, the hook asks
   for review": "the hook will ask".
3. Present for planned or unimplemented behavior, in any document. "The endpoint
   returns 404" in a plan, status, or spec while it returns 500 today: "after this
   change, the endpoint will return 404", or, for a contract, "the endpoint MUST
   return 404".
4. A hypothetical condition stated as a fact. "It fails if the key expires" when
   nobody expects it: "it would fail if the key expired". Keep the indicative for
   real, expected conditions: "if the test fails, I will revert".
5. The reader's option described as what happens. "Option B drops the cache":
   "Option B would drop the cache". After the reader chooses, describe the chosen
   path in the future.
6. A possibility stated as certain. "This causes the leak" without proof: "this
   might be causing the leak" or "this is likely the cause". Match the modal to
   the evidence you have.
7. Missing subjunctive or tense in dependent clauses. "If it was ready, I would
   merge" for a hypothesis: "if it were ready". "When it finishes, I tell you":
   "when it finishes, I will tell you". "It is essential that the job runs":
   "that the job run".
8. Simple present for a state that started earlier and continues. "It fails since
   Monday": "it has been failing since Monday".
9. Simple present for an action in progress. "The build runs now": "the build is
   running".
10. No marker for an event before another past event. "When I checked, it already
   failed": "it had already failed".
11. Tense switches inside one account with no change in time. Keep a narrative in
    one time frame and shift only when the event's time shifts.

## Keep the present for

What holds now and stays true: the current contract, how the code behaves today,
general facts, and instructions. "The endpoint returns 404 for unknown ids" stays in
the present when it already does. Changing these to past or future is also an
error.

## Contracts not yet met

State requirements with [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) keywords
(MUST, MUST NOT, SHOULD, SHOULD NOT, MAY) instead of the present. They state the
obligation without claiming it is met, so the text stays correct before and after
delivery. Per [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174), they carry that
meaning only in uppercase. When a requirement ships and the text becomes reference
documentation, describe the behavior in the present.

## Review

Before delivering text, check each verb: when does its event happen relative to
now, is it done, ongoing, planned, possible, or the reader's choice, and does the
form say that. Apply the right-now test to every present-tense verb. Rewrite every
verb that fails.
