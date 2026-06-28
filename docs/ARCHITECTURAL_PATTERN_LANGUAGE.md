# Architectural Pattern Language

Version: 0.4
Status: Self-Correcting Generator Contract

This corpus is a procedural architecture brain, not a style guide. Use it as `World constraints -> District -> Phrase -> Assembly -> Primitive -> Voxel/material`.

A generator must not place architectural nouns in isolation. Every generated structure must declare structural purpose, gameplay purpose, sightline purpose, support validity, and circulation validity.

## Hierarchy

VOXEL
Raw occupancy/material cell. Owns solidity, material, and destruction state.

PRIMITIVE
Box, slab, stair step, pier, column, arch segment, void cut, rail, lip. Owns measurable geometry.

STRUCTURAL ATOM
Reusable support or termination unit such as Wall Bay, Buttress, Retaining Wall, Bridge Pier, or Parapet.

ASSEMBLY
Playable architectural noun such as Gatehouse, Courtyard, Shaft, Bridge Span, or Catwalk.

PHRASE
Ordered sequence of assemblies/atoms with entry, exit, purpose, and validation rules.

ROOM
Bounded playable situation. Owns route choices, threat/readability, and local purpose.

DISTRICT
Connected room/phrase graph with a shared function such as dock, foundry, fortress, quarry, or station.

CITY
District graph plus landmarks, infrastructure, skyline, and civic/logistic circulation.

WORLD
Biome, era, gravity, material palette, macro route, and impossible/required structure rules.


## Validation Contracts

Validation belongs to every hierarchy level. Higher layers must not hide lower-layer invalidity; a district with a good skyline still fails if its bridges float or its routes do not connect.

VOXEL
Requires: solid or empty state, valid material id, valid neighbor references, no orphan material state.
Reject if: unknown material, contradictory occupancy, invalid neighbor coordinates, unsupported destruction state.
Rationale: bad cell truth poisons every higher structure.

PRIMITIVE
Requires: measurable dimensions, valid orientation, valid transform, support or explicit suspension rule.
Reject if: zero/negative dimensions, impossible rotation, floating slab without support, unbounded void cut.
Rationale: primitives are the first place geometry can become impossible.

STRUCTURAL ATOM
Requires: correct attachment, valid proportions, non-floating placement, valid termination when repeated.
Reject if: wall bay has no wall run, pier has no load, parapet has no edge, buttress supports nothing.
Rationale: atoms explain why assemblies look built instead of pasted on.

ASSEMBLY
Requires: structural support, circulation validity, declared structural/gameplay/sightline purpose, valid entry/exit contract.
Reject if: isolated, inaccessible, unsupported, decorative-only, or missing a purpose.
Rationale: assemblies are playable nouns; every one must do work.

PHRASE
Requires: readable beginning, readable ending, transition between parts, traversal possible under movement rules.
Reject if: same-width compression/reveal, disconnected sequence, invisible destination, impossible traversal, purposeless middle.
Rationale: phrases are architectural sentences; invalid transitions produce nonsense even with valid nouns.

ROOM
Requires: every entrance can reach an exit, combat/traversal/social/logistics purpose, intentional dead ends only.
Reject if: dead-end arena without purpose, unreachable reward, no sightline anchor, no route decision.
Rationale: rooms must be situations, not containers.

DISTRICT
Requires: connected circulation graph, at least one landmark, logistics or civic reason, service access, repeated material/atom grammar.
Reject if: disconnected rooms, landmark spam, no reason for infrastructure, buildings with no support system.
Rationale: districts must explain how spaces relate and why they coexist.

CITY
Requires: connected districts, continuous infrastructure, readable skyline, macro landmarks, district-to-district transitions.
Reject if: isolated districts, broken rail/dock/road continuity, unreadable massing, no hierarchy of destinations.
Rationale: city scale needs organization above room grammar.

WORLD
Requires: valid district graph, macro traversal possible, impossible structures justified by world rules, biome/material constraints honored.
Reject if: traversal chain breaks, floating structures lack setting logic, district functions contradict world premise.
Rationale: world rules decide what architecture can exist at all.

## Vocabulary Normalization

These aliases let domain phrases keep useful language while still resolving to canonical generator parts.

| Alias | Canonical Part | Use |
| --- | --- | --- |
| Viaduct Pier | Bridge Pier | Bridge pier repeated under long rail or road spans. |
| Flying Bridge | Bridge Span | High-clearance bridge span over void, street, cloud, or machine space. |
| Tower Gate | Gatehouse + Tower Base | Defended threshold attached to a vertical landmark. |
| Foundry Plinth | Machinery Plinth | Heavy industrial base for furnace, press, forge, or engine. |
| Warehouse | Warehouse Bay | Logistics storage room with dock/yard/rail adjacency. |
| Furnace | Furnace Hall | Hazard-core industrial room. |
| Plaza | Arena / Plaza | Civic or public version of the large open field assembly. |
| Tunnel | Service Tunnel or Barrel Vault | Choose by scale: utility bypass or major vaulted route. |

## Structural Atoms

====================================

NAME
Wall Bay

PURPOSE
repeated facade unit

BOX BREAKDOWN
2 side posts, 1 lower panel, 1 lintel or cap, optional inset opening

PROPORTIONS
width 1x to 2x height module; post thickness 0.15x to 0.25x bay width

ADJACENCY RULES
Repeat horizontally; terminate runs with Corner Transition or Tower Base.

GENERATOR USE
Prevents blank walls and gives facades rhythm.

====================================

NAME
Corner Transition

PURPOSE
turn or terminate wall systems

BOX BREAKDOWN
1 inside or outside corner mass, 2 receiving wall faces, optional chamfer

PROPORTIONS
corner mass 1.2x to 2x wall thickness

ADJACENCY RULES
Required where Wall Bay, Retaining Wall, Arcade, or parapet runs change direction.

GENERATOR USE
Stops buildings from reading as intersecting random boxes.

====================================

NAME
Buttress

PURPOSE
external wall support and vertical rhythm

BOX BREAKDOWN
1 vertical support mass, 1 foot block, optional sloped shoulder

PROPORTIONS
spacing 1.5x to 3x wall height; projection 0.25x to 0.6x wall height

ADJACENCY RULES
Attach to tall walls, vaults, retaining walls, and tower bases.

GENERATOR USE
Explains height, weight, and long walls.

====================================

NAME
Retaining Wall

PURPOSE
holds terrain or elevated platform

BOX BREAKDOWN
1 long heavy wall, 1 backfill side, 1 exposed face, optional buttresses

PROPORTIONS
height 1x to 5x walkway width; thickness 0.25x to 0.5x height

ADJACENCY RULES
Must terminate at Corner Transition, Stair Run, cliff, or tower mass.

GENERATOR USE
Makes plateaus, terraces, and vertical cities structurally believable.

====================================

NAME
Parapet

PURPOSE
safe or tactical edge cap

BOX BREAKDOWN
1 low wall strip, optional crenels, optional inner walk

PROPORTIONS
height 0.4x to 0.8x player height; thickness 0.2x to 0.5x walkway width

ADJACENCY RULES
Attach to bridges, roofs, batteries, terraces, and overlooks.

GENERATOR USE
Turns exposed edges into usable military or civic edges.

====================================

NAME
Bridge Abutment

PURPOSE
bridge-to-land transfer mass

BOX BREAKDOWN
1 heavy endpoint block, 1 receiving wall/terrain cut, optional stair or gate tie-in

PROPORTIONS
width 1.2x to 2x bridge width; depth 0.8x to 1.5x bridge width

ADJACENCY RULES
Required at both ends of Bridge Span unless the bridge grows from a tower.

GENERATOR USE
Makes bridges look supported and route-connected.

====================================

NAME
Bridge Pier

PURPOSE
vertical support under long spans

BOX BREAKDOWN
1 vertical shaft, 1 cap block, optional base foot

PROPORTIONS
spacing <= 4x bridge width for ordinary spans; taller piers need buttress or cross bracing

ADJACENCY RULES
Use under viaducts, flying bridges, docks, and rail approaches.

GENERATOR USE
Prevents long bridges from floating without explanation.

====================================

NAME
Tower Base

PURPOSE
grounded transition into vertical landmark

BOX BREAKDOWN
1 thick plinth, 1 door or stair tie, 2 to 4 wall faces

PROPORTIONS
base width 1.2x to 2x tower shaft width; height 0.3x to 0.8x shaft height

ADJACENCY RULES
Attach to gatehouses, walls, bridge abutments, or cliff cuts.

GENERATOR USE
Gives towers weight and a reason to meet the ground.

====================================

NAME
Tower Crown

PURPOSE
top termination and readable destination

BOX BREAKDOWN
1 upper platform, 1 parapet or roof cap, optional lookout opening

PROPORTIONS
crown width 1x to 1.4x shaft width; height 0.15x to 0.35x shaft height

ADJACENCY RULES
Required for tower phrases unless the tower terminates into a roof or battery.

GENERATOR USE
Stops towers from being endless columns.

====================================

NAME
Arcade

PURPOSE
repeated arch-edge passage

BOX BREAKDOWN
2+ Arch Spans in series, shared rear wall, optional balcony above

PROPORTIONS
bay spacing 1x to 1.5x opening width; run length 3+ bays

ADJACENCY RULES
Attach to courtyards, stations, terraces, and civic halls.

GENERATOR USE
Creates coherent repeated edge structure.

====================================

NAME
Colonnade

PURPOSE
post-and-beam rhythm

BOX BREAKDOWN
3+ columns or posts, 1 beam line, optional rear wall

PROPORTIONS
pillar spacing 1.5x to 3x pillar height; beam depth 0.15x to 0.25x height

ADJACENCY RULES
Use around plazas, docks, station fronts, and imperial halls.

GENERATOR USE
Creates civic order without requiring solid walls.

====================================

NAME
Terrace

PURPOSE
stepped exterior platform

BOX BREAKDOWN
1 flat platform, 1 retaining edge, 1 stair or ramp connector

PROPORTIONS
depth 1x to 3x adjacent route width; rise 0.5x to 2x route width

ADJACENCY RULES
Stack with Retaining Wall, Stair Run, and Parapet.

GENERATOR USE
Lets terrain become architecture.

====================================

NAME
Cliff Cut

PURPOSE
carved terrain boundary

BOX BREAKDOWN
1 exposed vertical face, 1 floor ledge, optional quarry shelves

PROPORTIONS
face height 2x to 8x route width; ledges every 1x to 3x height for traversal

ADJACENCY RULES
Attach to quarry, tunnel, retaining wall, and overlook phrases.

GENERATOR USE
Gives terrain a constructed readable edge.

====================================

NAME
Quarry Face

PURPOSE
worked cliff with extraction logic

BOX BREAKDOWN
Cliff Cut plus shelves, ramps, lift pocket, processing yard edge

PROPORTIONS
shelf depth 0.5x to 1.5x route width; lift pocket every 2 to 4 shelves

ADJACENCY RULES
Attach to barracks, lift cage, processing yard, rail spur.

GENERATOR USE
Turns raw rock into an economic place.

====================================

NAME
Machinery Plinth

PURPOSE
raised base for heavy machine or furnace

BOX BREAKDOWN
1 slab base, 1 service lip, optional anchor bolts/blocks

PROPORTIONS
base footprint 1.2x to 2x machine footprint; height 0.2x to 0.6x player height

ADJACENCY RULES
Attach to catwalk, service tunnel, foundry, crane base, battery.

GENERATOR USE
Makes industrial props belong to the building.

====================================

NAME
Dock Edge

PURPOSE
hard boundary for loading into void/water/cloud

BOX BREAKDOWN
1 platform edge, 1 fender/bumper strip, optional mooring posts

PROPORTIONS
edge thickness 0.2x to 0.5x platform width; loading bay every 2x to 4x platform width

ADJACENCY RULES
Attach to warehouse, crane base, rail spur, cloud mooring.

GENERATOR USE
Makes logistics space readable.

====================================

NAME
Crane Base

PURPOSE
industrial vertical landmark with working radius

BOX BREAKDOWN
1 machinery plinth, 1 tower post, 1 boom or service arm zone

PROPORTIONS
base width 1x to 2x route width; clear radius 1.5x to 4x base width

ADJACENCY RULES
Attach to dock edge, quarry face, foundry yard, rail station.

GENERATOR USE
Explains large vertical industrial space.

====================================

NAME
Roof Monitor

PURPOSE
raised roof light or vent volume

BOX BREAKDOWN
1 long raised box, 2 side windows/vents, 1 roof seam

PROPORTIONS
width 0.2x to 0.4x roof span; length 0.5x to 0.9x roof length

ADJACENCY RULES
Attach to foundry, station hall, warehouse, workshop.

GENERATOR USE
Terminates large roofs and implies interior function.

====================================

NAME
Battery Emplacement

PURPOSE
artillery-facing platform

BOX BREAKDOWN
1 firing slab, 1 parapet front, 1 rear service route, optional ammo alcove

PROPORTIONS
front arc 60 to 140 degrees; rear route at least 1x route width

ADJACENCY RULES
Attach to fortress plateau, retaining wall, tower crown, cliff cut.

GENERATOR USE
Turns a view direction into military architecture.

## Canonical Assemblies

====================================

NAME
Gatehouse

BOX BREAKDOWN
2 shoulder masses, 1 lintel block, 1 throat cut, 1 rear cap.

PROPORTIONS
opening width 1x; shoulder width 1.5x; depth 1.5x to 2.5x opening width

ADJACENCY RULES
requires Wall Bay or Retaining Wall tie-in on at least one side

CONSTRUCTION ORDER
Set shoulders. Bridge lintel. Cut throat. Cap rear mass.

STRUCTURAL PURPOSE
Threshold that compresses approach and turns entry into commitment.

VALIDATION REQUIRES
wall connection, supported lintel, traversable opening, visible threshold direction.

REJECT IF
floating, opening blocked, isolated from wall/route, lintel unsupported.

====================================

NAME
Arch Span

BOX BREAKDOWN
2 piers, 1 curved or stepped cap, 1 bridge slab.

PROPORTIONS
span width 2x to 4x pier thickness; cap height 1x to 1.5x pier thickness

ADJACENCY RULES
long runs become Arcade; long crossings require Bridge Abutment or Bridge Pier

CONSTRUCTION ORDER
Place piers. Add cap. Cut void under span.

STRUCTURAL PURPOSE
Supported crossing or opening.

VALIDATION REQUIRES
two load-bearing piers or equivalent supports, clear span, valid height clearance.

REJECT IF
unsupported cap, blocked void, decorative arch with no passage/view/support purpose.

====================================

NAME
Barrel Vault

BOX BREAKDOWN
2 end walls, 1 long ceiling shell, 1 floor channel.

PROPORTIONS
length 3x to 5x width; ceiling height 0.5x to 1x width above wall height

ADJACENCY RULES
needs buttress or thick side walls when long/tall

CONSTRUCTION ORDER
Lay floor. Cap sides. Shape roof arc. Tighten ends.

STRUCTURAL PURPOSE
Continuous shell for pressure tunnel or heavy corridor.

VALIDATION REQUIRES
continuous side support, valid ceiling clearance, start/end termination.

REJECT IF
vault floats, side walls absent, corridor has no entry/exit, ceiling intersects route.

====================================

NAME
Cross Vault

BOX BREAKDOWN
4 corner supports, 1 central crossing mass, 4 ribs.

PROPORTIONS
arms equal or near equal; center 1.2x to 1.8x route width

ADJACENCY RULES
connects 3 to 4 routes; must declare primary through-line

CONSTRUCTION ORDER
Set supports. Add ribs. Carve negative spaces.

STRUCTURAL PURPOSE
Route crossing with shared center.

VALIDATION REQUIRES
four supports or equivalent corner masses, connected route arms, declared primary through-line.

REJECT IF
center unsupported, arms dead-end accidentally, crossing has no route decision.

====================================

NAME
Courtyard

BOX BREAKDOWN
4 perimeter edges, 1 open center, 2 to 4 anchors.

PROPORTIONS
negative_space_ratio 0.4 to 0.65; edge depth 0.15x to 0.3x court width

ADJACENCY RULES
edges should be Wall Bay, Arcade, Balcony, or Retaining Wall, not blank boxes

CONSTRUCTION ORDER
Lay perimeter. Cut center. Add edge system. Place anchor routes.

STRUCTURAL PURPOSE
Open room that organizes multiple exits.

VALIDATION REQUIRES
perimeter edge system, open center, at least two connected exits, declared center purpose.

REJECT IF
blank box perimeter, isolated center, exits unreachable, no edge function.

====================================

NAME
Stair Run

BOX BREAKDOWN
1 stair spine, 2 side guards, 1 top landing, 1 bottom landing.

PROPORTIONS
rise 0.5x to 2x run; step pitch constrained by traversal model

ADJACENCY RULES
needs Landing every major direction or height change

CONSTRUCTION ORDER
Place landings. Step core. Flank run.

STRUCTURAL PURPOSE
Readable vertical travel.

VALIDATION REQUIRES
top and bottom landing, traversable pitch, collision clearance, support under run.

REJECT IF
stairs terminate in wall/void, pitch impossible, no landing, decorative-only stair.

====================================

NAME
Landing

BOX BREAKDOWN
1 flat platform, 2 side stops, optional rail/back edge.

PROPORTIONS
depth 1x to 2x route width; width >= connected route width

ADJACENCY RULES
must connect at least two route segments or one route and one overlook

CONSTRUCTION ORDER
Set platform. Add edge controls. Connect exits.

STRUCTURAL PURPOSE
Pause and reorientation point.

VALIDATION REQUIRES
incoming route, outgoing route or overlook contract, stable platform dimensions.

REJECT IF
platform unreachable, no onward purpose, too small for traversal, floating without support.

====================================

NAME
Switchback Stair

BOX BREAKDOWN
2 stair flights, 1 turn platform, 2 side guards.

PROPORTIONS
turn landing 1.2x to 2x stair width

ADJACENCY RULES
use in cliffs, towers, retaining walls, and compact vertical interiors

CONSTRUCTION ORDER
Place lower flight. Add turn. Place upper flight.

STRUCTURAL PURPOSE
Vertical route that hides the next segment until the turn.

VALIDATION REQUIRES
two stair flights, turn landing, valid vertical clearance, connected endpoints.

REJECT IF
turn blocked, one flight missing, no reason to switch back, inaccessible upper/lower endpoint.

====================================

NAME
Balcony

BOX BREAKDOWN
1 thin platform, 1 support edge, 1 front edge.

PROPORTIONS
depth 0.5x to 1.5x route width; height 1x to 3x room height above floor

ADJACENCY RULES
must overlook a lower phrase or room; front edge should be parapet/rail/lip

CONSTRUCTION ORDER
Set support edge. Project slab. Add edge termination.

STRUCTURAL PURPOSE
Elevated route or firing/reading platform.

VALIDATION REQUIRES
access route, lower subject to overlook, edge treatment, structural support.

REJECT IF
decorative-only, inaccessible, overlooks blank wall, unsupported projection.

====================================

NAME
Overlook

BOX BREAKDOWN
1 high perch, 1 lip, 1 back mass, optional undercut.

PROPORTIONS
height delta >= 1 room height; lip visible from below

ADJACENCY RULES
requires route down, route back, or drop contract

CONSTRUCTION ORDER
Raise perch. Carve underside. Terminate edge.

STRUCTURAL PURPOSE
High reading point and destination.

VALIDATION REQUIRES
access or intentional drop route, visible subject, protected/readable edge, return/descent rule.

REJECT IF
view target absent, unreachable, no exit/drop contract, reads as random ledge.

====================================

NAME
Window Bay

BOX BREAKDOWN
2 side blocks, 1 opening, 1 recess or reveal pocket.

PROPORTIONS
opening 0.25x to 0.6x bay width; reveal depth 0.1x to 0.4x wall thickness

ADJACENCY RULES
belongs to Wall Bay, tower, service room, or facade run

CONSTRUCTION ORDER
Lay wall bay. Cut opening. Deepen reveal.

STRUCTURAL PURPOSE
Controlled view and light cut.

VALIDATION REQUIRES
valid wall bay host, opening dimensions, reveal depth, sight/light purpose.

REJECT IF
window floats, opens into solid, no wall host, no view/light/gameplay function.

====================================

NAME
Bridge Span

BOX BREAKDOWN
1 deck slab, 2 abutments, optional piers/parapets.

PROPORTIONS
span <= support_strictness max; longer spans require Bridge Pier rhythm

ADJACENCY RULES
must connect two valid landings, towers, terraces, or abutments

CONSTRUCTION ORDER
Place abutments. Place deck. Add piers/parapets as required.

STRUCTURAL PURPOSE
Exposed commitment crossing.

VALIDATION REQUIRES
two endpoints, abutments or towers, usable width, support explanation by span length.

REJECT IF
ends in air, unsupported span, unusable width, connects nowhere meaningful.

====================================

NAME
Side Passage

BOX BREAKDOWN
1 side opening, 1 secondary route, 1 return wall.

PROPORTIONS
width 0.5x to 0.9x main route; length 1x to 4x main route width

ADJACENCY RULES
must rejoin, hide a cache, or bypass a known obstacle

CONSTRUCTION ORDER
Cut opening. Extend spur. Define payoff.

STRUCTURAL PURPOSE
Optional lateral deviation.

VALIDATION REQUIRES
main route connection, payoff or bypass purpose, rejoin/termination rule.

REJECT IF
spur to nowhere, indistinguishable from main route, no reward/bypass/view purpose.

====================================

NAME
Service Tunnel

BOX BREAKDOWN
2 end caps, 1 narrow channel, optional service pocket.

PROPORTIONS
ceiling 0.6x to 0.9x normal; width 0.5x to 0.8x normal

ADJACENCY RULES
attach to machinery, maintenance, secret, or bypass routes

CONSTRUCTION ORDER
Set caps. Compress channel. Add service pocket if needed.

STRUCTURAL PURPOSE
Utility circulation and concealed bypass.

VALIDATION REQUIRES
utility/logistics reason, connected endpoints, compressed but traversable dimensions.

REJECT IF
dead tunnel without payoff, too small to traverse, no service object/destination.

====================================

NAME
Shaft

BOX BREAKDOWN
2+ vertical walls, 1 void, 1 top/bottom stop.

PROPORTIONS
height >= 3x footprint; route must define lift, stair, ladder, or fall use

ADJACENCY RULES
must terminate into Landing, Lift Cage, or hazard

CONSTRUCTION ORDER
Set walls. Cut void. Add traversal/termination.

STRUCTURAL PURPOSE
Strong vertical connection or risk void.

VALIDATION REQUIRES
top/bottom termination, traversal method or hazard rule, readable vertical void.

REJECT IF
infinite hole, no landing/hazard, unreachable stops, unclear function.

====================================

NAME
Lift Cage

BOX BREAKDOWN
1 moving cage, 2 guide rails, 1 shaft frame.

PROPORTIONS
cage 0.6x to 0.9x shaft width; waiting landings at stops

ADJACENCY RULES
requires shaft and at least two landings

CONSTRUCTION ORDER
Frame shaft. Hang guides. Insert cage. Connect stops.

STRUCTURAL PURPOSE
Mechanical vertical traversal.

VALIDATION REQUIRES
shaft, at least two stops, cage clearance, waiting landings.

REJECT IF
single-stop lift, no shaft frame, cage clips walls, unreachable call/entry area.

====================================

NAME
Choke Point

BOX BREAKDOWN
2 side masses, 1 narrow pass-through, optional blocker.

PROPORTIONS
opening 0.35x to 0.7x adjacent room width

ADJACENCY RULES
must have readable release on at least one side

CONSTRUCTION ORDER
Lay side masses. Cut passage. Add blocker if desired.

STRUCTURAL PURPOSE
Compression and commitment beat.

VALIDATION REQUIRES
measurable narrowing, readable release, traversable opening, pressure reason.

REJECT IF
same width as surroundings, optional when phrase requires commitment, blocked passage.

====================================

NAME
Alcove

BOX BREAKDOWN
1 recess, 1 lip, 1 rear wall, optional side brace.

PROPORTIONS
depth 0.3x to 0.9x route width; width 0.5x to 1.5x route width

ADJACENCY RULES
must hold cover, cache, shrine, machine, shadow, or view

CONSTRUCTION ORDER
Cut recess. Thicken lip. Place purpose.

STRUCTURAL PURPOSE
Purposeful wall pocket.

VALIDATION REQUIRES
host wall, purposeful contents/view/shadow/cover, valid depth.

REJECT IF
random recess, unreachable pocket, no purpose, cuts through structural wall incorrectly.

====================================

NAME
Pit / Drop Well

BOX BREAKDOWN
1 floor void, 1 rim, 1 lower hazard/landing.

PROPORTIONS
void width 0.5x to 0.7x room width unless bridge/catwalk crosses it

ADJACENCY RULES
must define death, safe drop, hidden route, or resource risk

CONSTRUCTION ORDER
Mark rim. Cut void. Define bottom.

STRUCTURAL PURPOSE
Negative space that changes movement value.

VALIDATION REQUIRES
rim, bottom meaning, traversal/hazard rule, readable depth boundary.

REJECT IF
unmarked hole, bottom undefined, unavoidable death without purpose, no route/value relation.

====================================

NAME
Catwalk

BOX BREAKDOWN
1 narrow deck, 2 endpoints, optional rails/braces.

PROPORTIONS
width 0.35x to 0.7x room route width; length 2x to 6x width

ADJACENCY RULES
must cross visible void/machine/fight plane; endpoints need landings

CONSTRUCTION ORDER
Set endpoints. Draw deck. Add edge/support rules.

STRUCTURAL PURPOSE
Exposed narrow route.

VALIDATION REQUIRES
two endpoints, visible void/machine/fight plane below, usable width, edge/support rule.

REJECT IF
catwalk over nothing, ends inaccessible, too narrow, unsupported long span.

====================================

NAME
Hall

BOX BREAKDOWN
2 side walls or edge systems, 1 floor lane, 1 ceiling or open top, optional side bays.

PROPORTIONS
length 2x to 8x route width; ceiling height from mutation profile

ADJACENCY RULES
must terminate into Choke Point, Courtyard, Gatehouse, Stair Run, or service branch

CONSTRUCTION ORDER
Set lane. Define side system. Terminate both ends. Add side bays if needed.

STRUCTURAL PURPOSE
Primary linear room for pacing, approach, and controlled sightline.

VALIDATION REQUIRES
two termini, lane dimensions, side system or edge logic, sightline purpose.

REJECT IF
corridor to nowhere, no termination, blank endless tube, width contradicts mutation profile.

====================================

NAME
Arena / Plaza

BOX BREAKDOWN
1 large floor field, 2+ route edges, optional cover islands, optional landmark edge.

PROPORTIONS
negative_space_ratio 0.45 to 0.75; route_count 2 to 6

ADJACENCY RULES
must have at least one readable entry, one exit, and one edge system such as Arcade, Balcony, Wall Bay, or Retaining Wall

CONSTRUCTION ORDER
Lay field. Define edge system. Place routes. Add cover/landmark according to mutation profile.

STRUCTURAL PURPOSE
Large readable room for combat, civic arrival, or district gathering.

VALIDATION REQUIRES
large field, at least one entry and exit, edge system, landmark/cover/civic purpose.

REJECT IF
empty box, dead-end arena, no edge grammar, no reason to occupy center.

====================================

NAME
Station Platform

BOX BREAKDOWN
1 long platform slab, 1 track or void edge, 1 shelter/roof edge, optional columns or arcade.

PROPORTIONS
length 4x to 12x route width; platform width 1.5x to 3x route width

ADJACENCY RULES
attach to Viaduct Pier, Barrel Vault tunnel, Colonnade, Roof Monitor, or service route

CONSTRUCTION ORDER
Place track/void edge. Lay platform. Add shelter/columns. Connect tunnel and concourse exits.

STRUCTURAL PURPOSE
Infrastructure arrival edge that turns movement systems into architecture.

VALIDATION REQUIRES
track/void edge, platform clearance, arrival/departure routes, shelter or edge termination.

REJECT IF
platform with no rail/vehicle logic, no destination, unsafe edge without rule.

====================================

NAME
Warehouse Bay

BOX BREAKDOWN
1 large storage volume, 1 loading door, 1 roof span, 1 dock or yard edge.

PROPORTIONS
door width 1x to 2x route width; roof span requires support at mutation support_strictness

ADJACENCY RULES
attach to Dock Edge, Crane Base, Service Tunnel, rail spur, or yard

CONSTRUCTION ORDER
Lay storage volume. Cut loading face. Add roof support. Connect dock/service routes.

STRUCTURAL PURPOSE
Logistics room that explains why dock, crane, and service infrastructure exist.

VALIDATION REQUIRES
loading face, storage volume, roof support, dock/yard/rail adjacency.

REJECT IF
warehouse without cargo route, unsupported roof, no loading access, blank storage box.

====================================

NAME
Furnace Hall

BOX BREAKDOWN
1 large hazard core, 1 Machinery Plinth, 1 service perimeter, 1 roof/vent termination.

PROPORTIONS
hazard core 0.25x to 0.5x hall footprint; service perimeter at least 1 route width

ADJACENCY RULES
requires Catwalk, Cooling Hall, Service Tunnel, and Roof Monitor or vent termination

CONSTRUCTION ORDER
Place hazard core. Set plinth. Wrap service route. Add roof/vent termination and exits.

STRUCTURAL PURPOSE
Industrial heat room where machine purpose, danger, and circulation are the same structure.

VALIDATION REQUIRES
hazard core, machinery plinth, service perimeter, exhaust/roof termination, cooling exit.

REJECT IF
furnace with no logistics, no service route, no heat/exhaust path, inaccessible controls.

====================================

NAME
Cooling Hall

BOX BREAKDOWN
1 long exhaust or runoff lane, 1 service walkway, 1 vent/roof termination, optional water/steam channel.

PROPORTIONS
length 2x to 6x route width; channel width 0.3x to 0.6x hall width

ADJACENCY RULES
must connect downstream of Furnace Hall, foundry plinth, or machinery district

CONSTRUCTION ORDER
Lay channel. Add service walkway. Terminate vents. Connect back to district route.

STRUCTURAL PURPOSE
Industrial release room that gives foundry layouts a believable aftermath.

VALIDATION REQUIRES
connection from heat/process source, runoff/exhaust lane, service walkway, district rejoin.

REJECT IF
cooling room not downstream of anything, no exhaust/channel, dead service path.

## Mutation Grammars

Mutation profiles are generator parameters. Human identity prose may be derived from them, but generation must use the measurable fields.

| PROFILE | room_scale | ceiling_height | wall_thickness | span_length | route_count | compression_frequency | negative_space_ratio | verticality | landmark_frequency | cover_density | combat_distance | stealth_affordance | maintenance_visibility | symmetry | support_strictness | terrain_integration |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DOOM | 0.8-1.2 | 0.7-1.1 | 0.4-0.7 | 0.2-0.4 | 2-4 | high | 0.25-0.45 | low | low | 0.55-0.8 | short | low | low | broken axial | medium | flat/platform |
| DOOM II | 1.0-1.8 | 0.8-1.3 | 0.4-0.8 | 0.2-0.5 | 3-6 | high | 0.3-0.55 | medium | medium | 0.65-0.9 | short-medium | low | low | broken/radial | medium | flat/platform |
| QUAKE | 0.9-1.6 | 1.2-2.4 | 0.7-1.2 | 0.8-1.5 | 2-4 | medium | 0.35-0.6 | high | medium | 0.35-0.65 | medium | low | medium | asymmetric carved | high | cliff/void |
| QUAKE II | 1.0-1.7 | 1.0-1.8 | 0.4-0.8 | 1.0-2.0 | 3-6 | medium | 0.35-0.55 | medium | medium-high | 0.45-0.7 | medium-long | low | high | industrial grid | high | machine/platform |
| HALF-LIFE | 0.9-1.4 | 0.8-1.4 | 0.25-0.6 | 0.8-1.5 | 2-5 | medium | 0.3-0.5 | medium | low-medium | 0.35-0.6 | medium | medium | high | practical | high | facility/terrain |
| HALO CE | 1.6-3.0 | 1.2-2.2 | 0.35-0.7 | 1.5-3.5 | 3-7 | low-medium | 0.5-0.75 | medium | medium | 0.35-0.55 | long | low | medium | broad axial | medium | open terrain/platform |
| HALO 2 | 1.4-2.5 | 1.2-2.3 | 0.35-0.75 | 1.2-3.0 | 3-8 | medium | 0.45-0.7 | high | medium-high | 0.45-0.65 | medium-long | low | medium | layered axial | medium | platform/urban |
| MARATHON | 0.7-1.2 | 0.7-1.2 | 0.25-0.5 | 0.6-1.2 | 2-5 | medium | 0.25-0.45 | medium | low | 0.4-0.65 | short-medium | low | high | orthogonal loop | medium | ship/interior |
| THIEF | 0.8-1.4 | 0.9-1.7 | 0.35-0.8 | 0.8-1.8 | 2-5 | medium-low | 0.35-0.6 | high | low-medium | 0.2-0.45 | short-medium | high | medium | irregular civic | medium | urban/roof |
| DISHONORED | 1.0-1.8 | 1.1-2.2 | 0.35-0.7 | 1.0-2.5 | 3-7 | medium | 0.4-0.65 | high | medium-high | 0.25-0.5 | medium-long | high | medium-high | stacked urban | medium | street/roof/canal |
| DARK SOULS | 0.9-2.0 | 1.1-2.5 | 0.7-1.4 | 0.8-2.5 | 2-5 | medium-high | 0.35-0.6 | high | high | 0.25-0.55 | medium-long | low-medium | low-medium | asymmetric landmark | high | cliff/fortress |
| BLOOD | 0.7-1.3 | 0.8-1.6 | 0.5-0.9 | 0.5-1.4 | 2-4 | high | 0.25-0.5 | medium | low-medium | 0.45-0.75 | short | medium | low | ritual broken | medium | interior/crypt |
| DUKE NUKEM 3D | 0.8-1.5 | 0.8-1.5 | 0.25-0.6 | 0.6-1.6 | 2-6 | medium | 0.35-0.55 | medium | medium | 0.35-0.65 | short-medium | low-medium | medium | practical toybox | low-medium | urban/interior |

## Composition Phrases

Phrases are architectural sentences. A phrase is valid only when its required parts exist, its entry and exit connect, and its support rules pass.

====================================

NAME
Compression -> Reveal

REQUIRED PARTS
Choke Point, Gatehouse or Service Tunnel, then Courtyard/Overlook

CIRCULATION CONTRACT
1 narrow entry, 1 readable release space

VALIDATION RULE
entry width <= 0.7x release width

GAMEPLAY EFFECT
Forces a read, then grants a new choice.

COMMON MUTATIONS
Doom, Quake, Half-Life, Dark Souls

REJECT IF
reject if narrowing is not measurable, release is hidden, or reveal space is same scale as entry.

====================================

NAME
Hall -> Choke -> Arena

REQUIRED PARTS
Service Tunnel or Barrel Vault, Choke Point, Courtyard

CIRCULATION CONTRACT
primary entry and 2+ arena exits

VALIDATION RULE
arena negative_space_ratio 0.45-0.7; cover_density from mutation

GAMEPLAY EFFECT
Turns connector into combat commitment.

COMMON MUTATIONS
Doom, Doom II, Halo CE, Blood

REJECT IF
reject if arena is smaller than choke, choke is optional in the required path, or arena has no alternate exit.

====================================

NAME
Courtyard -> Arcade Ring

REQUIRED PARTS
Courtyard, Arcade, Balcony or Parapet edge

CIRCULATION CONTRACT
4 edge routes or 2 route pairs

VALIDATION RULE
arcade bay count >= 3 per active edge

GAMEPLAY EFFECT
Creates readable center plus tactical rim.

COMMON MUTATIONS
Halo, Dishonored, Quake, civic districts

REJECT IF
reject if arcade does not wrap a meaningful edge, ring has no route value, or center is unreadable.

====================================

NAME
Retaining Wall -> Stair -> Terrace

REQUIRED PARTS
Retaining Wall, Stair Run/Switchback, Terrace, Parapet

CIRCULATION CONTRACT
lower approach and upper terrace exit

VALIDATION RULE
terrace rise <= traversal comfort unless switchback exists

GAMEPLAY EFFECT
Turns terrain height into inhabited city structure.

COMMON MUTATIONS
Dark Souls, Dishonored, fortress districts

REJECT IF
reject if terrace lacks retaining structure, stair does not connect levels, or upper platform has no purpose.

====================================

NAME
Bridge Abutment -> Bridge Span -> Tower Gate

REQUIRED PARTS
2 Bridge Abutments, Bridge Span, Tower Base/Gatehouse

CIRCULATION CONTRACT
crossing entry and defended endpoint

VALIDATION RULE
span support required by support_strictness

GAMEPLAY EFFECT
Makes crossing resolve into landmark/defense.

COMMON MUTATIONS
Quake, Halo, Dark Souls

REJECT IF
reject if tower is not visible from bridge, endpoints are unsupported, or crossing has no defended destination.

====================================

NAME
Viaduct Pier -> Station Platform -> Tunnel

REQUIRED PARTS
Bridge Piers, Bridge Span, Platform/Terrace, Barrel Vault tunnel

CIRCULATION CONTRACT
arrival platform and onward tunnel

VALIDATION RULE
pier rhythm consistent; platform width >= 2x route width

GAMEPLAY EFFECT
Builds rail/infrastructure continuity.

COMMON MUTATIONS
Half-Life, Quake II, imperial rail stations

REJECT IF
reject if rail/road path has no destination, pier rhythm does not support span, or platform cannot be reached.

====================================

NAME
Dock Edge -> Crane Base -> Warehouse

REQUIRED PARTS
Dock Edge, Crane Base, Machinery Plinth, Wall Bay/roofed hall

CIRCULATION CONTRACT
loading edge, service route, storage entry

VALIDATION RULE
clear crane radius does not block primary circulation

GAMEPLAY EFFECT
Creates believable logistics space.

COMMON MUTATIONS
Duke Nukem 3D, Half-Life, industrial districts

REJECT IF
reject if dock has nowhere to dock, crane has no cargo zone, or warehouse has no loading path.

====================================

NAME
Quarry Face -> Lift Cage -> Processing Yard

REQUIRED PARTS
Quarry Face, Shaft/Lift Cage, Machinery Plinth, Terrace yard

CIRCULATION CONTRACT
shelf route, lift route, yard exit

VALIDATION RULE
lift connects at least 2 shelves; yard attaches to rail/dock/service

GAMEPLAY EFFECT
Turns carved terrain into production flow.

COMMON MUTATIONS
Quake, Half-Life, Napoleon Floating Kingdom

REJECT IF
reject if quarry shelves do not connect, lift serves no level change, or yard lacks output logistics.

====================================

NAME
Foundry Plinth -> Catwalk -> Furnace -> Cooling Hall

REQUIRED PARTS
Machinery Plinth, Catwalk, large hazard void, Roof Monitor hall

CIRCULATION CONTRACT
service entry, catwalk crossing, cooling exit

VALIDATION RULE
catwalk crosses hazard; service tunnel bypass allowed

GAMEPLAY EFFECT
Makes industrial scale legible and playable.

COMMON MUTATIONS
Quake II, Half-Life, Blood

REJECT IF
reject if foundry has no fuel/material/logistics route, catwalk does not service machinery, or cooling hall is not downstream.

====================================

NAME
Tower Base -> Shaft -> Tower Crown

REQUIRED PARTS
Tower Base, Shaft or Stair Run, Overlook, Tower Crown

CIRCULATION CONTRACT
ground entry and crown exit/view

VALIDATION RULE
base width >= 1.2x shaft; crown terminates tower

GAMEPLAY EFFECT
Makes vertical landmarks structurally complete.

COMMON MUTATIONS
Dark Souls, Quake, Dishonored

REJECT IF
reject if tower has no base, no termination, no circulation, or reads as an infinite column.

====================================

NAME
Parapet -> Battery Emplacement -> Rear Service Tunnel

REQUIRED PARTS
Parapet, Battery Emplacement, Alcove, Service Tunnel

CIRCULATION CONTRACT
front sight cone and rear logistics route

VALIDATION RULE
front arc unobstructed; rear route hidden/protected

GAMEPLAY EFFECT
Turns view direction into military function.

COMMON MUTATIONS
Doom, Blood, fortress plateaus

REJECT IF
reject if artillery has no firing arc, rear service is absent, or parapet blocks intended sightline.

====================================

NAME
Wall Bay -> Corner Transition -> Gatehouse

REQUIRED PARTS
Wall Bay run, Corner Transition, Gatehouse

CIRCULATION CONTRACT
wall approach and threshold exit

VALIDATION RULE
bay rhythm terminates cleanly at corner or shoulder

GAMEPLAY EFFECT
Prevents facade repetition from collapsing at entrances.

COMMON MUTATIONS
Duke Nukem 3D, Half-Life, Dark Souls

REJECT IF
reject if wall rhythm breaks without termination, corner intersects route, or gatehouse is isolated.

====================================

NAME
Cliff Cut -> Side Passage -> Overlook

REQUIRED PARTS
Cliff Cut, Side Passage, Overlook

CIRCULATION CONTRACT
main route and hidden/upper read point

VALIDATION RULE
side passage rejoins or overlooks known space

GAMEPLAY EFFECT
Turns terrain edge into exploration payoff.

COMMON MUTATIONS
Thief, Quake, Dark Souls

REJECT IF
reject if side passage does not rejoin or overlook something, cliff has no readable ledge, or overlook target is blank.

====================================

NAME
Colonnade -> Plaza -> Civic Stair

REQUIRED PARTS
Colonnade, Courtyard/plaza, Stair Run/Terrace

CIRCULATION CONTRACT
public edge and raised destination

VALIDATION RULE
pillar spacing consistent; stair aligns to landmark

GAMEPLAY EFFECT
Builds civic scale from repeated primitives.

COMMON MUTATIONS
Halo, Dishonored, imperial districts

REJECT IF
reject if columns do not align to plaza edge, stair lacks civic destination, or plaza has no public route logic.

====================================

NAME
Bridge Pier -> Flying Bridge -> Upper Gatehouse

REQUIRED PARTS
Bridge Piers, long Bridge Span, Gatehouse/Tower Base

CIRCULATION CONTRACT
lower visible supports, upper crossing, defended exit

VALIDATION RULE
pier rhythm visible from below; abutments terminate span

GAMEPLAY EFFECT
Makes suspended routes believable.

COMMON MUTATIONS
Quake, Halo 2, Napoleon Floating Kingdom

REJECT IF
reject if piers are not visible/supporting, span has no upper destination, or gatehouse cannot be entered.

## Generator Failure Checks

SUPPORT VALIDITY
No bridge span, vault, tower, retaining wall, or high balcony may exist without required supports or termination atoms.

ROUTE REACHABILITY
Every room and phrase must have a connected entry and exit. Optional routes must either rejoin, terminate with purpose, or expose a landmark.

PURPOSE VALIDITY
Every room declares structural purpose, gameplay purpose, and sightline purpose.

REPETITION LIMITS
Repeated atoms such as Wall Bay, Arcade, Colonnade, and Bridge Pier need rhythm breaks at corners, gates, towers, or landmarks.

TERMINATION VALIDITY
Walls, roofs, towers, bridges, cliffs, docks, and terraces need explicit end conditions.

NEGATIVE-SPACE VALIDITY
Pits, courtyards, shafts, docks, and voids must have readable rims and traversal/hazard meaning.

DISTRICT COHERENCE
A district must have a dominant function, a landmark, a service route, and at least one phrase that explains its economy or defense.

FAKE-BUILDING REJECTION
A building with blank box walls, no wall bays/corners/roof termination, and no support logic fails.

RANDOM-BOX REJECTION
A cluster of primitives without phrase membership or room purpose fails.

IMPOSSIBLE-CIRCULATION REJECTION
Routes that cannot be traversed under the target game movement profile fail.


## Generator Metrics

Metrics must be computed from generated geometry and graph data, not judged from prose.

| Metric | Computation Signal | Fails When |
| --- | --- | --- |
| support_score | supported load-bearing elements / required support points | span, tower, balcony, vault, or retaining wall lacks support |
| circulation_score | reachable required exits / declared exits | required route is unreachable or loops into accidental dead end |
| landmark_score | visible landmark anchors / required district anchors | district has no readable destination or too many equal landmarks |
| silhouette_score | meaningful height/edge/termination changes per district frontage | skyline is flat noise or random spikes with no crown/base logic |
| structural_confidence | weighted pass rate of support, attachment, termination, and proportion checks | structure is mostly decorative or physically unexplained |
| readability_score | visible entry, exit, destination, and hazard cues / required cues | player cannot read where to go or what the room does |
| logistics_score | service routes, cargo paths, process chain links / declared industrial or civic needs | dock, crane, foundry, station, or quarry has no reason to function |
| route_complexity | route_count plus loopbacks plus vertical transitions, normalized by mutation profile | route graph is too simple, too tangled, or contradicts profile |
| verticality | traversable height delta and vertical route count / district footprint | vertical promise is decorative or traversal is impossible |
| negative_space_ratio | void/open traversable area / total room or district footprint | room is too solid to read or too empty to have structure |
| purpose_coverage | objects with structural/gameplay/sightline purpose / total generated objects | boxes exist without declared role |
| termination_score | terminated runs / wall, bridge, roof, parapet, and terrace runs | endless walls, unended bridges, flat roofs, or naked edges appear |

Rationale: these metrics let the generator reject nonsense before art polish. They also create a tuning surface for mutation profiles: Quake can demand higher support_score and verticality, while Half-Life can demand higher logistics_score and maintenance_visibility.


## Imperial Floating Strata Validation

Napoleon's Floating Kingdom must answer three questions for every district: why was it built, why is it still standing, and why is the player here?

REQUIRE
- circulation: every plateau, dock, station, foundry, quarry, and battery connects to the district graph.
- logistics: industrial and military spaces have cargo, service, fuel, ammo, or maintenance paths.
- support: floating or elevated structures declare retaining walls, piers, abutments, tower bases, suspension logic, or world-rule exceptions.
- skyline: each district has a readable crown, battery, tower, crane, viaduct, or roof monitor profile.
- purpose: every major structure declares civic, military, industrial, traversal, or encounter role.

REJECT
- bridge with no military, civic, logistics, or traversal reason.
- plateau with no retaining structure or explicit floating-world support rule.
- foundry with no input logistics, service route, exhaust/cooling path, or output yard.
- dock with nowhere to dock, no loading edge, no cargo route, or no crane/warehouse relation.
- artillery battery with no firing arc, blocked sightline, missing parapet, or missing rear service route.
- rail without destination, platform, tunnel, viaduct rhythm, or cargo/passenger reason.
- crane without cargo zone, working radius, machinery plinth, or dock/quarry/foundry adjacency.
- retaining-wall city with disconnected terraces, no stair cascade, no wall-bay rhythm, or no landmark hierarchy.

RATIONALE
Imperial floating architecture fails fastest when spectacle replaces process. The validation rule is simple: if a structure floats, fires, loads, smelts, extracts, defends, or transports, its support and logistics must be visible in the generated grammar.

## Napoleon Test

Napoleon's Floating Kingdom is the stress test for whether this corpus can build districts, not just rooms.

| Target | Required Capability | Buildable With |
| --- | --- | --- |
| fortress plateaus | Retaining Wall, Parapet, Battery Emplacement, Tower Base, Terrace | Retaining Wall -> Stair -> Terrace; Parapet -> Battery Emplacement -> Rear Service Tunnel |
| artillery batteries | Battery Emplacement, Parapet, Alcove, Service Tunnel | Parapet -> Battery Emplacement -> Rear Service Tunnel |
| quarry barracks | Quarry Face, Terrace, Wall Bay, Service Tunnel, Lift Cage | Quarry Face -> Lift Cage -> Processing Yard |
| suspended viaducts | Bridge Pier, Bridge Abutment, Bridge Span, Parapet | Bridge Pier -> Flying Bridge -> Upper Gatehouse |
| imperial rail stations | Colonnade, Arcade, Roof Monitor, Terrace, Barrel Vault | Viaduct Pier -> Station Platform -> Tunnel |
| cloud docks | Dock Edge, Crane Base, Warehouse/Wall Bay, Parapet | Dock Edge -> Crane Base -> Warehouse |
| foundries | Machinery Plinth, Catwalk, Roof Monitor, Service Tunnel | Foundry Plinth -> Catwalk -> Furnace -> Cooling Hall |
| retaining-wall cities | Retaining Wall, Terrace, Stair Run, Wall Bay, Corner Transition | Retaining Wall -> Stair -> Terrace; Wall Bay -> Corner Transition -> Gatehouse |

## Migration Note

Version 0.2 introduced the canonical/mutation/phrase split. Version 0.3 made that split operational by adding hierarchy, structural atoms, measurable mutation parameters, phrase validation, and district-scale infrastructure grammar. Version 0.4 adds validation contracts, assembly invariants, phrase rejection rules, generator metrics, and Imperial Floating Strata validation so generators can reject nonsense before art polish.

If a future generator needs prose cards, generate them from these contracts rather than copying hand-authored variants forward.
