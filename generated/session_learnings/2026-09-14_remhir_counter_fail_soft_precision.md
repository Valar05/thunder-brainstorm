# Remhir Counter — Fail-Soft Precision Addendum — 2026-09-14

## Evidence status

The surviving `Remhir.blend` directly verifies separate `Block`, `Block_hold`, `Counter`, and `Parry` actions, and the prior excavation measured `Counter` as a whole-body reversal involving hands, torso, feet, head, wing controls, and a keyed `Hitbox` control.

The exact shipped input/timing contract described below is **USER_MEMORY** from Drew and is not yet source-verified from gameplay code.

## Drew's remembered interaction law

Drew remembers Remhir's counter as substantially more satisfying than the Dark Souls-style parry proposition because the skill attempt degraded safely:

```text
press defensive / counter input
-> precise timing: COUNTER / REVERSAL
-> imperfect timing: BLOCK
-> badly mistimed / outside defensive window: FAILURE
```

The key remembered preference is not "parry should be easy." It is:

> A precision defense should improve a safe defensive action rather than replace it with a separate all-or-nothing gamble.

Drew's critique of Dark Souls parry is explicitly about his own player utility: if a failed parry exposes the player to a full hit, while `attack twice + block` produces reliable offense and defense, then parry becomes a poor proposition for him even if the successful riposte reward is larger.

## Nested timing model

Working model:

```text
COUNTER_WINDOW ⊂ BLOCK_WINDOW
```

One defensive intention produces graded outcomes.

Let:

- `B` = value of a successful ordinary block;
- `C` = value of a counter / reversal, with `C > B`;
- `H` = value after a failed high-risk parry that eats the hit, with `H << B`;
- `p` = probability of landing the precision window.

A fail-soft counter behaves approximately like:

```text
U_fail_soft = B + p(C - B) - small_execution_cost
```

A fail-hard parry behaves approximately like:

```text
U_fail_hard = pC + (1-p)H - execution_cost
```

This explains how Remhir's counter could be **easy to attempt, still satisfying, and not trivial**. The floor stays near ordinary defense; mastery raises the ceiling through timing, initiative reversal, and extra payoff.

## Why this matters for minimalist combat

This is not merely a kinder parry.

It increases state depth without increasing verb count.

Instead of:

```text
ATTACK
BLOCK
PARRY
COUNTER
```

as four largely separate propositions, the system can collapse defense into one layered verb:

```text
DEFEND
-> ordinary read: BLOCK
-> excellent read: COUNTER
```

The player learns a gradient rather than a binary trap.

That is especially valuable in an infinite minimalist loop because the same small input vocabulary can continue yielding skill expression without requiring a larger move list.

## Animation consequence

The source's separate `Block`, `Block_hold`, `Counter`, and `Parry` actions suggest a body grammar that can visibly preserve the shared defensive intention while branching at the moment of successful read:

```text
WIDE / READY
-> WING COMPRESSION / RECEIVE
-> either HOLD DEFENSE
-> or REVERSE OWNERSHIP
-> RE-EXPAND
```

That makes the counter feel like a superior continuation of defense rather than an unrelated special move.

## Design law candidate

**FAIL-SOFT PRECISION:**

> Put the high-skill outcome inside the safe base action whenever the fantasy is "do the same thing better," not "gamble on a different thing."

This preserves accessibility without flattening mastery.

Do not promote this as universal doctrine from one remembered game. Test it against later Drew combat systems and surviving gameplay code when available.
