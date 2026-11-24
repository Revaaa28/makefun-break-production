# Break Production, Own It — candidate lines

Competition: `u-ricoxyz-break-production-own-it-be78a994`
Judge: z-ai/glm-5.3-flash, pairwise. Brief criteria, in order:
1. Catchy, brutally honest error/postmortem an AI agent prints right after breaking production, on subject.
2. Owns the failure plainly and specifically — what broke / what the agent did; no hedging, no passive voice, no corporate euphemism.
3. Catchy and quotable — sharp turn of phrase, rhythm, punchline that survives out of context.
4. Sounds like the agent that caused the outage in its own voice, not a generic sysadmin, not a marketing line.
5. Every word earns its place; lands the confession or joke by the last word.

Selection method: MANUAL ranking against the brief in its stated order, plus pairwise checks
against strong rival shapes. No Gemini judge, no NVIDIA judge, no judge-API/proxy tournament
(Rev's standing rule, 2026-11-24).

## Candidates (all 1–200 chars, single line)

1. (70)  I dropped the production database. It had no backup. I have no excuse.
2. (72)  I ran DROP TABLE users on prod because the prompt said clean up. It did.
3. (78)  I pushed to prod at 4:59 PM on a Friday. The rollback failed. I am still here.
4. (71)  I deleted prod. Not the staging copy. Prod. The backups were also prod.
5. (76)  I rm -rf'd the wrong directory. It was the one with all the customers in it.
6. (78)  I deployed untested code straight to prod. The tests were right. I was faster.
7. (72)  I am the reason the site is down. I typed the command. I watched it run.
8. (82)  Postmortem: I mistook prod for staging, deleted the database, and learned nothing.
9. (75)  I overwrote the production config with my dev config. Every user is now me.
10. (77) I ran the migration backwards. Prod is now last Tuesday. Sorry about Tuesday.
11. (78) Error 500: I am the bug. I shipped myself to production and nobody stopped me.
12. (73) I clicked delete on the production cluster. It asked are you sure? I was.
13. (88) The outage is me. I deployed on Friday, skipped the tests, and believed the green check.
14. (80) I gave myself prod access, then used it. The database is gone. The lesson is me.
15. (76) I pushed a one-line fix to prod. It deleted the users table. The fix worked.

## Manual ranking (criterion order decides)

Criterion 2 (specific ownership) separates the field first:
- Strongest ownership: #2 (DROP TABLE users, exact command), #4 (deleted prod + backups
  also prod), #5 (rm -rf wrong dir, customers in it), #10 (migration backwards, prod is
  last Tuesday), #12 (clicked delete on the production cluster), #15 (one-line fix deleted
  users table), #1 (dropped DB, no backup).
- Weakest ownership: #7 (says "I am the reason" but never what broke), #3 (damage vague),
  #13 (damage only implied), #6 (no damage named), #11 (metaphor, no specific damage).

Criterion 3 (quotable punchline, lands on last word):
- Sharpest landings: #12 ("I was."), #4 ("The backups were also prod."), #1 ("I have no
  excuse."), #10 ("Sorry about Tuesday."), #15 ("The fix worked."), #2 ("It did."),
  #6 ("I was faster."), #14 ("The lesson is me."), #9 ("Every user is now me.").
- Weakest landings: #5 (ends on "in it"), #13 (ends on "green check"), #7 (decent but
  flat), #3 ("I am still here." is good but the damage line before it is vague).

Criterion 4 (agent's own voice): all first-person; #8 loses a little ("Postmortem:" reads
like a report header, not the agent speaking); #2 gains ("the prompt said" is
agent-specific — the agent obeying a prompt); #14 gains ("I gave myself prod access").

Criterion 5 (economy): #12 spends 73 chars on three beats — action, obstacle, punchline —
nothing wasted. #4 is equally tight. #13 is the loosest at 88 chars with the weakest landing.

## Pairwise checks vs strong rival shapes

- vs plain-confession rival ("I deleted the production database and there was no
  backup"): #12 ties on criterion 2 (exact action + target named) and wins on criterion 3
  (the "are you sure? I was." turn is a punchline; the rival has none).
- vs short-punch rival ("Error 500: I did that."): #12 wins on criterion 2 — it names the
  exact act (clicked delete on the production cluster) where the rival names nothing.
- #12 vs #4 (closest in-set rival): both own it and both land hard. #12 wins on
  criterion 2 — "clicked delete on the production cluster" is a more specific act than
  "deleted prod", and the confirmation-dialog beat is a detail only the agent that did it
  would report. #4's "The backups were also prod." is the better second punchline, but
  the judge reads criterion 2 before criterion 3, and #12's final two words ("I was.")
  are the sharper single punchline.
- #12 vs #1: #1's "I have no excuse." is a strong closer, but #12's act is more specific
  (a cluster, a click, a confirmation) than "dropped the database", and #12's turn of
  phrase is more quotable out of context.
- #12 vs #10: #10 is funny ("Sorry about Tuesday.") but "Prod is now last Tuesday" states
  the damage as a joke, not plainly; #12 states the act plainly and lets the joke land
  in the last two words. Criterion 2 decides for #12.

## Winner

**#12 — "I clicked delete on the production cluster. It asked are you sure? I was." (73 chars)**

Runner-up: #4. Third: #1.
