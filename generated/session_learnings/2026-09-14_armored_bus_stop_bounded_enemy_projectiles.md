# Armored Bus Stop — bounded enemy projectiles

Live playtest correction: continuous survivor-like pressure made ranged enemies feel unavoidable because their tracers were effectively hitscan damage. That turns ranged pressure into attrition tax instead of a dodgeable threat.

Correction:

- Enemy ranged fire is now represented by real world-space projectiles with bounded speed.
- Rifle, gunner, flanker, and heavy shots each have fixed launch speed, lifetime, radius, and damage profile.
- Shooters commit to a firing solution at launch. Projectiles do not home or retroactively correct after the player moves.
- Suppression and shock may worsen aim before launch, but do not alter projectile speed in flight.
- Swept collision is used so fast shots do not tunnel through the APC or commandos.
- Friendly squad fire may remain fast/hitscan for now; the important correction is that incoming player-facing ranged pressure is readable and dodgeable.

Design rule:

> Continuous pressure needs avoidable danger, not unavoidable taxation.

Or more mechanically:

> Commit the shooter, bound the projectile, let movement create the miss.

Smoke-test evidence for this specimen: enemy fire spawned physical projectiles, APC health did not change at fire time, projectile speeds stayed within the configured 175–315 world-units/s envelope, and a 0.1 s update advanced the sampled rifle projectile exactly 24.5 world units at 245 units/s.
