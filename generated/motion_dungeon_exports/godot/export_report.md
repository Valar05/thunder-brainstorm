# Motion Dungeon godot Export Target

- Export target: motion-dungeon:godot
- Source manifest: generated/motion_dungeon_composition/motion_dungeon_composition_manifest.json
- Source fingerprint: bdad9a765d48094da2d51b8ed5e2b2d6bb3a94a4bfb255a0a7327ba010dc7590
- Input hash: bdad9a765d48094da2d51b8ed5e2b2d6bb3a94a4bfb255a0a7327ba010dc7590
- Target fingerprint: 6018e1ebe6ab3cf1c722eb59e898cc86e716e3f5ab42e7e07146cf241c57c69a
- Source adapter: scene tree + resource manifests
- Export lane: project export only
- Binary on export: True

## Artifact Map

- export_report: export_report.md
- export_spec: export_spec.json
- export_stamp: export_stamp.json
- matrix: ../export_matrix.json

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

## Performance Axes

### exporting (export gate)
- [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L909] setExporting(true);exportingRef.current=true;setPlaying(false);stopFoley();stopVoice();setProgress(0);setStatus("Rendering on this device…");

### foley (audio lane)
- [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L260] async function renderBeardSlapAudio(duration: number, includeFoley: boolean, includeVoice: boolean) {

### outputSizeRef (capture sizing)
- [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L418] renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.75));

### preset (composition selection)
- [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L8] const BEARD_SLAP_VOICE_PATH = "/specimens/randi-adam-beard-slap/randi-adam-beard-slap-gemini-v1.wav";

### rendererMode (render backend)
- [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L317] const [rendererMode, setRendererMode] = useState<"loading" | "webgl" | "fallback">("loading");

### sourceName (performance provenance)
- [https://github.com/Valar05/motion-dungeon/blob/main/app/scenes/lexen-cage-with-glass-walls/page.tsx#L3] import SourceLockedScene from "./source-locked-scene";

### time (timeline)
- [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L297] const renderAtRef = useRef<(time: number) => void>(() => {});

### voice (audio lane)
- [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L8] const BEARD_SLAP_VOICE_PATH = "/specimens/randi-adam-beard-slap/randi-adam-beard-slap-gemini-v1.wav";

## Portable Patterns

### Audio tracks as composition lanes
- Problem: Treat voice and foley as first-class compositional tracks, not post-process noise.
- Mechanics: tts_audio_pipeline, ai_pressure, web_choice_player
- Supporting breadth: 80
- Supporting records: 88553
- Engine note: Map the manifest to scenes/resources; keep source as text and let export generate the binary build later.
- Evidence:
  - [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L8] const BEARD_SLAP_VOICE_PATH = "/specimens/randi-adam-beard-slap/randi-adam-beard-slap-gemini-v1.wav";
  - [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L237] async function renderAdamAudio(duration: number) {

### Browser preview, heavy MP4 export
- Problem: Let preview stay light while the exported movie carries the heavy output.
- Mechanics: web_choice_player, tts_audio_pipeline, asset_import_pipeline
- Supporting breadth: 80
- Supporting records: 77647
- Engine note: Map the manifest to scenes/resources; keep source as text and let export generate the binary build later.
- Evidence:
  - [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L909] setExporting(true);exportingRef.current=true;setPlaying(false);stopFoley();stopVoice();setProgress(0);setStatus("Rendering on this device…");
  - [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L916] for(let frame=0;frame<duration*FPS;frame++){const frameTime=frame/FPS;renderAtRef.current(frameTime);const videoFrame=new VideoFrame(canvas,{timestamp:Math.round(frameTime*1_000...

### Source-locked composition canon
- Problem: Keep the editable composition authoritative while binaries stay downstream.
- Mechanics: asset_import_pipeline, validation_pipeline, web_choice_player
- Supporting breadth: 80
- Supporting records: 60654
- Engine note: Map the manifest to scenes/resources; keep source as text and let export generate the binary build later.
- Evidence:
  - [https://github.com/Valar05/motion-dungeon/blob/main/app/scenes/lexen-cage-with-glass-walls/page.tsx#L3] import SourceLockedScene from "./source-locked-scene";
  - [https://github.com/Valar05/motion-dungeon/blob/main/app/scenes/lexen-cage-with-glass-walls/page.tsx#L8] description: "A source-locked Motion Dungeon carrier for Lexen Vigil’s accepted take 8 performance.",

### Key-driven timeline transport
- Problem: Keep motion composition deterministic and scrub-friendly from source keys.
- Mechanics: web_choice_player, text_console_runtime, delayed_consequences
- Supporting breadth: 80
- Supporting records: 29436
- Engine note: Map the manifest to scenes/resources; keep source as text and let export generate the binary build later.
- Evidence:
  - [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L297] const renderAtRef = useRef<(time: number) => void>(() => {});
  - [https://github.com/Valar05/motion-dungeon/blob/main/app/page.tsx#L317] const [rendererMode, setRendererMode] = useState<"loading" | "webgl" | "fallback">("loading");

### Child manifest composition chain
- Problem: Let scenes and performance records inherit the engine without losing their own source names.
- Mechanics: asset_import_pipeline, source_packet_generation, validation_pipeline
- Supporting breadth: 79
- Supporting records: 55645
- Engine note: Map the manifest to scenes/resources; keep source as text and let export generate the binary build later.
- Evidence:
  - [https://github.com/Valar05/motion-dungeon/blob/main/app/scenes/lexen-cage-with-glass-walls/page.tsx#L8] description: "A source-locked Motion Dungeon carrier for Lexen Vigil’s accepted take 8 performance.",
  - [https://github.com/Valar05/motion-dungeon/blob/main/app/scenes/lexen-cage-with-glass-walls/source-locked-scene.tsx#L51] const performance = object(document.performance);

## Retry Queue

- Hard-Surface-Factory:  Command '['/data/data/com.termux/files/usr/bin/python', '/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/thunder_brainstorm.py', 'mine-gh-repo', '--owner', 'Valar05', '--repo', 'Hard-Surface-Factory', '--ref', 'HEAD', '--out-dir', 'generated/repo_mining', '--max-files', '24', '--quiet']' returned non-zero exit status 1.
- ruined_air:  Command '['/data/data/com.termux/files/usr/bin/python', '/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/thunder_brainstorm.py', 'mine-gh-repo', '--owner', 'Valar05', '--repo', 'ruined_air', '--ref', 'HEAD', '--out-dir', 'generated/repo_mining', '--max-files', '24', '--quiet']' returned non-zero exit status 1.
- Fleshpunk-Crusade:  Command '['/data/data/com.termux/files/usr/bin/python', '/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/thunder_brainstorm.py', 'mine-gh-repo', '--owner', 'Valar05', '--repo', 'Fleshpunk-Crusade', '--ref', 'HEAD', '--out-dir', 'generated/repo_mining', '--max-files', '24', '--quiet']' returned non-zero exit status 1.
- mealPlanner:  Command '['/data/data/com.termux/files/usr/bin/python', '/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/thunder_brainstorm.py', 'mine-gh-repo', '--owner', 'Valar05', '--repo', 'mealPlanner', '--ref', 'HEAD', '--out-dir', 'generated/repo_mining', '--max-files', '24', '--quiet']' returned non-zero exit status 1.
