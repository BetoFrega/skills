---
name: verb-tense
description: Choose verb tense and mood by when each event happens and how certain it is. Use when writing or reviewing any text, and when a reader asks for a tense review.
---

Agents default to the simple present. Before writing each verb, ask when the event
happens and whether it is a fact, a plan, a condition, or an option. Then pick the
form that says so. Apply the same rules in any language you write.

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
3. A hypothetical condition stated as a fact. "It fails if the key expires" when
   nobody expects it: "it would fail if the key expired". Keep the indicative for
   real, expected conditions: "if the test fails, I will revert".
4. The reader's option described as what happens. "Option B drops the cache":
   "Option B would drop the cache". After the reader chooses, describe the chosen
   path in the future.
5. A possibility stated as certain. "This causes the leak" without proof: "this
   might be causing the leak" or "this is likely the cause". Match the modal to
   the evidence you have.
6. Missing subjunctive or tense in dependent clauses. "If it was ready, I would
   merge" for a hypothesis: "if it were ready". "When it finishes, I tell you":
   "when it finishes, I will tell you". "It is essential that the job runs":
   "that the job run".
7. Simple present for a state that started earlier and continues. "It fails since
   Monday": "it has been failing since Monday".
8. Simple present for an action in progress. "The build runs now": "the build is
   running".
9. No marker for an event before another past event. "When I checked, it already
   failed": "it had already failed".
10. Tense switches inside one account with no change in time. Keep a narrative in
    one time frame and shift only when the event's time shifts.

## Keep the present for

What holds now and stays true: the current contract, how the code behaves, general
facts, and instructions. "The endpoint returns 404 for unknown ids" stays in the
present. Changing these to past or future is also an error.

## Review

Before delivering text, check each verb: when does its event happen relative to
now, is it done, ongoing, planned, possible, or the reader's choice, and does the
form say that. Rewrite every verb that fails.
