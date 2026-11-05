---
name: verb-tense
description: Choose verb tense and mood by when each event happens and how certain it is. Use when writing or reviewing any text, and when a reader asks for a tense review.
---

Agents default to the simple present. Before writing each verb, ask when the event
happens and whether it is a fact, a plan, a condition, or an option. Then pick the
form that says so. Examples are in English and Brazilian Portuguese because both
appear in this work; apply the same rules in either language.

## Available forms

- Portuguese: presente; pretérito perfeito (fiz), imperfeito (fazia), mais-que-perfeito
  (tinha feito, fizera); futuro do presente (farei, vou fazer); futuro do pretérito
  (faria); periphrases for ongoing or continuing action (estou fazendo, venho
  fazendo); subjuntivo presente (faça), imperfeito (fizesse), and futuro (fizer).
- English: simple, progressive, perfect, and perfect progressive, each in past,
  present, and future; modals for conditions and possibility (would, could, might);
  the subjunctive ("if it were", "I suggest it be").

## Errors to fix

1. Present for something already done. "Abro o PR" when the PR is open: "Abri o
   PR". "CI passes" about one finished run: "CI passed".
2. Present for something that has not happened yet. "Depois do merge, o hook pede
   revisão": "vai pedir". "After merge, the hook asks": "will ask".
3. A hypothetical condition stated as a fact. "Isso quebra se a chave expirar" when
   nobody expects it: "quebraria se a chave expirasse". "It fails if the key
   expires": "it would fail if the key expired". Keep the indicative for real,
   expected conditions: "se o teste falhar, vou reverter".
4. The reader's option described as what happens. "A opção B remove o cache": "A
   opção B removeria o cache". "Option B drops the table": "would drop". After the
   reader chooses, describe the chosen path in the future.
5. A possibility stated as certain. "Isso causa o bug" without proof: "isso pode
   estar causando o bug" or "deve ser isso". "This causes the leak": "this might be
   causing the leak". Match the modal to the evidence you have.
6. Missing subjunctive. "Se você quer": "se você quiser". "Quando termina, aviso":
   "quando terminar, aviso". "É preciso que o job roda": "que o job rode".
7. Simple present for a state that started earlier and continues. "O teste falha
   desde segunda": "vem falhando desde segunda". "It fails since Monday": "it has
   been failing since Monday".
8. Simple present for an action in progress. "O CI roda agora": "está rodando".
   "The build runs now": "is running".
9. No marker for an event before another past event. "Quando vi, o deploy já
   falhou": "já tinha falhado". "When I checked, it already failed": "it had
   already failed".
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
