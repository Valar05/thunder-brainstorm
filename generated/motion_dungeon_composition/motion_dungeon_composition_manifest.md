# Motion Dungeon Composition Compiler

- Source repo: Valar05/motion-dungeon
- Created: 2026-09-03T12:05:47+00:00Z
- Source-first: True
- Binary boundary: binary artifacts are only produced on export
- Primary output: mp4 (H.264 MP4)

## Source Inputs

- generated/repo_mining/motion-dungeon/repo_surface.json
- generated/repo_mining/motion-dungeon/mechanic_source_refs.jsonl
- generated/critical_thunder_manifest/critical_thunder_manifest.json
- generated/repo_mining/Valar05_overnight_summary.json

## Composition Units

| Path | Role | Score | Mechanics |
| --- | --- | --- | --- |
| app/page.tsx | composition_core | 216 | ai_pressure, asset_import_pipeline, deck_pressure, delayed_consequences, pose_animation_tools, text_console_runtime, touch_lane_combat, tts_audio_pipeline, validation_pipeline, vehicle_survival, web_choice_player, writing_corpus_review |
| app/layout.tsx | supporting_surface | 200 | ai_pressure, asset_import_pipeline, text_console_runtime, web_choice_player |
| app/scenes/lexen-cage-with-glass-walls/page.tsx | source_locked_scene | 160 | asset_import_pipeline |
| app/ferravine/ferravine-lab.tsx | supporting_surface | 152 | ai_pressure, asset_import_pipeline, pose_animation_tools, source_packet_generation, text_console_runtime, tts_audio_pipeline, validation_pipeline, vehicle_survival, web_choice_player |
| app/scenes/lexen-cage-with-glass-walls/source-locked-scene.tsx | source_locked_scene | 152 | ai_pressure, asset_import_pipeline, resource_upgrade_loop, text_console_runtime, touch_lane_combat, tts_audio_pipeline, validation_pipeline, web_choice_player |
| app/sherman/sherman-lab.tsx | supporting_surface | 152 | ai_pressure, asset_import_pipeline, deck_pressure, delayed_consequences, pose_animation_tools, resource_upgrade_loop, source_packet_generation, text_console_runtime, touch_lane_combat, vehicle_survival, web_choice_player |
| app/venice/venice-room.tsx | supporting_surface | 152 | ai_pressure, asset_import_pipeline, pose_animation_tools, text_console_runtime, tts_audio_pipeline, vehicle_survival, web_choice_player, writing_corpus_review |
| app/scenes/lexen-cage-with-glass-walls/lexen-scene.css | source_locked_scene | 148 | none |
| app/api/venice/voice/route.ts | service_lane | 122 | ai_pressure, asset_import_pipeline, web_choice_player |
| README.md | source_contract | 112 | ai_pressure, asset_import_pipeline, pose_animation_tools, resource_upgrade_loop, tts_audio_pipeline, web_choice_player, writing_corpus_review |
| app/api/venice/route.ts | service_lane | 110 | ai_pressure, asset_import_pipeline, pose_animation_tools, web_choice_player |
| state.md | composition_bible | 106 | ai_pressure, asset_import_pipeline, delayed_consequences, event_clouds, pose_animation_tools, resource_upgrade_loop, text_console_runtime, touch_lane_combat, tts_audio_pipeline, validation_pipeline, vehicle_survival, web_choice_player, writing_corpus_review |

## Performance Keys

### time (timeline)
- [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L297] const renderAtRef = useRef<(time: number) => void>(() => {});
- [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L667] const renderAt = (rawTime: number) => {
- [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L769] renderAtRef.current = renderAt;

### preset (composition selection)
- [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L8] const BEARD_SLAP_VOICE_PATH = "/specimens/randi-adam-beard-slap/randi-adam-beard-slap-gemini-v1.wav";
- [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L12] const COURTSHIP_LINE = "She said yes. Adam will ask instead of narrating. One step at a time. Complete readback.";
- [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L20] beardslap: {name: "Randi vs Adam", note: "read / load / slap / return", color: "#ff3f75", accent: "#ffd66b", duration: BEARD_SLAP_DURATION},

### rendererMode (render backend)
- [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L317] const [rendererMode, setRendererMode] = useState<"loading" | "webgl" | "fallback">("loading");
- [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L410] if (!probe.getContext("webgl2") && !probe.getContext("webgl")) {
- [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L411] setRendererMode("fallback");

### exporting (export gate)
- [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L909] setExporting(true);exportingRef.current=true;setPlaying(false);stopFoley();stopVoice();setProgress(0);setStatus("Rendering on this device…");
- [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L922] muxer.finalize();const blob=new Blob([target.buffer],{type:"video/mp4"});const url=URL.createObjectURL(blob);const link=document.createElement("a");link.href=url;link.download=`...
- [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L923] }catch(error){setStatus(error instanceof Error?error.message:"MP4 export failed");}finally{outputSizeRef.current();setExporting(false);exportingRef.current=false;seek(0);}

### outputSizeRef (capture sizing)
- [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L418] renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.75));
- [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L419] renderer.setSize(mount.clientWidth, mount.clientHeight, false);
- [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L778] const resize = () => { if (!mount.clientWidth || !mount.clientHeight) return; renderer.setPixelRatio(Math.min(window.devicePixelRatio,1.75)); renderer.setSize(mount.clientWidth,...

### voice (audio lane)
- [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L8] const BEARD_SLAP_VOICE_PATH = "/specimens/randi-adam-beard-slap/randi-adam-beard-slap-gemini-v1.wav";
- [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L237] async function renderAdamAudio(duration: number) {
- [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L245] async function renderCourtshipAudio(duration: number) {

### foley (audio lane)
- [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L260] async function renderBeardSlapAudio(duration: number, includeFoley: boolean, includeVoice: boolean) {
- [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L272] const foleyBus = context.createGain();
- [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L273] foleyBus.gain.value = .72;

### sourceName (performance provenance)
- [https://github.com/Valar05/motion-dungeon/blob/main/app/scenes/lexen-cage-with-glass-walls/page.tsx#L3] import SourceLockedScene from "./source-locked-scene";
- [https://github.com/Valar05/motion-dungeon/blob/main/app/scenes/lexen-cage-with-glass-walls/page.tsx#L8] description: "A source-locked Motion Dungeon carrier for Lexen Vigil’s accepted take 8 performance.",
- [https://github.com/Valar05/motion-dungeon/blob/main/app/scenes/lexen-cage-with-glass-walls/source-locked-scene.tsx#L1] "use client";

## Portable Patterns

### Audio tracks as composition lanes
- Problem: Treat voice and foley as first-class compositional tracks, not post-process noise.
- Supporting breadth: 80
- Supporting records: 88553
- Mechanics: tts_audio_pipeline, ai_pressure, web_choice_player
- Engine notes:
  - threejs: Keep the source manifest textual; render the preview with a scene graph and export MP4 only at the end.
  - godot: Map the manifest to scenes/resources; keep source as text and let export generate the binary build later.
  - unity: Translate the same manifest to data assets and timeline-like transport; compile only during export.
  - unreal: Treat the manifest as Sequencer/DataAsset input; package binaries only when exporting.
- Evidence:
  - [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L8] const BEARD_SLAP_VOICE_PATH = "/specimens/randi-adam-beard-slap/randi-adam-beard-slap-gemini-v1.wav";
  - [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L237] async function renderAdamAudio(duration: number) {
  - [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L245] async function renderCourtshipAudio(duration: number) {

### Browser preview, heavy MP4 export
- Problem: Let preview stay light while the exported movie carries the heavy output.
- Supporting breadth: 80
- Supporting records: 77647
- Mechanics: web_choice_player, tts_audio_pipeline, asset_import_pipeline
- Engine notes:
  - threejs: Keep the source manifest textual; render the preview with a scene graph and export MP4 only at the end.
  - godot: Map the manifest to scenes/resources; keep source as text and let export generate the binary build later.
  - unity: Translate the same manifest to data assets and timeline-like transport; compile only during export.
  - unreal: Treat the manifest as Sequencer/DataAsset input; package binaries only when exporting.
- Evidence:
  - [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L909] setExporting(true);exportingRef.current=true;setPlaying(false);stopFoley();stopVoice();setProgress(0);setStatus("Rendering on this device…");
  - [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L916] for(let frame=0;frame<duration*FPS;frame++){const frameTime=frame/FPS;renderAtRef.current(frameTime);const videoFrame=new VideoFrame(canvas,{timestamp:Math.round(frameTime*1_000...
  - [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L922] muxer.finalize();const blob=new Blob([target.buffer],{type:"video/mp4"});const url=URL.createObjectURL(blob);const link=document.createElement("a");link.href=url;link.download=`...

### Source-locked composition canon
- Problem: Keep the editable composition authoritative while binaries stay downstream.
- Supporting breadth: 80
- Supporting records: 60654
- Mechanics: asset_import_pipeline, validation_pipeline, web_choice_player
- Engine notes:
  - threejs: Keep the source manifest textual; render the preview with a scene graph and export MP4 only at the end.
  - godot: Map the manifest to scenes/resources; keep source as text and let export generate the binary build later.
  - unity: Translate the same manifest to data assets and timeline-like transport; compile only during export.
  - unreal: Treat the manifest as Sequencer/DataAsset input; package binaries only when exporting.
- Evidence:
  - [https://github.com/Valar05/motion-dungeon/blob/main/app/scenes/lexen-cage-with-glass-walls/page.tsx#L3] import SourceLockedScene from "./source-locked-scene";
  - [https://github.com/Valar05/motion-dungeon/blob/main/app/scenes/lexen-cage-with-glass-walls/page.tsx#L8] description: "A source-locked Motion Dungeon carrier for Lexen Vigil’s accepted take 8 performance.",
  - [https://github.com/Valar05/motion-dungeon/blob/main/app/scenes/lexen-cage-with-glass-walls/source-locked-scene.tsx#L1] "use client";

### Key-driven timeline transport
- Problem: Keep motion composition deterministic and scrub-friendly from source keys.
- Supporting breadth: 80
- Supporting records: 29436
- Mechanics: web_choice_player, text_console_runtime, delayed_consequences
- Engine notes:
  - threejs: Keep the source manifest textual; render the preview with a scene graph and export MP4 only at the end.
  - godot: Map the manifest to scenes/resources; keep source as text and let export generate the binary build later.
  - unity: Translate the same manifest to data assets and timeline-like transport; compile only during export.
  - unreal: Treat the manifest as Sequencer/DataAsset input; package binaries only when exporting.
- Evidence:
  - [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L297] const renderAtRef = useRef<(time: number) => void>(() => {});
  - [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L317] const [rendererMode, setRendererMode] = useState<"loading" | "webgl" | "fallback">("loading");
  - [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L411] setRendererMode("fallback");

### Child manifest composition chain
- Problem: Let scenes and performance records inherit the engine without losing their own source names.
- Supporting breadth: 79
- Supporting records: 55645
- Mechanics: asset_import_pipeline, source_packet_generation, validation_pipeline
- Engine notes:
  - threejs: Keep the source manifest textual; render the preview with a scene graph and export MP4 only at the end.
  - godot: Map the manifest to scenes/resources; keep source as text and let export generate the binary build later.
  - unity: Translate the same manifest to data assets and timeline-like transport; compile only during export.
  - unreal: Treat the manifest as Sequencer/DataAsset input; package binaries only when exporting.
- Evidence:
  - [https://github.com/Valar05/motion-dungeon/blob/main/app/scenes/lexen-cage-with-glass-walls/page.tsx#L8] description: "A source-locked Motion Dungeon carrier for Lexen Vigil’s accepted take 8 performance.",
  - [https://github.com/Valar05/motion-dungeon/blob/main/app/scenes/lexen-cage-with-glass-walls/source-locked-scene.tsx#L51] const performance = object(document.performance);
  - [https://github.com/Valar05/motion-dungeon/blob/main/app/scenes/lexen-cage-with-glass-walls/source-locked-scene.tsx#L144] <p className="lexen-kicker">SOURCE-LOCKED SCENE DOCUMENT 01</p>

## Engine Matrix

| Engine | Source adapter | Binary on export | Export lane |
| --- | --- | --- | --- |
| threejs | scene graph + browser composition | True | MP4 via browser media capture or WebCodecs |
| godot | scene tree + resource manifests | True | project export only |
| unity | data assets + timeline transport | True | package only on export |
| unreal | sequencer + data assets | True | packaged build only |

## Export Profile

- Primary output: mp4
- Format: H.264 MP4
- Role: heavy output archive
- Source truth: Motion Dungeon composition keys and source-locked manifests
- Binary policy: binaries are export artifacts, not source

## Retry Queue

- Hard-Surface-Factory:  Command '['/data/data/com.termux/files/usr/bin/python', '/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/thunder_brainstorm.py', 'mine-gh-repo', '--owner', 'Valar05', '--repo', 'Hard-Surface-Factory', '--ref', 'HEAD', '--out-dir', 'generated/repo_mining', '--max-files', '24', '--quiet']' returned non-zero exit status 1.
- ruined_air:  Command '['/data/data/com.termux/files/usr/bin/python', '/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/thunder_brainstorm.py', 'mine-gh-repo', '--owner', 'Valar05', '--repo', 'ruined_air', '--ref', 'HEAD', '--out-dir', 'generated/repo_mining', '--max-files', '24', '--quiet']' returned non-zero exit status 1.
- Fleshpunk-Crusade:  Command '['/data/data/com.termux/files/usr/bin/python', '/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/thunder_brainstorm.py', 'mine-gh-repo', '--owner', 'Valar05', '--repo', 'Fleshpunk-Crusade', '--ref', 'HEAD', '--out-dir', 'generated/repo_mining', '--max-files', '24', '--quiet']' returned non-zero exit status 1.
- mealPlanner:  Command '['/data/data/com.termux/files/usr/bin/python', '/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/thunder_brainstorm.py', 'mine-gh-repo', '--owner', 'Valar05', '--repo', 'mealPlanner', '--ref', 'HEAD', '--out-dir', 'generated/repo_mining', '--max-files', '24', '--quiet']' returned non-zero exit status 1.
