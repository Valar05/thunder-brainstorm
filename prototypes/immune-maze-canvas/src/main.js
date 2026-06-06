const canvas = document.getElementById('game');
const ctx = canvas.getContext('2d');
const antibodyCount = document.getElementById('antibodyCount');
const complementState = document.getElementById('complementState');
const zoneState = document.getElementById('zoneState');
const feverValue = document.getElementById('feverValue');
const feverFill = document.getElementById('feverFill');
const runState = document.getElementById('runState');
const restartButton = document.getElementById('restart');
const pauseToggle = document.getElementById('pauseToggle');
const musicToggle = document.getElementById('musicToggle');
const fullscreenToggle = document.getElementById('fullscreenToggle');
const menuToggle = document.getElementById('menuToggle');
const mobileFullscreenToggle = document.getElementById('mobileFullscreenToggle');
const mobilePauseToggle = document.getElementById('mobilePauseToggle');
const mobileMusicToggle = document.getElementById('mobileMusicToggle');
const mobileMenuToggle = document.getElementById('mobileMenuToggle');
const debugToggle = document.getElementById('debugToggle');
const appShell = document.querySelector('.app-shell');
const gameSurface = document.querySelector('.game-surface');
const touchJoystick = document.getElementById('touchJoystick');

const APP_VERSION = 'v0.9.0-rc3';
const TILE = 32;
const PLAYER_SHEET = 'assets/player/phagocyte_4frame_sprite_sheet.png';
const TILE_SHEET = 'assets/tiles/immune_tile_sheet.png';
const TISSUE_TEXTURE = 'assets/backgrounds/flesh_tissue_texture.png';
const ROGUELIKE_BACKGROUND = 'assets/backgrounds/roguelike_tissue_menu_bg.png';
const ENEMY_SHEET = 'assets/enemies/infection_archetype_sheet_chromakey.png';
const MUSIC_TRACKS = [
  'assets/Lumen_Organism.mp3',
  'assets/Lumen_Organism(1).mp3',
  'assets/Organism.mp3',
  'assets/Organism(1).mp3',
  'assets/The_Breathing_Megastructure.mp3',
  'assets/The_Breathing_Megastructure(2).mp3',
  'assets/The_Great_Ventricle.mp3',
  'assets/Vast_Organism.mp3'
];
const MUSIC_VOLUME = 0.58;
const SFX = {
  uiSelect: 'assets/sfx/ui_select_soft_01.wav',
  uiToggle: 'assets/sfx/ui_toggle_pause_01.wav',
  eatAntibody: 'assets/sfx/eat_antibody_01.wav',
  pickupComplement: 'assets/sfx/pickup_complement_pellet_01.wav',
  complementSirenLoop: 'assets/sfx/complement_active_siren_loop_01.wav',
  complementEnemyIngest: 'assets/sfx/complement_enemy_ingest_01.wav',
  pseudopodRamStart: 'assets/sfx/pseudopod_ram_start_01.wav',
  ramEnemyLaunch: 'assets/sfx/ram_enemy_launch_01.wav',
  knockbackChainImpact: 'assets/sfx/knockback_chain_impact_01.wav',
  knockbackWallKill: 'assets/sfx/knockback_wall_kill_01.wav',
  enemyDeathSpin: 'assets/sfx/enemy_death_spin_01.wav',
  playerDeath: 'assets/sfx/player_death_membrane_breach_01.wav',
  nestCleanseWave: 'assets/sfx/nest_cleanse_wave_01.wav',
  levelClearGate: 'assets/sfx/level_clear_gate_01.wav',
  enemyRespawnWarning: 'assets/sfx/enemy_respawn_warning_01.wav',
  feverTickWarning: 'assets/sfx/fever_tick_warning_01.wav',
  antibodyVacuumStart: 'assets/sfx/antibody_vacuum_start_01.wav'
};
const SFX_VOLUME = 0.72;
const SFX_POOL_SIZE = 6;
const JOYSTICK_MAX_DISTANCE = 42;
const JOYSTICK_DEADZONE = 0.08;
const JOYSTICK_DIAGONAL_RATIO = 0.48;
const RADIAL_MOVEMENT = true;
const PLAYER_RADIAL_SPEED = 7.4;
const PLAYER_TURN_BOOST = 1.14;
const PSEUDOPOD_RAM_REARM_THRESHOLD = 0.25;
const PSEUDOPOD_RAM_DURATION = 0.22;
const PSEUDOPOD_RAM_BONUS_SPEED = 2.35;
const PSEUDOPOD_RAM_HIT_RADIUS = TILE * 0.94;
const PSEUDOPOD_RAM_KNOCKBACK = TILE * 9.5;
const PSEUDOPOD_RAM_KNOCKBACK_SPEED = TILE * 13.5;
const PSEUDOPOD_RAM_CONTACT_GRACE = 0.32;
const PSEUDOPOD_RAM_AIM_RANGE = TILE * 3.8;
const PSEUDOPOD_RAM_AIM_WIDTH = TILE * 1.55;
const PSEUDOPOD_RAM_AIM_STRENGTH = 0.72;
const PSEUDOPOD_RAM_CHAIN_HIT_PAD = TILE * 0.72;
const JOYSTICK_RESPONSE_EXPONENT = 0.58;
const GRID_NAV_HELPER = true;
const PINCH_WIDENING = false;
const GRID_HELPER_LOOKAHEAD = TILE * 0.82;
const GRID_HELPER_STRENGTH = 0.58;
const GRID_HELPER_DIAGONAL_STRENGTH = 0.34;
const PLAYER_COLLISION_RADIUS = TILE * 0.24;
const PICKUP_COLLECT_RADIUS = TILE * 0.56;
const PLAYER_FRAME_TIME = 0.14;
const IDLE_PULSE_TIME = 1.45;
const ANTIBODY_VACUUM_RANGE = TILE * 1.15;
const ANTIBODY_VACUUM_SPEED = TILE * 8.5;
const ANTIBODY_COLLECT_DISTANCE = 7;
const ANTIBODY_TOUCH_SOUND_DISTANCE = TILE * 0.96;
const COMPLEMENT_PICKUP_VACUUM_RANGE = TILE * 2.6;
const COMPLEMENT_PICKUP_VACUUM_SPEED = TILE * 9.2;
const COMPLEMENT_PICKUP_COLLECT_DISTANCE = 10;
const BASE_ENEMY_COUNT = 3;
const MAX_ENEMY_COUNT = 8;
const ENEMY_SPEED = TILE * 3.35;
const ENEMY_RADIUS = TILE * 0.34;
const ENEMY_RESPAWN_DELAY = 4.5;
const ENEMY_CONTACT_RADIUS = TILE * 0.54;
const ENEMY_FEVER_BUMP = 7;
const ENEMY_CONTACT_COOLDOWN = 1.1;
const ENEMY_GATE_SPAWN_EXCLUSION_TILES = 7;
const ENEMY_SPAWN_SPACING_TILES = 5;
const ENEMY_SEPARATION_RADIUS = TILE * 1.05;
const ENEMY_SEPARATION_STRENGTH = 0.62;
const COMPLEMENT_ENEMY_SUCTION_RANGE = TILE * 4.2;
const COMPLEMENT_ENEMY_SUCTION_SPEED = TILE * 8.2;
const COMPLEMENT_ENEMY_INGEST_DISTANCE = TILE * 0.42;
const ENEMY_DEATH_EXPAND_DURATION = 0.34;
const ENEMY_DEATH_SHRINK_DURATION = 0.46;
const ENEMY_DEATH_DURATION = ENEMY_DEATH_EXPAND_DURATION + ENEMY_DEATH_SHRINK_DURATION;
const ENEMY_DEATH_EXPAND_SCALE = 1.55;
const ENEMY_DEATH_SPIN = Math.PI * 2 * 3;
const NEST_CLEANSE_DURATION = 1.9;
const RESTART_BUTTON_W = 148;
const RESTART_BUTTON_H = 34;
const PAUSE_BUTTON_SIZE = 48;
const MUSIC_BUTTON_SIZE = 48;
const ZERO_DIR = { x: 0, y: 0 };

const TILE_INDEX = {
  open: 0,
  wall: 1,
  antibody: 2,
  complement: 3,
  gate: 4,
  inflamed: 5,
  necrotic: 6,
  scar: 7
};

let debug = false;
let level;
let state;
let appMode = 'menu';
let currentRun = null;
let seedHistory = [];
let generationSeed = 0;
let menuButtons = [];
let menuSeedOffset = 0;
let pendingNewRunSeed = null;
let appErrorMessage = '';
let lastFrameTime = performance.now();
let sprite = new Image();
sprite.src = PLAYER_SHEET;
let tileSheet = new Image();
tileSheet.src = TILE_SHEET;
let tissueTexture = new Image();
tissueTexture.src = TISSUE_TEXTURE;
let roguelikeBackground = new Image();
roguelikeBackground.src = ROGUELIKE_BACKGROUND;
let enemySheet = new Image();
enemySheet.src = ENEMY_SHEET;
let enemyFrames = null;
let playerFrames = null;
let musicPlayer = {
  audio: null,
  queue: [],
  currentTrack: '',
  started: false,
  blocked: false,
  disabled: false,
  wasPlayingBeforeBackground: false
};
let sfxPools = new Map();
let sfxContext = null;
let sfxBuffers = new Map();
let sfxBufferPromises = new Map();
let activeSoundLoops = new Map();
let lastVacuumStartSfxTime = 0;
let lastFeverWarningSfxTime = 0;
let joystick = {
  activePointerId: null,
  origin: { x: 0, y: 0 },
  inputVector: { x: 0, y: 0 },
  inputMagnitude: 0,
  heldDirection: { ...ZERO_DIR }
};
let heldKeys = new Map();


const STORAGE_KEYS = {
  seeds: 'marrowRunner.seedHistory.v1',
  activeRun: 'marrowRunner.activeRun.v1',
  tutorialSeen: 'marrowRunner.tutorialSeen.v1',
  musicDisabled: 'marrowRunner.musicDisabled.v1'
};

const ENEMY_ARCHETYPES = [
  {
    id: 'pursuer',
    name: 'Hot Strain',
    label: 'Pursuer',
    frame: 0,
    color: '#b72b45',
    accent: '#ff9d91',
    unlockDepth: 1,
    speedScale: 1.0
  },
  {
    id: 'ambusher',
    name: 'Blind Probe',
    label: 'Ambusher',
    frame: 1,
    color: '#7342ac',
    accent: '#e4b4ff',
    unlockDepth: 2,
    speedScale: 0.96
  },
  {
    id: 'flanker',
    name: 'Split Vector',
    label: 'Flanker',
    frame: 2,
    color: '#15907a',
    accent: '#9affdb',
    unlockDepth: 3,
    speedScale: 1.04
  },
  {
    id: 'wanderer',
    name: 'Fever Drift',
    label: 'Wanderer',
    frame: 3,
    color: '#c47b26',
    accent: '#ffd27a',
    unlockDepth: 4,
    speedScale: 0.9
  }
];

function hashString(value) {
  let hash = 2166136261;
  for (let i = 0; i < String(value).length; i++) {
    hash ^= String(value).charCodeAt(i);
    hash = Math.imul(hash, 16777619);
  }
  return hash >>> 0;
}

function seededUnit(salt) {
  let n = (hashString(`${generationSeed}:${salt}`) + 0x6d2b79f5) >>> 0;
  n = Math.imul(n ^ (n >>> 15), n | 1);
  n ^= n + Math.imul(n ^ (n >>> 7), n | 61);
  return ((n ^ (n >>> 14)) >>> 0) / 4294967296;
}

function seededInt(min, max, salt) {
  const low = Math.ceil(min);
  const high = Math.floor(max);
  if (high <= low) return low;
  return low + Math.floor(seededUnit(salt) * (high - low + 1));
}

function shuffledMusicTracks() {
  const tracks = [...MUSIC_TRACKS];
  for (let i = tracks.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [tracks[i], tracks[j]] = [tracks[j], tracks[i]];
  }
  if (tracks.length > 1 && tracks[0] === musicPlayer.currentTrack) {
    [tracks[0], tracks[1]] = [tracks[1], tracks[0]];
  }
  return tracks;
}

function loadMusicPreference() {
  try {
    musicPlayer.disabled = localStorage.getItem(STORAGE_KEYS.musicDisabled) === 'true';
  } catch (_) {
    musicPlayer.disabled = false;
  }
}

function saveMusicPreference() {
  try {
    localStorage.setItem(STORAGE_KEYS.musicDisabled, musicPlayer.disabled ? 'true' : 'false');
  } catch (_) {}
}

function updateMusicToggleLabel() {
  const label = musicPlayer.disabled ? 'Music On' : 'Music Off';
  if (musicToggle) musicToggle.textContent = musicPlayer.disabled ? 'Music Off' : 'Music On';
  if (mobileMusicToggle) mobileMusicToggle.textContent = label;
}

function updateFullscreenToggleLabel() {
  const label = document.fullscreenElement ? 'Exit' : 'Fullscreen';
  if (fullscreenToggle) fullscreenToggle.textContent = document.fullscreenElement ? 'Exit Fullscreen' : 'Fullscreen';
  if (mobileFullscreenToggle) mobileFullscreenToggle.textContent = label;
}

function updateOverlayControls() {
  updateMusicToggleLabel();
  updateFullscreenToggleLabel();
  const canPause = Boolean(state && !state.dead && !state.won);
  const pauseLabel = state?.paused ? 'Resume' : 'Pause';
  if (pauseToggle) pauseToggle.textContent = pauseLabel;
  if (mobilePauseToggle) {
    mobilePauseToggle.textContent = pauseLabel;
    mobilePauseToggle.disabled = !canPause;
  }
  if (mobileMenuToggle) mobileMenuToggle.disabled = false;
}

function ensureMusicAudio() {
  if (!MUSIC_TRACKS.length || typeof Audio === 'undefined') return null;
  if (musicPlayer.audio) return musicPlayer.audio;

  const audio = new Audio();
  audio.preload = 'auto';
  audio.volume = MUSIC_VOLUME;
  audio.addEventListener('ended', () => {
    if (!musicPlayer.disabled) playNextMusicTrack();
  });
  audio.addEventListener('error', () => {
    if (!musicPlayer.disabled) playNextMusicTrack();
  });
  musicPlayer.audio = audio;
  return audio;
}

function stopMusicPlayback() {
  if (!musicPlayer.audio) return;
  musicPlayer.audio.pause();
}

function playNextMusicTrack() {
  if (musicPlayer.disabled) return;
  const audio = ensureMusicAudio();
  if (!audio) return;
  if (!musicPlayer.queue.length) musicPlayer.queue = shuffledMusicTracks();
  const track = musicPlayer.queue.shift();
  if (!track) return;
  musicPlayer.currentTrack = track;
  audio.src = track;
  audio.loop = MUSIC_TRACKS.length <= 1;
  audio.volume = MUSIC_VOLUME;
  musicPlayer.started = true;
  audio.play().then(() => {
    musicPlayer.blocked = false;
  }).catch(() => {
    musicPlayer.blocked = true;
  });
}

function startMusicPlayback() {
  if (musicPlayer.disabled) return;
  const audio = ensureMusicAudio();
  if (!audio) return;
  if (!musicPlayer.currentTrack) {
    playNextMusicTrack();
    return;
  }
  if (!audio.paused) return;
  musicPlayer.started = true;
  audio.play().then(() => {
    musicPlayer.blocked = false;
  }).catch(() => {
    musicPlayer.blocked = true;
  });
}

function toggleMusicPlayback() {
  playSoundEffect(SFX.uiToggle, 0.42);
  musicPlayer.disabled = !musicPlayer.disabled;
  saveMusicPreference();
  updateMusicToggleLabel();
  if (musicPlayer.disabled) stopMusicPlayback();
  else startAudioSystems();
}

function pauseMusicForBackground() {
  if (sfxContext?.state === 'running') sfxContext.suspend().catch(() => {});
  if (!musicPlayer.audio || musicPlayer.audio.paused) return;
  musicPlayer.wasPlayingBeforeBackground = true;
  musicPlayer.audio.pause();
}

function resumeMusicFromBackground() {
  if (sfxContext?.state === 'suspended') sfxContext.resume().catch(() => {});
  if (!musicPlayer.wasPlayingBeforeBackground) return;
  musicPlayer.wasPlayingBeforeBackground = false;
  if (!musicPlayer.disabled && musicPlayer.started) startAudioSystems();
}

function handleMusicVisibilityChange() {
  if (document.hidden) pauseMusicForBackground();
  else resumeMusicFromBackground();
}

function handleWindowFocus() {
  if (!document.hidden) resumeMusicFromBackground();
}

function soundEffectPool(src) {
  if (typeof Audio === 'undefined') return [];
  if (sfxPools.has(src)) return sfxPools.get(src);
  const pool = Array.from({ length: SFX_POOL_SIZE }, () => {
    const audio = new Audio(src);
    audio.preload = 'auto';
    audio.volume = SFX_VOLUME;
    try {
      audio.load();
    } catch (_) {}
    return audio;
  });
  sfxPools.set(src, pool);
  return pool;
}

function ensureSfxContext() {
  const AudioContextCtor = window.AudioContext || window.webkitAudioContext;
  if (!AudioContextCtor) return null;
  if (!sfxContext) sfxContext = new AudioContextCtor();
  if (sfxContext.state === 'suspended') sfxContext.resume().catch(() => {});
  return sfxContext;
}

function preloadSoundEffectBuffer(src) {
  const context = ensureSfxContext();
  if (!context || sfxBuffers.has(src) || sfxBufferPromises.has(src)) return;
  const promise = fetch(src)
    .then(response => response.ok ? response.arrayBuffer() : Promise.reject(new Error(`Unable to load SFX: ${src}`)))
    .then(buffer => context.decodeAudioData(buffer))
    .then(decoded => {
      sfxBuffers.set(src, decoded);
      sfxBufferPromises.delete(src);
      return decoded;
    })
    .catch(() => {
      sfxBufferPromises.delete(src);
      return null;
    });
  sfxBufferPromises.set(src, promise);
}

function warmSoundEffects() {
  for (const src of Object.values(SFX)) {
    soundEffectPool(src);
    preloadSoundEffectBuffer(src);
  }
}

function startAudioSystems() {
  warmSoundEffects();
  startMusicPlayback();
}

function playBufferedSoundEffect(src, volume = SFX_VOLUME) {
  const context = ensureSfxContext();
  const buffer = sfxBuffers.get(src);
  if (!context || !buffer) return false;
  try {
    const source = context.createBufferSource();
    const gain = context.createGain();
    source.buffer = buffer;
    gain.gain.value = volume;
    source.connect(gain);
    gain.connect(context.destination);
    source.start(0);
    return true;
  } catch (_) {
    return false;
  }
}

function startSoundLoop(src, volume = SFX_VOLUME) {
  if (activeSoundLoops.has(src)) return;
  const context = ensureSfxContext();
  const buffer = sfxBuffers.get(src);
  if (context && buffer) {
    try {
      const source = context.createBufferSource();
      const gain = context.createGain();
      source.buffer = buffer;
      source.loop = true;
      gain.gain.value = volume;
      source.connect(gain);
      gain.connect(context.destination);
      activeSoundLoops.set(src, { source, gain });
      source.start(0);
      return;
    } catch (_) {
      activeSoundLoops.delete(src);
    }
  }

  preloadSoundEffectBuffer(src);
  if (typeof Audio === 'undefined') return;
  const audio = new Audio(src);
  audio.loop = true;
  audio.preload = 'auto';
  audio.volume = volume;
  activeSoundLoops.set(src, { audio });
  audio.play().catch(() => {
    activeSoundLoops.delete(src);
  });
}

function stopSoundLoop(src) {
  const loop = activeSoundLoops.get(src);
  if (!loop) return;
  try {
    if (loop.source) loop.source.stop(0);
    if (loop.audio) {
      loop.audio.pause();
      loop.audio.currentTime = 0;
    }
  } catch (_) {}
  activeSoundLoops.delete(src);
}

function stopAllSoundLoops() {
  for (const src of [...activeSoundLoops.keys()]) stopSoundLoop(src);
}

function updateComplementSirenLoop() {
  if (state?.player?.complementTicks > 0 && !state.dead && !state.won && !state.paused) {
    startSoundLoop(SFX.complementSirenLoop, 0.22);
  } else {
    stopSoundLoop(SFX.complementSirenLoop);
  }
}

function playSoundEffect(src, volume = SFX_VOLUME) {
  if (playBufferedSoundEffect(src, volume)) return;
  preloadSoundEffectBuffer(src);
  const pool = soundEffectPool(src);
  if (!pool.length) return;
  const audio = pool.find(candidate => candidate.paused || candidate.ended) || pool[0];
  try {
    audio.pause();
    audio.currentTime = 0;
    audio.volume = volume;
    audio.play().catch(() => {});
  } catch (_) {}
}

function makeRunSeed() {
  const now = new Date();
  const compact = now.toISOString().slice(0, 10).replace(/-/g, '');
  const random = Math.floor(Math.random() * 0xfffff).toString(36).padStart(4, '0').toUpperCase();
  return `MR-${compact}-${random}`;
}

function loadSeedHistory() {
  try {
    const parsed = JSON.parse(localStorage.getItem(STORAGE_KEYS.seeds) || '[]');
    seedHistory = Array.isArray(parsed) ? parsed.filter(entry => entry?.seed).slice(0, 16) : [];
  } catch (_) {
    seedHistory = [];
  }
}

function saveSeedHistory() {
  try {
    localStorage.setItem(STORAGE_KEYS.seeds, JSON.stringify(seedHistory.slice(0, 16)));
  } catch (_) {}
}

function rememberSeed(seed, depth = 1) {
  const existing = seedHistory.find(entry => entry.seed === seed);
  const now = new Date().toISOString();
  if (existing) {
    existing.lastPlayed = now;
    existing.maxDepth = Math.max(existing.maxDepth || 1, depth);
  } else {
    seedHistory.unshift({ seed, createdAt: now, lastPlayed: now, maxDepth: depth });
  }
  seedHistory.sort((a, b) => String(b.lastPlayed || b.createdAt).localeCompare(String(a.lastPlayed || a.createdAt)));
  saveSeedHistory();
}

function saveActiveRun() {
  if (!currentRun) return;
  try {
    localStorage.setItem(STORAGE_KEYS.activeRun, JSON.stringify(currentRun));
  } catch (_) {}
}

function loadActiveRun() {
  try {
    const parsed = JSON.parse(localStorage.getItem(STORAGE_KEYS.activeRun) || 'null');
    return parsed?.seed ? { seed: parsed.seed, depth: parsed.depth || 1, startedAt: parsed.startedAt || new Date().toISOString() } : null;
  } catch (_) {
    return null;
  }
}

function hasSeenTutorial() {
  try {
    return localStorage.getItem(STORAGE_KEYS.tutorialSeen) === 'true';
  } catch (_) {
    return false;
  }
}

function markTutorialSeen() {
  try {
    localStorage.setItem(STORAGE_KEYS.tutorialSeen, 'true');
  } catch (_) {}
}

function clearLocalProgress() {
  try {
    for (const key of Object.values(STORAGE_KEYS)) localStorage.removeItem(key);
  } catch (_) {}
  seedHistory = [];
  currentRun = null;
  pendingNewRunSeed = null;
  musicPlayer.disabled = false;
  updateMusicToggleLabel();
  returnToMenu();
}

function enemyCountForDepth(depth) {
  return clamp(BASE_ENEMY_COUNT + Math.max(0, depth - 1), BASE_ENEMY_COUNT, MAX_ENEMY_COUNT);
}

function availableArchetypesForDepth(depth) {
  return ENEMY_ARCHETYPES.filter(archetype => archetype.unlockDepth <= depth);
}

function archetypeById(id) {
  return ENEMY_ARCHETYPES.find(archetype => archetype.id === id) || ENEMY_ARCHETYPES[0];
}

async function loadLevel() {
  const response = await fetch('data/level_01.json');
  if (!response.ok) throw new Error(`Unable to load level: ${response.status}`);
  return response.json();
}

function clamp(value, min, max) {
  return Math.max(min, Math.min(max, value));
}

function chooseGridDimensions() {
  const viewport = window.visualViewport || window;
  const width = Math.max(320, viewport.width || window.innerWidth);
  const height = Math.max(320, viewport.height || window.innerHeight);
  const aspect = width / height;

  if (aspect < 0.7) {
    const cols = 18;
    const rows = clamp(Math.round(cols / aspect), 30, 34);
    return { cols, rows };
  }

  const targetArea = aspect > 1.6 ? 468 : 500;
  let cols = Math.round(Math.sqrt(targetArea * aspect));
  let rows = Math.round(cols / aspect);

  cols = clamp(cols, 20, 30);
  rows = clamp(rows, 18, 28);
  if (aspect > 1.6) {
    cols = Math.max(cols, 28);
    rows = Math.min(rows, 20);
  }

  return { cols, rows };
}

function blankMap(cols, rows, fill) {
  return Array.from({ length: rows }, () => Array.from({ length: cols }, () => fill));
}

function room(id, label, type, x, y, w, h) {
  return { id, label, type, x, y, w, h, cx: Math.floor(x + w / 2), cy: Math.floor(y + h / 2) };
}

function clampZone(zone, cols, rows) {
  zone.x = clamp(zone.x, 1, cols - zone.w - 1);
  zone.y = clamp(zone.y, 1, rows - zone.h - 1);
  zone.cx = Math.floor(zone.x + zone.w / 2);
  zone.cy = Math.floor(zone.y + zone.h / 2);
  return zone;
}

function zoneAt(zones, tx, ty) {
  return zones.find(zone => tx >= zone.x && tx < zone.x + zone.w && ty >= zone.y && ty < zone.y + zone.h) || null;
}

function clearTile(map, x, y, tile = ' ') {
  if (y <= 0 || x <= 0 || y >= map.length - 1 || x >= map[0].length - 1) return;
  map[y][x] = tile;
}

function carveRect(map, rect, tile = ' ') {
  const rows = map.length;
  const cols = map[0].length;
  for (let y = clamp(rect.y, 1, rows - 2); y < clamp(rect.y + rect.h, 1, rows - 1); y++) {
    for (let x = clamp(rect.x, 1, cols - 2); x < clamp(rect.x + rect.w, 1, cols - 1); x++) {
      map[y][x] = tile;
    }
  }
}

function carveOrganicBrush(map, cx, cy, radiusX = 1, radiusY = radiusX) {
  const minX = Math.floor(cx - radiusX - 1);
  const maxX = Math.ceil(cx + radiusX + 1);
  const minY = Math.floor(cy - radiusY - 1);
  const maxY = Math.ceil(cy + radiusY + 1);
  for (let y = minY; y <= maxY; y++) {
    for (let x = minX; x <= maxX; x++) {
      if (y <= 0 || x <= 0 || y >= map.length - 1 || x >= map[0].length - 1) continue;
      const nx = (x - cx) / Math.max(0.35, radiusX);
      const ny = (y - cy) / Math.max(0.35, radiusY);
      const edgeNoise = (tileNoise(x, y, 113) - 0.5) * 0.42;
      if (nx * nx + ny * ny <= 1 + edgeNoise) map[y][x] = ' ';
    }
  }
}

function carveZoneBlob(map, zone) {
  const rx = Math.max(1.7, zone.w * 0.58);
  const ry = Math.max(1.45, zone.h * 0.62);
  carveOrganicBrush(map, zone.cx, zone.cy, rx, ry);
  carveOrganicBrush(map, zone.cx - 0.7, zone.cy + 0.35, rx * 0.72, ry * 0.76);
  if (zone.w >= 5) carveOrganicBrush(map, zone.cx + 1.1, zone.cy - 0.15, rx * 0.55, ry * 0.58);
  clearTile(map, zone.cx, zone.cy);
}

function chooseOrganicStep(x, y, bx, by, salt) {
  const dx = bx - x;
  const dy = by - y;
  if (dx === 0 && dy === 0) return { x, y };
  const absX = Math.abs(dx);
  const absY = Math.abs(dy);
  const noise = tileNoise(x, y, salt);
  const stepX = Math.sign(dx);
  const stepY = Math.sign(dy);

  if (absX === 0) return { x, y: y + stepY };
  if (absY === 0) return { x: x + stepX, y };
  if (absX > absY && noise > 0.22) return { x: x + stepX, y };
  if (absY > absX && noise > 0.22) return { x, y: y + stepY };
  return noise > 0.5 ? { x: x + stepX, y } : { x, y: y + stepY };
}

function carveOrganicCorridor(map, ax, ay, bx, by, baseRadius = 1) {
  let x = ax;
  let y = ay;
  const guard = map.length * map[0].length;
  for (let step = 0; step < guard && (x !== bx || y !== by); step++) {
    const n = tileNoise(x, y, 140 + step);
    const neck = n < 0.14;
    const bulb = n > 0.78;
    const radius = neck ? 0.72 : baseRadius + (bulb ? 0.55 : 0.12 * tileNoise(x, y, 141 + step));
    carveOrganicBrush(map, x, y, radius, radius * (0.86 + tileNoise(x, y, 142 + step) * 0.28));

    if (bulb && step % 3 === 0) {
      const side = tileNoise(x, y, 143 + step) > 0.5 ? 1 : -1;
      if (Math.abs(bx - x) > Math.abs(by - y)) carveOrganicBrush(map, x, y + side, radius * 0.85, radius * 0.65);
      else carveOrganicBrush(map, x + side, y, radius * 0.65, radius * 0.85);
    }

    const next = chooseOrganicStep(x, y, bx, by, 150 + step);
    x = clamp(next.x, 1, map[0].length - 2);
    y = clamp(next.y, 1, map.length - 2);
  }
  carveOrganicBrush(map, bx, by, baseRadius + 0.1);
}

function carveOrganicTendril(map, ax, ay, length, salt) {
  let x = ax;
  let y = ay;
  let dir = Math.floor(tileNoise(ax, ay, salt) * 4);
  for (let i = 0; i < length; i++) {
    const turn = tileNoise(x, y, salt + 20 + i);
    if (turn < 0.24) dir = (dir + 1) % 4;
    else if (turn > 0.82) dir = (dir + 3) % 4;
    if (dir === 0) x += 1;
    else if (dir === 1) y += 1;
    else if (dir === 2) x -= 1;
    else y -= 1;
    x = clamp(x, 2, map[0].length - 3);
    y = clamp(y, 2, map.length - 3);
    carveOrganicBrush(map, x, y, tileNoise(x, y, salt + 40 + i) > 0.7 ? 1.25 : 0.82);
  }
  if (tileNoise(x, y, salt + 90) > 0.35) carveOrganicBrush(map, x, y, 1.65, 1.35);
}

function carveBaseMaze(map, cols, rows) {
  for (let y = 0; y < rows; y++) {
    for (let x = 0; x < cols; x++) map[y][x] = '#';
  }
}

function addRoomIslands(map, zones) {
  for (const zone of zones) {
    if (zone.w < 5 || zone.h < 4 || zone.type === 'marrow' || zone.type === 'lymph') continue;
    const x = clamp(zone.cx + (tileNoise(zone.cx, zone.cy, 88) > 0.5 ? 1 : -1), 1, map[0].length - 2);
    const y = clamp(zone.cy + (tileNoise(zone.cx, zone.cy, 89) > 0.5 ? 1 : -1), 1, map.length - 2);
    if (x !== zone.cx || y !== zone.cy) map[y][x] = '#';
  }
}

function isOpenForWidening(map, x, y) {
  return map[y]?.[x] === ' ';
}

function clearForWidening(changes, map, x, y) {
  if (y <= 0 || x <= 0 || y >= map.length - 1 || x >= map[0].length - 1) return;
  if (map[y][x] === '#') changes.push({ x, y });
}

function widenPinchPoints(map) {
  if (!PINCH_WIDENING) return;
  const rows = map.length;
  const cols = map[0].length;
  const changes = [];

  for (let y = 1; y < rows - 1; y++) {
    for (let x = 1; x < cols - 1; x++) {
      if (!isOpenForWidening(map, x, y)) continue;

      const horizontalPinch = map[y][x - 1] === '#' && map[y][x + 1] === '#';
      const verticalPinch = map[y - 1][x] === '#' && map[y + 1][x] === '#';
      const verticalFlow = isOpenForWidening(map, x, y - 1) || isOpenForWidening(map, x, y + 1);
      const horizontalFlow = isOpenForWidening(map, x - 1, y) || isOpenForWidening(map, x + 1, y);
      const preferPositive = tileNoise(x, y, 91) > 0.5;

      if (horizontalPinch && verticalFlow) {
        clearForWidening(changes, map, x + (preferPositive ? 1 : -1), y);
      }
      if (verticalPinch && horizontalFlow) {
        clearForWidening(changes, map, x, y + (preferPositive ? 1 : -1));
      }
    }
  }

  for (const change of changes) map[change.y][change.x] = ' ';
}

function antibodyDensityFor(zone) {
  if (!zone) return 4;
  if (zone.type === 'capillary') return 2;
  if (zone.type === 'necrotic' || zone.type === 'infection') return 2;
  if (zone.type === 'complement') return 4;
  if (zone.type === 'marrow') return 3;
  if (zone.type === 'lymph') return 3;
  return 4;
}

function shouldPlaceAntibody(x, y, zone) {
  const density = antibodyDensityFor(zone);
  const stagger = zone ? zone.id.length : 1;
  if (zone && (x === zone.cx || y === zone.cy)) return true;
  return (x * 11 + y * 7 + stagger) % density === 0;
}

function populateAntibodies(map, zones) {
  const rows = map.length;
  const cols = map[0].length;
  for (let y = 1; y < rows - 1; y++) {
    for (let x = 1; x < cols - 1; x++) {
      if (map[y][x] !== ' ') continue;
      const zone = zoneAt(zones, x, y);
      if (shouldPlaceAntibody(x, y, zone)) map[y][x] = '.';
    }
  }
}

function seededShuffle(items, salt) {
  return [...items].sort((a, b) => seededUnit(`${salt}:${a.id || a}`) - seededUnit(`${salt}:${b.id || b}`));
}

function zoneDistance(a, b) {
  return Math.hypot(a.cx - b.cx, a.cy - b.cy);
}

function zoneOverlapScore(a, b, pad = 2) {
  const separated = a.x + a.w + pad <= b.x || b.x + b.w + pad <= a.x || a.y + a.h + pad <= b.y || b.y + b.h + pad <= a.y;
  return separated ? 0 : 1000;
}

function placeSeededZone(id, label, type, cols, rows, w, h, placed, salt, options = {}) {
  const minDistance = options.minDistance || Math.max(5, Math.floor(Math.min(cols, rows) * 0.34));
  let best = null;
  let bestScore = -Infinity;

  for (let i = 0; i < 72; i++) {
    const x = seededInt(1, cols - w - 1, `${salt}:x:${i}`);
    const y = seededInt(1, rows - h - 1, `${salt}:y:${i}`);
    const candidate = clampZone(room(id, label, type, x, y, w, h), cols, rows);
    let score = seededUnit(`${salt}:score:${i}`) * 8;

    for (const zone of placed) {
      const distance = zoneDistance(candidate, zone);
      score += Math.min(distance, 14) * 1.8;
      score -= zoneOverlapScore(candidate, zone, 2);
      if (distance < minDistance) score -= (minDistance - distance) * 24;
    }

    if (options.awayFrom) {
      for (const zone of options.awayFrom) score += Math.min(zoneDistance(candidate, zone), 18) * 2.2;
    }

    if (options.nearCenter) {
      score -= Math.hypot(candidate.cx - cols / 2, candidate.cy - rows / 2) * 0.9;
    }

    if (score > bestScore) {
      best = candidate;
      bestScore = score;
    }
  }

  return best;
}

function buildZoneLinks(zones, archetype) {
  const byId = Object.fromEntries(zones.map(zone => [zone.id, zone]));
  const middle = zones.filter(zone => zone.id !== 'marrow' && zone.id !== 'lymph');
  const ordered = seededShuffle(middle, `link-order:${archetype}`);
  const links = [];
  const add = (a, b, radius = 1.04) => {
    if (!a || !b) return;
    const duplicate = links.some(link => (link.a === a && link.b === b) || (link.a === b && link.b === a));
    if (!duplicate) links.push({ a, b, radius });
  };

  if (archetype === 'hub') {
    const hub = ordered[0] || byId.infection;
    add(byId.marrow, hub, 1.16);
    add(hub, byId.lymph, 1.08);
    for (const zone of ordered.slice(1)) add(hub, zone, 0.92);
    if (ordered[1]) add(byId.marrow, ordered[1], 0.82);
  } else if (archetype === 'fork') {
    add(byId.marrow, ordered[0], 1.06);
    add(byId.marrow, ordered[1], 0.92);
    add(ordered[0], ordered[2], 1.0);
    add(ordered[1], ordered[2] || byId.lymph, 0.94);
    add(ordered[2] || ordered[0], byId.lymph, 1.08);
  } else if (archetype === 'loop') {
    add(byId.marrow, ordered[0], 1.04);
    for (let i = 0; i < ordered.length - 1; i++) add(ordered[i], ordered[i + 1], 1.0);
    add(ordered[ordered.length - 1], byId.lymph, 1.04);
    add(byId.marrow, ordered[ordered.length - 1], 0.82);
    add(ordered[0], byId.lymph, 0.82);
  } else {
    add(byId.marrow, ordered[0], 1.08);
    for (let i = 0; i < ordered.length - 1; i++) add(ordered[i], ordered[i + 1], 1.02);
    add(ordered[ordered.length - 1], byId.lymph, 1.08);
    if (ordered[1]) add(byId.marrow, ordered[1], 0.84);
    if (ordered[2]) add(ordered[0], ordered[2], 0.86);
  }

  return links;
}

function buildZoneLayout(cols, rows) {
  const pocketW = clamp(Math.floor(cols * 0.28), 4, 6);
  const pocketH = clamp(Math.floor(rows * 0.16), 3, 5);
  const startZone = placeSeededZone('marrow', 'Marrow Pocket', 'marrow', cols, rows, 4, 3, [], 'marrow', { minDistance: 4 });
  const gateZone = placeSeededZone('lymph', 'Lymph Chamber', 'lymph', cols, rows, 4, 3, [startZone], 'lymph', {
    awayFrom: [startZone],
    minDistance: Math.max(7, Math.floor(Math.min(cols, rows) * 0.46))
  });
  const placed = [startZone, gateZone];

  const infectionZone = placeSeededZone('infection', 'Infection Nest', 'infection', cols, rows, pocketW, pocketH, placed, 'infection', { awayFrom: [startZone, gateZone], nearCenter: true });
  placed.push(infectionZone);
  const complementZone = placeSeededZone('complement', 'Complement Cyst', 'complement', cols, rows, pocketW, pocketH, placed, 'complement', { awayFrom: [startZone] });
  placed.push(complementZone);

  const extras = seededShuffle([
    { id: 'capillary', label: 'Capillary Pocket', type: 'capillary', h: pocketH },
    { id: 'scar', label: 'Scar Bypass', type: 'scar', h: Math.max(3, pocketH - 1) }
  ], 'extra-zone');
  const extra = extras[0];
  const extraZone = placeSeededZone(extra.id, extra.label, extra.type, cols, rows, pocketW, extra.h, placed, extra.id, { awayFrom: [infectionZone] });
  placed.push(extraZone);

  const middleZones = seededShuffle([infectionZone, complementZone, extraZone], 'path-order');
  const zones = [startZone, ...middleZones, gateZone];
  const archetypes = ['spine', 'hub', 'fork', 'loop'];
  zones.layoutArchetype = archetypes[seededInt(0, archetypes.length - 1, 'layout:archetype')];
  zones.links = buildZoneLinks(zones, zones.layoutArchetype);
  return zones;
}

function buildResponsiveLevel(run = currentRun) {
  const runSeed = run?.seed || 'prototype';
  const depth = run?.depth || 1;
  generationSeed = hashString(`${runSeed}:depth:${depth}`);
  const { cols, rows } = chooseGridDimensions();
  const map = blankMap(cols, rows, '#');
  carveBaseMaze(map, cols, rows);
  const zones = buildZoneLayout(cols, rows);

  for (const zone of zones) carveZoneBlob(map, zone);
  const zoneLinks = zones.links || [];
  for (const link of zoneLinks) carveOrganicCorridor(map, link.a.cx, link.a.cy, link.b.cx, link.b.cy, link.radius);
  if (!zoneLinks.length) {
    for (let i = 0; i < zones.length - 1; i++) carveOrganicCorridor(map, zones[i].cx, zones[i].cy, zones[i + 1].cx, zones[i + 1].cy, 1.05);
  }
  for (const zone of zones) carveOrganicTendril(map, zone.cx, zone.cy, clamp(Math.floor((cols + rows) * 0.12), 4, 8), 210 + zone.id.length);
  addRoomIslands(map, zones);
  widenPinchPoints(map);
  populateAntibodies(map, zones);

  const spawnZone = zones[0];
  const gateZone = zones[zones.length - 1];
  const complementZones = zones.filter(zone => zone.id !== 'marrow' && zone.id !== 'lymph' && zone.id !== 'infection').slice(0, 3);
  for (const zone of complementZones) map[zone.cy][zone.cx] = 'o';
  map[Math.max(1, spawnZone.y + 1)][Math.max(1, spawnZone.x + 1)] = 'S';
  map[gateZone.y + gateZone.h - 2][gateZone.x + gateZone.w - 2] = 'G';

  return { cols, rows, zones, map: map.map(row => row.join('')) };
}

function enemyNestZone(zones) {
  return zones.find(zone => zone.id === 'infection' || zone.type === 'infection')
    || zones.find(zone => zone.type === 'necrotic')
    || zones[Math.floor(zones.length / 2)];
}

function enemySpawnCandidates(map, playerSpawn, zones) {
  const rows = map.length;
  const cols = map[0].length;
  const nest = enemyNestZone(zones);
  const gate = zones.find(zone => zone.type === 'lymph');
  const candidates = [];

  for (let y = 1; y < rows - 1; y++) {
    for (let x = 1; x < cols - 1; x++) {
      if (map[y][x] === '#' || map[y][x] === 'S' || map[y][x] === 'G') continue;
      const playerDistance = Math.hypot(x - playerSpawn.x, y - playerSpawn.y);
      if (playerDistance < 6) continue;
      const gateDistance = gate ? Math.hypot(x - gate.cx, y - gate.cy) : ENEMY_GATE_SPAWN_EXCLUSION_TILES + 1;
      if (gateDistance < ENEMY_GATE_SPAWN_EXCLUSION_TILES) continue;
      const inNest = nest && x >= nest.x && x < nest.x + nest.w && y >= nest.y && y < nest.y + nest.h;
      const nestDistance = nest ? Math.hypot(x - nest.cx, y - nest.cy) : 0;
      const score = (inNest ? 100 : 34 - nestDistance) + tileNoise(x, y, 319) * 3;
      if (inNest || nestDistance <= 3.5) candidates.push({ x, y, score, inNest });
    }
  }

  candidates.sort((a, b) => b.score - a.score);
  return candidates;
}

function chooseSpacedEnemySpawnTiles(candidates, count = BASE_ENEMY_COUNT) {
  const chosen = [];
  for (const candidate of candidates) {
    const tooClose = chosen.some(tile => Math.hypot(tile.x - candidate.x, tile.y - candidate.y) < ENEMY_SPAWN_SPACING_TILES);
    if (!tooClose) chosen.push(candidate);
    if (chosen.length >= count) return chosen;
  }
  for (const candidate of candidates) {
    if (chosen.some(tile => tile.x === candidate.x && tile.y === candidate.y)) continue;
    chosen.push(candidate);
    if (chosen.length >= count) break;
  }
  return chosen;
}

function buildEnemies(map, spawn, zones, run = currentRun) {
  const depth = run?.depth || 1;
  const count = enemyCountForDepth(depth);
  const spawnTiles = chooseSpacedEnemySpawnTiles(enemySpawnCandidates(map, spawn, zones), count);
  const archetypes = availableArchetypesForDepth(depth);
  const enemies = [];
  for (let i = 0; i < Math.min(count, spawnTiles.length); i++) {
    const tile = spawnTiles[i];
    const archetype = archetypes[Math.floor(seededUnit(`enemy:${i}:${depth}`) * archetypes.length) % archetypes.length];
    const center = tileCenter(tile.x, tile.y);
    enemies.push({
      id: `germ-${i + 1}`,
      archetype: archetype.id,
      name: archetype.name,
      x: center.x,
      y: center.y,
      spawnX: center.x,
      spawnY: center.y,
      spawnTx: tile.x,
      spawnTy: tile.y,
      dir: normalizeMovementVector({ x: spawn.x - tile.x, y: spawn.y - tile.y }),
      radius: ENEMY_RADIUS,
      speed: ENEMY_SPEED * archetype.speedScale * (0.94 + (i % 3) * 0.05),
      respawnTicks: 0,
      deathTicks: 0,
      deathX: center.x,
      deathY: center.y,
      contactCooldown: 0,
      ramming: false,
      rammed: false,
      knockbackDir: { ...ZERO_DIR },
      knockbackRemaining: 0,
      knockbackSpeed: 0,
      state: 'active'
    });
  }
  return enemies;
}

function resizeCanvas(cols, rows) {
  canvas.width = cols * TILE;
  canvas.height = rows * TILE;
}

function buildState(levelData, run = currentRun) {
  const responsiveLevel = buildResponsiveLevel(run);
  const map = responsiveLevel.map.map(row => row.split(''));
  let spawn = { x: 1, y: 1 };
  let total = 0;
  for (let y = 0; y < map.length; y++) {
    for (let x = 0; x < map[y].length; x++) {
      if (map[y][x] === 'S') spawn = { x, y };
      if (map[y][x] === '.') total++;
    }
  }
  resizeCanvas(responsiveLevel.cols, responsiveLevel.rows);
  return {
    cols: responsiveLevel.cols,
    rows: responsiveLevel.rows,
    zones: responsiveLevel.zones,
    currentZone: responsiveLevel.zones[0].label,
    map,
    totalAntibodies: total,
    collected: 0,
    vacuumedAntibodies: [],
    vacuumedComplements: [],
    enemyNest: enemyNestZone(responsiveLevel.zones),
    runSeed: run?.seed || 'prototype',
    depth: run?.depth || 1,
    enemies: buildEnemies(map, spawn, responsiveLevel.zones, run),
    upgrades: {
      antibodyVacuum: true
    },
    player: {
      x: spawn.x,
      y: spawn.y,
      px: spawn.x * TILE + TILE / 2,
      py: spawn.y * TILE + TILE / 2,
      dir: { x: 1, y: 0 },
      lastMoveDir: { x: 1, y: 0 },
      queued: { ...ZERO_DIR },
      speed: RADIAL_MOVEMENT ? PLAYER_RADIAL_SPEED : 7.6,
      moving: false,
      targetPx: spawn.x * TILE + TILE / 2,
      targetPy: spawn.y * TILE + TILE / 2,
      animTime: 0,
      frame: 0,
      complementTicks: 0,
      ramTicks: 0,
      ramArmed: true,
      ramDir: { x: 1, y: 0 }
    },
    fever: 0,
    won: false,
    dead: false,
    contactGraceTicks: 0,
    paused: false,
    infectionNeutralized: false,
    cleanseTicks: 0,
    restartButtonBounds: null,
    advanceButtonBounds: null,
    pauseButtonBounds: null,
    musicButtonBounds: null,
    lastTime: lastFrameTime
  };
}

function tutorialEnemy(id, x, y) {
  const center = tileCenter(x, y);
  return {
    id,
    archetype: 'pursuer',
    name: 'Training Germ',
    x: center.x,
    y: center.y,
    spawnX: center.x,
    spawnY: center.y,
    spawnTx: x,
    spawnTy: y,
    dir: { x: -1, y: 0 },
    radius: ENEMY_RADIUS,
    speed: 0,
    respawnTicks: 999,
    deathTicks: 0,
    deathX: center.x,
    deathY: center.y,
    contactCooldown: 999,
    ramming: false,
    rammed: false,
    knockbackDir: { ...ZERO_DIR },
    knockbackRemaining: 0,
    knockbackSpeed: 0,
    state: 'active'
  };
}

function buildTutorialState(returnSeed = null, returnMode = returnSeed ? 'run' : 'menu') {
  const { cols: responsiveCols, rows: responsiveRows } = chooseGridDimensions();
  const cols = clamp(responsiveCols, 18, 24);
  const rows = clamp(responsiveRows, 18, 26);
  const map = blankMap(cols, rows, '#');
  for (let y = 1; y < rows - 1; y++) {
    for (let x = 1; x < cols - 1; x++) map[y][x] = ' ';
  }

  const laneY = Math.floor(rows * 0.55);
  for (let y = 2; y < rows - 2; y++) {
    if (y === laneY || y === laneY - 1 || y === laneY + 1) continue;
    for (let x = 6; x < cols - 3; x++) {
      if ((x + y) % 5 === 0) map[y][x] = '#';
    }
  }
  for (let y = laneY - 1; y <= laneY + 1; y++) {
    for (let x = 2; x < cols - 2; x++) map[y][x] = ' ';
  }

  const playerX = 3;
  const enemyStartX = Math.min(cols - 8, 7);
  const enemyTiles = [0, 2, 4, 6, 8].map(offset => ({ x: enemyStartX + offset, y: laneY })).filter(tile => tile.x < cols - 2);
  const zones = [room('training', 'Training Tissue', 'marrow', 1, laneY - 3, cols - 2, 7)];
  map[laneY][playerX] = 'S';
  map[laneY][cols - 2] = 'G';
  resizeCanvas(cols, rows);
  const spawn = tileCenter(playerX, laneY);

  return {
    cols,
    rows,
    zones,
    currentZone: 'Training Tissue',
    map,
    totalAntibodies: 0,
    collected: 0,
    vacuumedAntibodies: [],
    vacuumedComplements: [],
    enemyNest: null,
    runSeed: 'TUTORIAL',
    depth: 0,
    enemies: enemyTiles.map((tile, index) => tutorialEnemy(`tutorial-germ-${index + 1}`, tile.x, tile.y)),
    upgrades: {
      antibodyVacuum: true
    },
    player: {
      x: playerX,
      y: laneY,
      px: spawn.x,
      py: spawn.y,
      dir: { x: 1, y: 0 },
      lastMoveDir: { x: 1, y: 0 },
      queued: { ...ZERO_DIR },
      speed: RADIAL_MOVEMENT ? PLAYER_RADIAL_SPEED : 7.6,
      moving: false,
      targetPx: spawn.x,
      targetPy: spawn.y,
      animTime: 0,
      frame: 0,
      complementTicks: 0,
      ramTicks: 0,
      ramArmed: true,
      ramDir: { x: 1, y: 0 }
    },
    fever: 0,
    won: false,
    dead: false,
    contactGraceTicks: 0,
    paused: false,
    infectionNeutralized: false,
    cleanseTicks: 0,
    restartButtonBounds: null,
    advanceButtonBounds: null,
    pauseButtonBounds: null,
    musicButtonBounds: null,
    tutorialButtons: [],
    tutorialComplete: false,
    tutorialTicks: 0,
    tutorialChainStarted: false,
    tutorialReturnSeed: returnSeed,
    tutorialReturnMode: returnMode,
    isTutorial: true,
    lastTime: lastFrameTime
  };
}

function tileAt(tx, ty) {
  if (!state.map[ty] || state.map[ty][tx] === undefined) return '#';
  return state.map[ty][tx];
}

function isWall(tx, ty) {
  return tileAt(tx, ty) === '#';
}

function tileCenter(tx, ty) {
  return {
    x: tx * TILE + TILE / 2,
    y: ty * TILE + TILE / 2
  };
}

function playerTile() {
  return {
    x: Math.floor(state.player.px / TILE),
    y: Math.floor(state.player.py / TILE)
  };
}

function normalizeGridDir(dir) {
  return {
    x: Math.sign(dir.x),
    y: Math.sign(dir.y)
  };
}

function normalizeMovementVector(dir) {
  const length = Math.hypot(dir.x, dir.y);
  if (length === 0) return { ...ZERO_DIR };
  return {
    x: dir.x / length,
    y: dir.y / length
  };
}

function isZeroDir(dir) {
  return dir.x === 0 && dir.y === 0;
}

function isDiagonalDir(dir) {
  return dir.x !== 0 && dir.y !== 0;
}

function canStepFrom(tile, dir) {
  if (isZeroDir(dir)) return false;
  const nx = tile.x + dir.x;
  const ny = tile.y + dir.y;
  if (isWall(nx, ny)) return false;
  if (!isDiagonalDir(dir)) return true;
  return !isWall(tile.x + dir.x, tile.y) && !isWall(tile.x, tile.y + dir.y);
}

function fallbackDirectionsFor(dir) {
  if (!isDiagonalDir(dir)) return [dir];
  const current = state.player.dir;
  const xDir = { x: dir.x, y: 0 };
  const yDir = { x: 0, y: dir.y };
  if (current.x === dir.x && current.y === 0) return [dir, xDir, yDir];
  if (current.y === dir.y && current.x === 0) return [dir, yDir, xDir];
  return [dir, xDir, yDir];
}

function startStep(inputDir) {
  const tile = playerTile();
  const candidates = fallbackDirectionsFor(normalizeGridDir(inputDir));
  const dir = candidates.find(candidate => canStepFrom(tile, candidate));
  if (!dir) return false;

  const target = tileCenter(tile.x + dir.x, tile.y + dir.y);
  state.player.dir = { ...dir };
  state.player.targetPx = target.x;
  state.player.targetPy = target.y;
  state.player.moving = true;
  return true;
}

function setDirection(x, y) {
  if (!state || state.won || state.dead || state.paused) return;
  if (RADIAL_MOVEMENT) {
    const dir = normalizeMovementVector({ x, y });
    state.player.queued = { ...ZERO_DIR };
    if (!isZeroDir(dir)) state.player.dir = { ...dir };
    return;
  }

  const dir = normalizeGridDir({ x, y });
  if (isZeroDir(dir)) {
    state.player.queued = { ...ZERO_DIR };
    return;
  }
  if (state.player.moving) {
    state.player.queued = dir;
    return;
  }

  state.player.queued = { ...ZERO_DIR };
  startStep(dir);
}

function setHeldDirection(dir) {
  if (!state || state.won || state.dead || state.paused) return;
  if (dir.x === joystick.heldDirection.x && dir.y === joystick.heldDirection.y) return;
  joystick.heldDirection = { ...dir };
  if (!isZeroDir(dir)) setDirection(dir.x, dir.y);
}

function combinedHeldDirection() {
  let x = 0;
  let y = 0;
  for (const dir of heldKeys.values()) {
    x += dir.x;
    y += dir.y;
  }
  const dir = { x, y };
  return RADIAL_MOVEMENT ? normalizeMovementVector(dir) : normalizeGridDir(dir);
}

function nextHeldDirection() {
  const keyboardDir = combinedHeldDirection();
  if (!isZeroDir(keyboardDir)) return keyboardDir;
  return joystick.activePointerId === null ? ZERO_DIR : joystick.heldDirection;
}

function surfacePoint(event) {
  const rect = gameSurface.getBoundingClientRect();
  return {
    x: event.clientX - rect.left,
    y: event.clientY - rect.top
  };
}

function canvasPoint(event) {
  const rect = canvas.getBoundingClientRect();
  return {
    x: ((event.clientX - rect.left) / rect.width) * canvas.width,
    y: ((event.clientY - rect.top) / rect.height) * canvas.height
  };
}


function startRun(seed, depth = 1) {
  stopAllSoundLoops();
  startAudioSystems();
  currentRun = { seed, depth, startedAt: new Date().toISOString() };
  rememberSeed(seed, depth);
  saveActiveRun();
  appMode = 'playing';
  heldKeys.clear();
  resetJoystick();
  state = buildState(level, currentRun);
  updateHud();
}

function startTutorial(returnSeed = pendingNewRunSeed, returnMode = returnSeed ? 'run' : 'menu') {
  stopAllSoundLoops();
  startAudioSystems();
  if (returnMode === 'run') pendingNewRunSeed = returnSeed || pendingNewRunSeed || makeRunSeed();
  appMode = 'tutorial';
  heldKeys.clear();
  resetJoystick();
  state = buildTutorialState(returnMode === 'run' ? pendingNewRunSeed : null, returnMode);
  runState.textContent = 'Training tissue';
  updateHud();
}

function completeTutorialAndStartRun() {
  const returnMode = state?.tutorialReturnMode || 'run';
  const seed = state?.tutorialReturnSeed || pendingNewRunSeed || makeRunSeed();
  markTutorialSeen();
  pendingNewRunSeed = null;
  if (returnMode === 'menu') {
    returnToMenu();
    return;
  }
  startRun(seed, 1);
}

function skipTutorialAndStartRun() {
  const seed = pendingNewRunSeed || makeRunSeed();
  markTutorialSeen();
  pendingNewRunSeed = null;
  startRun(seed, 1);
}

function startNewRun(forceTutorialDecision = false) {
  stopAllSoundLoops();
  startAudioSystems();
  const seed = makeRunSeed();
  if (!forceTutorialDecision && !hasSeenTutorial()) {
    pendingNewRunSeed = seed;
    appMode = 'tutorialPrompt';
    state = null;
    heldKeys.clear();
    resetJoystick();
    runState.textContent = 'Tutorial available';
    return;
  }
  startRun(seed, 1);
}

function replaySeed(seed) {
  startRun(seed, 1);
}

function resumeRun() {
  const active = loadActiveRun();
  if (active) startRun(active.seed, active.depth || 1);
  else startNewRun();
}

function returnToMenu() {
  stopAllSoundLoops();
  appMode = 'menu';
  state = null;
  heldKeys.clear();
  resetJoystick();
  runState.textContent = 'Choose a seed';
  updateOverlayControls();
}

function advanceRun() {
  if (!currentRun) return;
  currentRun.depth = (currentRun.depth || 1) + 1;
  rememberSeed(currentRun.seed, currentRun.depth);
  saveActiveRun();
  startRun(currentRun.seed, currentRun.depth);
}

function drawMenuButton(label, x, y, w, h, action, sublabel = '') {
  menuButtons.push({ x, y, w, h, action });
  ctx.fillStyle = 'rgba(18, 4, 5, 0.78)';
  ctx.fillRect(x, y, w, h);
  ctx.strokeStyle = 'rgba(255, 196, 132, 0.58)';
  ctx.lineWidth = 1.5;
  ctx.strokeRect(x + 0.5, y + 0.5, w - 1, h - 1);
  ctx.textAlign = 'center';
  ctx.fillStyle = '#fff0d2';
  ctx.font = 'bold 15px Inter, ui-sans-serif, system-ui, sans-serif';
  ctx.fillText(label, x + w / 2, y + 23);
  if (sublabel) {
    ctx.fillStyle = '#d5b69e';
    ctx.font = '11px Inter, ui-sans-serif, system-ui, sans-serif';
    ctx.fillText(sublabel, x + w / 2, y + 40);
  }
}

function drawMenu() {
  menuButtons = [];
  ctx.fillStyle = '#060102';
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  if (roguelikeBackground.complete && roguelikeBackground.naturalWidth > 0) {
    drawImageCover(roguelikeBackground, 0, 0, canvas.width, canvas.height, 0.82);
    ctx.fillStyle = 'rgba(5, 0, 4, 0.42)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
  } else {
    drawTextureCover(0.36);
    ctx.fillStyle = 'rgba(5, 0, 4, 0.62)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
  }

  const panelW = Math.min(canvas.width - 36, 360);
  const x = (canvas.width - panelW) / 2;
  let y = Math.max(36, canvas.height * 0.14);
  ctx.save();
  ctx.fillStyle = 'rgba(8, 0, 5, 0.72)';
  ctx.fillRect(x, y, panelW, 116);
  ctx.strokeStyle = 'rgba(255, 142, 99, 0.44)';
  ctx.strokeRect(x + 0.5, y + 0.5, panelW - 1, 115);
  ctx.textAlign = 'center';
  ctx.fillStyle = '#ffb35f';
  ctx.font = 'bold 13px Inter, ui-sans-serif, system-ui, sans-serif';
  ctx.fillText('MARROW RUNNER', canvas.width / 2, y + 28);
  ctx.fillStyle = '#fff0d2';
  ctx.font = 'bold 28px Inter, ui-sans-serif, system-ui, sans-serif';
  ctx.fillText('Seeded Infection', canvas.width / 2, y + 64);
  ctx.fillStyle = '#d5b69e';
  ctx.font = '12px Inter, ui-sans-serif, system-ui, sans-serif';
  ctx.fillText('Cleanse the nest, reach lymph, descend deeper.', canvas.width / 2, y + 91);
  ctx.font = '10px Inter, ui-sans-serif, system-ui, sans-serif';
  ctx.fillText(APP_VERSION, canvas.width / 2, y + 108);

  y += 136;
  drawMenuButton('New Run', x, y, panelW, 48, () => startNewRun(), 'Generate and save a fresh seed');
  y += 58;
  drawMenuButton('Tutorial', x, y, panelW, 48, () => startTutorial(null, 'menu'), hasSeenTutorial() ? 'Replay movement and ram training' : 'Practice before your first run');
  y += 58;
  const active = loadActiveRun();
  drawMenuButton(active ? 'Resume Run' : 'Start Run', x, y, panelW, 48, () => resumeRun(), active ? `${active.seed}  |  Level ${active.depth || 1}` : 'No saved run yet');
  y += 70;

  ctx.fillStyle = '#f4d5b6';
  ctx.font = 'bold 13px Inter, ui-sans-serif, system-ui, sans-serif';
  ctx.textAlign = 'left';
  ctx.fillText('Replay Seed', x, y);
  y += 10;
  const visibleSeeds = seedHistory.slice(menuSeedOffset, menuSeedOffset + 4);
  if (!visibleSeeds.length) {
    ctx.fillStyle = '#b89478';
    ctx.font = '12px Inter, ui-sans-serif, system-ui, sans-serif';
    ctx.fillText('No saved seeds yet.', x, y + 24);
  }
  for (const entry of visibleSeeds) {
    y += 12;
    const date = new Date(entry.createdAt || entry.lastPlayed || Date.now()).toLocaleDateString();
    drawMenuButton(entry.seed, x, y, panelW, 44, () => replaySeed(entry.seed), `${date}  |  best ${entry.maxDepth || 1}`);
    y += 44;
  }

  y += visibleSeeds.length ? 18 : 58;
  const utilityGap = 10;
  const utilityW = (panelW - utilityGap) / 2;
  drawMenuButton('Credits', x, y, utilityW, 38, () => { appMode = 'credits'; }, 'Version and controls');
  drawMenuButton('Clear Data', x + utilityW + utilityGap, y, utilityW, 38, () => { appMode = 'resetConfirm'; }, 'Reset local saves');
  ctx.restore();
}

function drawInfoPanel(title, lines, buttons) {
  menuButtons = [];
  ctx.fillStyle = '#060102';
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  if (roguelikeBackground.complete && roguelikeBackground.naturalWidth > 0) {
    drawImageCover(roguelikeBackground, 0, 0, canvas.width, canvas.height, 0.76);
    ctx.fillStyle = 'rgba(5, 0, 4, 0.56)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
  } else {
    drawTextureCover(0.32);
    ctx.fillStyle = 'rgba(5, 0, 4, 0.70)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
  }

  const panelW = Math.min(canvas.width - 36, 390);
  const panelH = Math.min(canvas.height - 72, 360);
  const x = (canvas.width - panelW) / 2;
  const y = Math.max(34, (canvas.height - panelH) / 2);
  ctx.save();
  ctx.fillStyle = 'rgba(8, 0, 5, 0.78)';
  ctx.fillRect(x, y, panelW, panelH);
  ctx.strokeStyle = 'rgba(255, 142, 99, 0.50)';
  ctx.strokeRect(x + 0.5, y + 0.5, panelW - 1, panelH - 1);
  ctx.textAlign = 'center';
  ctx.fillStyle = '#fff0d2';
  ctx.font = 'bold 22px Inter, ui-sans-serif, system-ui, sans-serif';
  ctx.fillText(title, canvas.width / 2, y + 36);
  ctx.textAlign = 'left';
  ctx.fillStyle = '#d5b69e';
  ctx.font = '12px Inter, ui-sans-serif, system-ui, sans-serif';
  let lineY = y + 68;
  for (const line of lines) {
    ctx.fillText(line, x + 18, lineY);
    lineY += 18;
  }
  const buttonY = y + panelH - 58;
  const gap = 10;
  const buttonW = buttons.length > 1 ? (panelW - 36 - gap) / 2 : panelW - 36;
  buttons.forEach((button, index) => {
    drawMenuButton(button.label, x + 18 + index * (buttonW + gap), buttonY, buttonW, 40, button.action, button.sublabel || '');
  });
  ctx.restore();
}

function drawCreditsScreen() {
  drawInfoPanel('Marrow Runner', [
    `${APP_VERSION} release candidate`,
    'Move with touch, arrow keys, or WASD.',
    'Release input to rearm Pseudopod Ram.',
    'Dash into germs to start chain knockbacks.',
    'Collect antibodies, cleanse the nest, reach lymph.',
    'Art, music, and SFX are project-owned generated/local assets.',
    'Asset provenance is recorded in assets/asset_manifest.json.'
  ], [{ label: 'Back', action: () => returnToMenu(), sublabel: 'Main menu' }]);
}

function drawResetConfirm() {
  drawInfoPanel('Clear Local Data?', [
    'This removes saved seeds, active run, tutorial state,',
    'and music preference from this browser only.',
    'It does not change the shipped game files.'
  ], [
    { label: 'Cancel', action: () => returnToMenu(), sublabel: 'Keep saves' },
    { label: 'Clear', action: () => clearLocalProgress(), sublabel: 'Reset browser data' }
  ]);
}

function drawErrorScreen() {
  drawInfoPanel('Load Error', [
    appErrorMessage || 'The game failed to load an asset.',
    'Refresh the page after checking the release package.',
    'If this is the itch build, verify all asset folders uploaded.'
  ], [{ label: 'Retry', action: () => window.location.reload(), sublabel: 'Reload page' }]);
}

function drawTutorialPrompt() {
  menuButtons = [];
  ctx.fillStyle = '#060102';
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  if (roguelikeBackground.complete && roguelikeBackground.naturalWidth > 0) {
    drawImageCover(roguelikeBackground, 0, 0, canvas.width, canvas.height, 0.78);
    ctx.fillStyle = 'rgba(5, 0, 4, 0.50)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
  } else {
    drawTextureCover(0.32);
    ctx.fillStyle = 'rgba(5, 0, 4, 0.66)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
  }

  const panelW = Math.min(canvas.width - 36, 380);
  const panelH = 228;
  const x = (canvas.width - panelW) / 2;
  const y = Math.max(42, canvas.height * 0.22);
  ctx.save();
  ctx.fillStyle = 'rgba(8, 0, 5, 0.78)';
  ctx.fillRect(x, y, panelW, panelH);
  ctx.strokeStyle = 'rgba(255, 142, 99, 0.52)';
  ctx.lineWidth = 1.5;
  ctx.strokeRect(x + 0.5, y + 0.5, panelW - 1, panelH - 1);
  ctx.textAlign = 'center';
  ctx.fillStyle = '#ffb35f';
  ctx.font = 'bold 13px Inter, ui-sans-serif, system-ui, sans-serif';
  ctx.fillText('FIRST RUN TRAINING', canvas.width / 2, y + 28);
  ctx.fillStyle = '#fff0d2';
  ctx.font = 'bold 24px Inter, ui-sans-serif, system-ui, sans-serif';
  ctx.fillText('Learn Pseudopod Ram', canvas.width / 2, y + 62);
  ctx.fillStyle = '#d5b69e';
  ctx.font = '12px Inter, ui-sans-serif, system-ui, sans-serif';
  ctx.fillText('Practice movement, dash timing, knockback,', canvas.width / 2, y + 91);
  ctx.fillText('and a prepared chain reaction before the run.', canvas.width / 2, y + 108);
  drawMenuButton('Play Tutorial', x + 18, y + 132, panelW - 36, 44, () => startTutorial(pendingNewRunSeed, 'run'), 'Recommended for the first run');
  drawMenuButton('Dismiss', x + 18, y + 182, panelW - 36, 36, () => skipTutorialAndStartRun(), 'Do not show this prompt again');
  ctx.restore();
}

function handleMenuPointer(event) {
  if (!['menu', 'tutorialPrompt', 'credits', 'resetConfirm', 'error'].includes(appMode)) return false;
  const point = canvasPoint(event);
  const hit = menuButtons.find(button => pointInRect(point, button));
  if (hit) {
    playSoundEffect(SFX.uiSelect, 0.42);
    hit.action();
  }
  event.preventDefault();
  return true;
}

function pauseButtonBounds() {
  return {
    x: canvas.width - PAUSE_BUTTON_SIZE - 12,
    y: 12,
    w: PAUSE_BUTTON_SIZE,
    h: PAUSE_BUTTON_SIZE
  };
}

function musicButtonBounds() {
  return {
    x: canvas.width - PAUSE_BUTTON_SIZE - MUSIC_BUTTON_SIZE - 24,
    y: 12,
    w: MUSIC_BUTTON_SIZE,
    h: MUSIC_BUTTON_SIZE
  };
}

function pauseMenuButtonBounds() {
  const panelW = Math.min(canvas.width - 40, 360);
  const buttonH = 46;
  const gap = 10;
  const x = (canvas.width - panelW) / 2;
  const y = Math.max(88, canvas.height * 0.36);
  return [
    { id: 'resume', label: 'Resume', x, y: y + 70, w: panelW, h: buttonH, action: () => togglePause() },
    { id: 'music', label: musicPlayer.disabled ? 'Music On' : 'Music Off', x, y: y + 70 + buttonH + gap, w: panelW, h: buttonH, action: () => toggleMusicPlayback() },
    { id: 'menu', label: 'Main Menu', x, y: y + 70 + (buttonH + gap) * 2, w: panelW, h: buttonH, action: () => returnToMenu() }
  ];
}

function restartButtonBounds() {
  const w = RESTART_BUTTON_W;
  const h = RESTART_BUTTON_H;
  return {
    x: (canvas.width - w) / 2,
    y: Math.max(120, canvas.height * 0.42 + 64),
    w,
    h
  };
}

function pointInRect(point, rect) {
  return rect && point.x >= rect.x && point.x <= rect.x + rect.w && point.y >= rect.y && point.y <= rect.y + rect.h;
}

function pointInExpandedRect(point, rect, pad = 0) {
  return rect
    && point.x >= rect.x - pad
    && point.x <= rect.x + rect.w + pad
    && point.y >= rect.y - pad
    && point.y <= rect.y + rect.h + pad;
}

function restartFromResult() {
  if (state?.dead) startNewRun();
  else reset();
}

function maybeHandleCanvasRestart(event) {
  if (!state || (!state.dead && !state.won)) return false;
  const point = canvasPoint(event);
  const bounds = state.restartButtonBounds || restartButtonBounds();
  if (!pointInRect(point, bounds)) return false;
  playSoundEffect(SFX.uiSelect, 0.42);
  restartFromResult();
  event.preventDefault();
  return true;
}

function maybeHandleCanvasAdvance(event) {
  if (!state?.won) return false;
  const point = canvasPoint(event);
  const bounds = state.advanceButtonBounds;
  if (!pointInRect(point, bounds)) return false;
  playSoundEffect(SFX.uiSelect, 0.42);
  advanceRun();
  event.preventDefault();
  return true;
}

function togglePause() {
  if (!state || state.dead || state.won) return;
  playSoundEffect(SFX.uiToggle, 0.42);
  state.paused = !state.paused;
  if (state.paused) {
    resetJoystick();
    heldKeys.clear();
    state.player.moving = false;
  }
  updateComplementSirenLoop();
  updateHud();
}

function maybeHandleCanvasMusic(event) {
  if (!state) return false;
  const point = canvasPoint(event);
  const bounds = state.musicButtonBounds || musicButtonBounds();
  if (!pointInExpandedRect(point, bounds, 10)) return false;
  toggleMusicPlayback();
  event.preventDefault();
  return true;
}

function maybeHandleCanvasPauseMenu(event) {
  if (!state?.paused || state.dead || state.won) return false;
  const point = canvasPoint(event);
  const buttons = state.pauseMenuButtons || pauseMenuButtonBounds();
  const hit = buttons.find(button => pointInExpandedRect(point, button, 10));
  if (!hit) return false;
  playSoundEffect(SFX.uiSelect, 0.42);
  hit.action();
  event.preventDefault();
  return true;
}

function maybeHandleCanvasPause(event) {
  if (!state || state.dead || state.won) return false;
  const point = canvasPoint(event);
  const bounds = state.pauseButtonBounds || pauseButtonBounds();
  if (!pointInExpandedRect(point, bounds, 10)) return false;
  togglePause();
  event.preventDefault();
  return true;
}

function setJoystickVisual(origin, pip, active) {
  touchJoystick.style.setProperty('--origin-x', `${origin.x}px`);
  touchJoystick.style.setProperty('--origin-y', `${origin.y}px`);
  touchJoystick.style.setProperty('--pip-x', `${pip.x}px`);
  touchJoystick.style.setProperty('--pip-y', `${pip.y}px`);
  touchJoystick.classList.toggle('is-active', active);
}

function resetJoystick() {
  joystick.activePointerId = null;
  joystick.inputVector = { x: 0, y: 0 };
  joystick.inputMagnitude = 0;
  joystick.heldDirection = { ...ZERO_DIR };
  setJoystickVisual(joystick.origin, joystick.origin, false);
}

function joystickResponseMagnitude(magnitude) {
  const normalized = clamp((magnitude - JOYSTICK_DEADZONE) / (1 - JOYSTICK_DEADZONE), 0, 1);
  return Math.pow(normalized, JOYSTICK_RESPONSE_EXPONENT);
}

function directionFromJoystickVector(vector) {
  const ax = Math.abs(vector.x);
  const ay = Math.abs(vector.y);
  if (ax < JOYSTICK_DEADZONE && ay < JOYSTICK_DEADZONE) return ZERO_DIR;
  if (RADIAL_MOVEMENT) return { ...vector };

  const maxAxis = Math.max(ax, ay);
  const minAxis = Math.min(ax, ay);
  if (minAxis / maxAxis >= JOYSTICK_DIAGONAL_RATIO) {
    return { x: Math.sign(vector.x), y: Math.sign(vector.y) };
  }
  return ax >= ay
    ? { x: Math.sign(vector.x), y: 0 }
    : { x: 0, y: Math.sign(vector.y) };
}

function setDirectionFromVector(vector) {
  setHeldDirection(directionFromJoystickVector(vector));
}

function beginJoystick(event) {
  startAudioSystems();
  if (handleMenuPointer(event)) return;
  if (maybeHandleTutorialPointer(event)) return;
  if (maybeHandleCanvasPauseMenu(event)) return;
  if (maybeHandleCanvasMusic(event)) return;
  if (maybeHandleCanvasAdvance(event)) return;
  if (maybeHandleCanvasRestart(event)) return;
  if (maybeHandleCanvasPause(event)) return;
  if (state && (state.dead || state.won || state.paused)) {
    event.preventDefault();
    return;
  }
  if (joystick.activePointerId !== null) return;

  joystick.activePointerId = event.pointerId;
  joystick.origin = surfacePoint(event);
  joystick.inputVector = { x: 0, y: 0 };
  joystick.inputMagnitude = 0;
  setJoystickVisual(joystick.origin, joystick.origin, true);
  gameSurface.setPointerCapture(event.pointerId);
  event.preventDefault();
}

function updateJoystick(event) {
  if (event.pointerId !== joystick.activePointerId) return;
  const point = surfacePoint(event);
  const dx = point.x - joystick.origin.x;
  const dy = point.y - joystick.origin.y;
  const distance = Math.hypot(dx, dy);
  const magnitude = Math.min(distance / JOYSTICK_MAX_DISTANCE, 1);

  if (magnitude < JOYSTICK_DEADZONE || distance === 0) {
    joystick.inputVector = { x: 0, y: 0 };
    joystick.inputMagnitude = 0;
    setHeldDirection(ZERO_DIR);
    setJoystickVisual(joystick.origin, joystick.origin, true);
    event.preventDefault();
    return;
  }

  const nx = dx / distance;
  const ny = dy / distance;
  const clampedDistance = Math.min(distance, JOYSTICK_MAX_DISTANCE);
  const responseMagnitude = joystickResponseMagnitude(magnitude);
  joystick.inputVector = { x: nx * responseMagnitude, y: ny * responseMagnitude };
  joystick.inputMagnitude = responseMagnitude;
  setJoystickVisual(
    joystick.origin,
    {
      x: joystick.origin.x + nx * clampedDistance,
      y: joystick.origin.y + ny * clampedDistance
    },
    true
  );
  setDirectionFromVector(joystick.inputVector);
  event.preventDefault();
}

function endJoystick(event) {
  if (event.pointerId !== joystick.activePointerId) return;
  resetJoystick();
  event.preventDefault();
}

function feverRateFor(zone) {
  if (state.player.complementTicks > 0) return 1.0;
  if (zone?.type === 'infection') return 4.2;
  if (zone?.type === 'necrotic') return 3.2;
  if (zone?.type === 'complement') return 1.35;
  return 1.8;
}

function circleOverlapsWall(cx, cy, radius) {
  const minTx = Math.floor((cx - radius) / TILE);
  const maxTx = Math.floor((cx + radius) / TILE);
  const minTy = Math.floor((cy - radius) / TILE);
  const maxTy = Math.floor((cy + radius) / TILE);
  for (let ty = minTy; ty <= maxTy; ty++) {
    for (let tx = minTx; tx <= maxTx; tx++) {
      if (!isWall(tx, ty)) continue;
      const left = tx * TILE;
      const top = ty * TILE;
      const nearestX = clamp(cx, left, left + TILE);
      const nearestY = clamp(cy, top, top + TILE);
      if (Math.hypot(cx - nearestX, cy - nearestY) < radius) return true;
    }
  }
  return false;
}

function movementInputVector() {
  const keyboardDir = combinedHeldDirection();
  if (!isZeroDir(keyboardDir)) return keyboardDir;
  if (joystick.activePointerId === null || isZeroDir(joystick.inputVector)) return ZERO_DIR;
  return { ...joystick.inputVector };
}

function canUseAssistStep(tile, dir) {
  return canStepFrom(tile, normalizeGridDir(dir));
}

function assistCandidatesFor(input) {
  const p = state.player;
  const tile = playerTile();
  const lookTx = Math.floor((p.px + input.x * GRID_HELPER_LOOKAHEAD) / TILE);
  const lookTy = Math.floor((p.py + input.y * GRID_HELPER_LOOKAHEAD) / TILE);
  const dx = clamp(lookTx - tile.x, -1, 1);
  const dy = clamp(lookTy - tile.y, -1, 1);
  const sx = Math.sign(input.x);
  const sy = Math.sign(input.y);
  const horizontalFirst = Math.abs(input.x) >= Math.abs(input.y);
  const candidates = [];

  if (dx !== 0 || dy !== 0) candidates.push({ x: dx, y: dy });
  if (horizontalFirst) {
    if (sx !== 0) candidates.push({ x: sx, y: 0 });
    if (sy !== 0) candidates.push({ x: 0, y: sy });
  } else {
    if (sy !== 0) candidates.push({ x: 0, y: sy });
    if (sx !== 0) candidates.push({ x: sx, y: 0 });
  }

  return candidates.filter((candidate, index) => {
    if (isZeroDir(candidate)) return false;
    return candidates.findIndex(other => other.x === candidate.x && other.y === candidate.y) === index;
  });
}

function gridNavigationAssist(input) {
  if (!GRID_NAV_HELPER || isZeroDir(input)) return input;
  const tile = playerTile();
  const candidate = assistCandidatesFor(input).find(dir => canUseAssistStep(tile, dir));
  if (!candidate) return input;

  const p = state.player;
  const goal = tileCenter(tile.x + candidate.x, tile.y + candidate.y);
  const strength = isDiagonalDir(candidate) ? GRID_HELPER_DIAGONAL_STRENGTH : GRID_HELPER_STRENGTH;
  const pull = {
    x: clamp((goal.x - p.px) / (TILE * 0.5), -1, 1),
    y: clamp((goal.y - p.py) / (TILE * 0.5), -1, 1)
  };

  return normalizeMovementVector({
    x: input.x + pull.x * strength,
    y: input.y + pull.y * strength
  });
}

function updatePseudopodRam(dt, rawInput, inputDirection) {
  const p = state.player;
  const inputMagnitude = clamp(Math.hypot(rawInput.x, rawInput.y), 0, 1);
  if (p.ramTicks > 0) p.ramTicks = Math.max(0, p.ramTicks - dt);
  if (inputMagnitude < PSEUDOPOD_RAM_REARM_THRESHOLD) {
    p.ramArmed = true;
    return;
  }
  if (p.ramArmed && !p.moving) {
    playSoundEffect(SFX.pseudopodRamStart, 0.74);
    p.ramTicks = PSEUDOPOD_RAM_DURATION;
    p.ramDir = { ...inputDirection };
    p.ramArmed = false;
  }
}

function ramSpeedMultiplier(player) {
  if (player.ramTicks <= 0) return 1;
  const t = player.ramTicks / PSEUDOPOD_RAM_DURATION;
  return 1 + PSEUDOPOD_RAM_BONUS_SPEED * t * t;
}

function enemyRadius(enemy) {
  return enemy.radius || ENEMY_RADIUS;
}

function enemyTile(enemy) {
  return {
    x: clamp(Math.floor(enemy.x / TILE), 0, state.cols - 1),
    y: clamp(Math.floor(enemy.y / TILE), 0, state.rows - 1)
  };
}

function isEnemyWalkableTile(x, y) {
  return !isWall(x, y);
}

function nearestWalkableGoal(goal, fallback) {
  const gx = clamp(Math.floor(goal.x), 0, state.cols - 1);
  const gy = clamp(Math.floor(goal.y), 0, state.rows - 1);
  if (isEnemyWalkableTile(gx, gy)) return { x: gx, y: gy };
  let best = null;
  for (let radius = 1; radius <= 4; radius++) {
    for (let y = gy - radius; y <= gy + radius; y++) {
      for (let x = gx - radius; x <= gx + radius; x++) {
        if (!isEnemyWalkableTile(x, y)) continue;
        const score = Math.hypot(x - gx, y - gy);
        if (!best || score < best.score) best = { x, y, score };
      }
    }
    if (best) return { x: best.x, y: best.y };
  }
  return fallback;
}

function enemyGoalTile(enemy, player) {
  const pTile = playerTile();
  const dir = normalizeMovementVector(player.dir || { x: 1, y: 0 });
  const gridDir = normalizeGridDir(dir);
  const archetype = enemy.archetype || 'pursuer';
  if (archetype === 'ambusher') {
    return nearestWalkableGoal({ x: pTile.x + gridDir.x * 4, y: pTile.y + gridDir.y * 4 }, pTile);
  }
  if (archetype === 'flanker') {
    const side = tileNoise(Math.floor(enemy.x / TILE), Math.floor(enemy.y / TILE), 811) > 0.5 ? 1 : -1;
    return nearestWalkableGoal({
      x: pTile.x + gridDir.x * 2 + -gridDir.y * side * 3,
      y: pTile.y + gridDir.y * 2 + gridDir.x * side * 3
    }, pTile);
  }
  if (archetype === 'wanderer') {
    const salt = Math.floor(state.player.animTime * 0.55) + hashString(enemy.id);
    const ox = Math.floor(tileNoise(pTile.x, pTile.y, 900 + salt) * 7) - 3;
    const oy = Math.floor(tileNoise(pTile.y, pTile.x, 930 + salt) * 7) - 3;
    return nearestWalkableGoal({ x: pTile.x + ox, y: pTile.y + oy }, pTile);
  }
  return pTile;
}

function findNextEnemyTile(enemy, goal) {
  const start = enemyTile(enemy);
  const goalTile = nearestWalkableGoal(goal, start);
  if (!isEnemyWalkableTile(start.x, start.y) || !isEnemyWalkableTile(goalTile.x, goalTile.y)) return null;
  if (start.x === goalTile.x && start.y === goalTile.y) return { x: goalTile.x, y: goalTile.y, sameTile: true };

  const visited = Array.from({ length: state.rows }, () => Array.from({ length: state.cols }, () => false));
  const queue = [{ x: start.x, y: start.y, firstX: start.x, firstY: start.y }];
  visited[start.y][start.x] = true;
  const dirs = [
    { x: 1, y: 0 },
    { x: -1, y: 0 },
    { x: 0, y: 1 },
    { x: 0, y: -1 }
  ];

  for (let head = 0; head < queue.length; head++) {
    const node = queue[head];
    for (const dir of dirs) {
      const nx = node.x + dir.x;
      const ny = node.y + dir.y;
      if (ny < 0 || nx < 0 || ny >= state.rows || nx >= state.cols) continue;
      if (visited[ny][nx] || !isEnemyWalkableTile(nx, ny)) continue;
      visited[ny][nx] = true;
      const firstX = node.x === start.x && node.y === start.y ? nx : node.firstX;
      const firstY = node.x === start.x && node.y === start.y ? ny : node.firstY;
      if (nx === goalTile.x && ny === goalTile.y) return { x: firstX, y: firstY, sameTile: false };
      queue.push({ x: nx, y: ny, firstX, firstY });
    }
  }

  return null;
}

function enemyPathTarget(enemy, player) {
  const goal = enemyGoalTile(enemy, player);
  const nextTile = findNextEnemyTile(enemy, goal);
  if (!nextTile) return null;
  if (nextTile.sameTile) return { x: player.px, y: player.py, hasPath: true };
  const center = tileCenter(nextTile.x, nextTile.y);
  return { ...center, hasPath: true };
}

function killEnemy(enemy, cause = 'generic') {
  if (enemy.state === 'dying' || enemy.state === 'respawning') return;
  if (cause !== 'cleanse') playSoundEffect(SFX.enemyDeathSpin, cause === 'generic' ? 0.58 : 0.34);
  enemy.state = 'dying';
  enemy.deathTicks = ENEMY_DEATH_DURATION;
  enemy.deathX = enemy.x;
  enemy.deathY = enemy.y;
  enemy.rammed = false;
  resetEnemyKnockback(enemy);
}

function finishEnemyDeath(enemy) {
  enemy.state = 'respawning';
  enemy.respawnTicks = ENEMY_RESPAWN_DELAY;
  enemy.x = enemy.spawnX;
  enemy.y = enemy.spawnY;
  enemy.deathTicks = 0;
  resetEnemyKnockback(enemy);
}

function updateEnemyDeath(enemy, dt) {
  enemy.deathTicks = Math.max(0, enemy.deathTicks - dt);
  if (enemy.deathTicks <= 0) finishEnemyDeath(enemy);
}

function killPlayer(enemy) {
  if (state.dead || state.won) return;
  playSoundEffect(SFX.playerDeath, 0.9);
  stopAllSoundLoops();
  state.dead = true;
  state.fever = 100;
  state.player.moving = false;
  state.player.ramTicks = 0;
  resetJoystick();
  runState.textContent = enemy?.name ? `${enemy.name} breached the membrane` : 'Infection breached the membrane';
}

function resetEnemyKnockback(enemy) {
  enemy.knockbackDir = { ...ZERO_DIR };
  enemy.knockbackRemaining = 0;
  enemy.knockbackSpeed = 0;
}


function knockbackTargetBias(enemy, dir) {
  const forward = normalizeMovementVector(dir);
  if (isZeroDir(forward)) return forward;
  let best = null;
  for (const other of state.enemies) {
    if (other === enemy || other.state === 'dying' || other.state === 'respawning' || other.state === 'knockback') continue;
    const dx = other.x - enemy.x;
    const dy = other.y - enemy.y;
    const ahead = dx * forward.x + dy * forward.y;
    if (ahead <= 0 || ahead > PSEUDOPOD_RAM_AIM_RANGE) continue;
    const lateral = Math.abs(dx * -forward.y + dy * forward.x);
    if (lateral > PSEUDOPOD_RAM_AIM_WIDTH + enemyRadius(other)) continue;
    const score = ahead + lateral * 1.35;
    if (!best || score < best.score) best = { enemy: other, score };
  }
  if (!best) return forward;
  const toward = normalizeMovementVector({ x: best.enemy.x - enemy.x, y: best.enemy.y - enemy.y });
  return normalizeMovementVector({
    x: forward.x * (1 - PSEUDOPOD_RAM_AIM_STRENGTH) + toward.x * PSEUDOPOD_RAM_AIM_STRENGTH,
    y: forward.y * (1 - PSEUDOPOD_RAM_AIM_STRENGTH) + toward.y * PSEUDOPOD_RAM_AIM_STRENGTH
  });
}

function launchEnemyKnockback(enemy, dir, distance = PSEUDOPOD_RAM_KNOCKBACK, source = 'ram') {
  if (enemy.state === 'dying' || enemy.state === 'respawning') return;
  const knockDir = knockbackTargetBias(enemy, dir);
  if (isZeroDir(knockDir)) return;
  playSoundEffect(source === 'chain' ? SFX.knockbackChainImpact : SFX.ramEnemyLaunch, source === 'chain' ? 0.78 : 0.82);
  enemy.state = 'knockback';
  enemy.rammed = true;
  enemy.dir = { ...knockDir };
  enemy.knockbackDir = { ...knockDir };
  enemy.knockbackRemaining = Math.max(enemy.knockbackRemaining || 0, distance);
  enemy.knockbackSpeed = PSEUDOPOD_RAM_KNOCKBACK_SPEED;
  enemy.contactCooldown = Math.max(enemy.contactCooldown || 0, PSEUDOPOD_RAM_CONTACT_GRACE);
  state.contactGraceTicks = Math.max(state.contactGraceTicks || 0, PSEUDOPOD_RAM_CONTACT_GRACE);
}

function stopEnemyKnockback(enemy) {
  enemy.state = 'active';
  enemy.contactCooldown = Math.max(enemy.contactCooldown || 0, PSEUDOPOD_RAM_CONTACT_GRACE);
  resetEnemyKnockback(enemy);
}

function knockbackCollisionEnemy(enemy, x, y, dir) {
  for (const other of state.enemies) {
    if (other === enemy || other.state === 'dying' || other.state === 'respawning') continue;
    const dx = other.x - x;
    const dy = other.y - y;
    const ahead = dx * dir.x + dy * dir.y;
    if (ahead < 0) continue;
    const distance = Math.hypot(dx, dy);
    if (distance <= enemyRadius(enemy) + enemyRadius(other) + PSEUDOPOD_RAM_CHAIN_HIT_PAD) return other;
  }
  return null;
}

function updateEnemyKnockback(enemy, dt) {
  const dir = normalizeMovementVector(enemy.knockbackDir || ZERO_DIR);
  if (isZeroDir(dir) || enemy.knockbackRemaining <= 0) {
    stopEnemyKnockback(enemy);
    return;
  }

  let remainingStep = Math.min(enemy.knockbackSpeed * dt, enemy.knockbackRemaining);
  const microStep = TILE * 0.18;
  while (remainingStep > 0 && enemy.state === 'knockback') {
    const step = Math.min(microStep, remainingStep);
    const nx = enemy.x + dir.x * step;
    const ny = enemy.y + dir.y * step;

    if (circleOverlapsWall(nx, ny, enemyRadius(enemy))) {
      playSoundEffect(SFX.knockbackWallKill, 0.86);
      killEnemy(enemy, 'wall');
      return;
    }

    const hitEnemy = knockbackCollisionEnemy(enemy, nx, ny, dir);
    if (hitEnemy) {
      enemy.x = nx;
      enemy.y = ny;
      enemy.knockbackRemaining = Math.max(0, enemy.knockbackRemaining - step);
      const chainDistance = Math.max(enemy.knockbackRemaining, PSEUDOPOD_RAM_KNOCKBACK * 0.72);
      launchEnemyKnockback(hitEnemy, dir, chainDistance, 'chain');
      killEnemy(enemy, 'chain');
      return;
    }

    enemy.x = nx;
    enemy.y = ny;
    enemy.knockbackRemaining = Math.max(0, enemy.knockbackRemaining - step);
    remainingStep -= step;
  }

  if (enemy.state === 'knockback' && enemy.knockbackRemaining <= 0) stopEnemyKnockback(enemy);
}

function tryPseudopodRamHit(enemy) {
  const p = state.player;
  if (p.ramTicks <= 0 || enemy.state !== 'active' || enemy.rammed) return false;
  const dir = normalizeMovementVector(p.ramDir || p.dir);
  if (isZeroDir(dir)) return false;
  const distance = Math.hypot(enemy.x - p.px, enemy.y - p.py);
  if (distance > PSEUDOPOD_RAM_HIT_RADIUS + enemyRadius(enemy) + PSEUDOPOD_RAM_CHAIN_HIT_PAD * 0.55) return false;
  launchEnemyKnockback(enemy, dir, PSEUDOPOD_RAM_KNOCKBACK, 'ram');
  return true;
}

function handlePseudopodRamHits() {
  const p = state.player;
  if (!state.enemies.length) return;
  if (p.ramTicks <= 0) {
    for (const enemy of state.enemies) enemy.rammed = false;
    return;
  }

  for (const enemy of state.enemies) tryPseudopodRamHit(enemy);
}

function enemyCanMoveTo(enemy, x, y) {
  return !circleOverlapsWall(x, y, enemyRadius(enemy));
}


function enemySeparationVector(enemy) {
  let x = 0;
  let y = 0;
  for (const other of state.enemies) {
    if (other === enemy || other.state !== 'active') continue;
    const dx = enemy.x - other.x;
    const dy = enemy.y - other.y;
    const distance = Math.hypot(dx, dy);
    if (distance <= 0.01 || distance >= ENEMY_SEPARATION_RADIUS) continue;
    const strength = (1 - distance / ENEMY_SEPARATION_RADIUS) * ENEMY_SEPARATION_STRENGTH;
    x += (dx / distance) * strength;
    y += (dy / distance) * strength;
  }
  return { x, y };
}

function moveEnemyTowardTarget(enemy, target, dt, speed) {
  const dx = target.x - enemy.x;
  const dy = target.y - enemy.y;
  const targetDistance = Math.hypot(dx, dy);
  if (targetDistance <= 0.01) return false;
  const pathDir = { x: dx / targetDistance, y: dy / targetDistance };
  const separate = enemySeparationVector(enemy);
  const dir = normalizeMovementVector({
    x: pathDir.x + separate.x,
    y: pathDir.y + separate.y
  });
  if (isZeroDir(dir)) return false;
  const distance = Math.min(speed * dt, targetDistance);
  const nextX = enemy.x + dir.x * distance;
  const nextY = enemy.y + dir.y * distance;
  let moved = false;

  if (enemyCanMoveTo(enemy, nextX, enemy.y)) {
    enemy.x = nextX;
    moved = true;
  }
  if (enemyCanMoveTo(enemy, enemy.x, nextY)) {
    enemy.y = nextY;
    moved = true;
  }
  if (moved) enemy.dir = dir;
  return moved;
}

function moveEnemy(enemy, dt, speed = enemy.speed) {
  const target = enemyPathTarget(enemy, state.player);
  if (!target) {
    enemy.dir = enemy.dir || { x: 1, y: 0 };
    return false;
  }
  return moveEnemyTowardTarget(enemy, target, dt, speed);
}

function respawnEnemy(enemy) {
  if (state.infectionNeutralized) return;
  playSoundEffect(SFX.enemyRespawnWarning, 0.42);
  enemy.x = enemy.spawnX;
  enemy.y = enemy.spawnY;
  enemy.state = 'active';
  enemy.respawnTicks = 0;
  enemy.deathTicks = 0;
  enemy.rammed = false;
  resetEnemyKnockback(enemy);
  enemy.contactCooldown = ENEMY_CONTACT_COOLDOWN;
}

function updateEnemies(dt) {
  for (const enemy of state.enemies) {
    if (enemy.contactCooldown > 0) enemy.contactCooldown = Math.max(0, enemy.contactCooldown - dt);
    if (enemy.state === 'dying') {
      updateEnemyDeath(enemy, dt);
      continue;
    }
    if (enemy.state === 'respawning') {
      if (state.infectionNeutralized) continue;
      enemy.respawnTicks = Math.max(0, enemy.respawnTicks - dt);
      if (enemy.respawnTicks <= 0) respawnEnemy(enemy);
      continue;
    }
    if (enemy.state === 'knockback') {
      updateEnemyKnockback(enemy, dt);
      continue;
    }

    if (tryPseudopodRamHit(enemy)) continue;

    const distanceToPlayer = Math.hypot(state.player.px - enemy.x, state.player.py - enemy.y);
    if (state.player.complementTicks > 0 && distanceToPlayer <= COMPLEMENT_ENEMY_SUCTION_RANGE) {
      moveEnemy(enemy, dt, COMPLEMENT_ENEMY_SUCTION_SPEED);
      const contact = Math.hypot(enemy.x - state.player.px, enemy.y - state.player.py);
      if (contact <= COMPLEMENT_ENEMY_INGEST_DISTANCE) {
        playSoundEffect(SFX.complementEnemyIngest, 0.82);
        killEnemy(enemy, 'complement');
      }
      continue;
    }

    moveEnemy(enemy, dt);
    if (tryPseudopodRamHit(enemy)) continue;
    const contact = Math.hypot(enemy.x - state.player.px, enemy.y - state.player.py);
    if (contact <= ENEMY_CONTACT_RADIUS && enemy.contactCooldown <= 0 && state.contactGraceTicks <= 0 && state.player.ramTicks <= 0) {
      enemy.contactCooldown = ENEMY_CONTACT_COOLDOWN;
      if (!state.isTutorial) {
        state.fever = Math.min(100, state.fever + ENEMY_FEVER_BUMP);
        killPlayer(enemy);
      }
    }
  }
}


function triggerNestCleanse() {
  if (state.infectionNeutralized) return;
  playSoundEffect(SFX.nestCleanseWave, 0.86);
  state.infectionNeutralized = true;
  state.cleanseTicks = NEST_CLEANSE_DURATION;
  if (state.enemyNest) state.currentZone = `${state.enemyNest.label} neutralized`;
  for (const enemy of state.enemies) {
    if (enemy.state === 'active') killEnemy(enemy, 'cleanse');
    else if (enemy.state === 'respawning') enemy.respawnTicks = Math.max(enemy.respawnTicks, ENEMY_RESPAWN_DELAY);
  }
  runState.textContent = 'Infection nest neutralized';
}

function checkCollectionComplete() {
  if (state.collected >= state.totalAntibodies) triggerNestCleanse();
}

function movePlayerRadially(dt) {
  const rawInput = movementInputVector();
  if (isZeroDir(rawInput)) {
    state.player.moving = false;
    updatePseudopodRam(dt, ZERO_DIR, state.player.dir);
    return;
  }

  const p = state.player;
  const inputDirection = normalizeMovementVector(rawInput);
  updatePseudopodRam(dt, rawInput, inputDirection);
  const previousMoveDir = p.lastMoveDir || p.dir;
  const turnAmount = clamp(1 - ((previousMoveDir.x * inputDirection.x + previousMoveDir.y * inputDirection.y + 1) / 2), 0, 1);
  const input = gridNavigationAssist(inputDirection);
  p.dir = { ...input };
  const speedMultiplier = (1 + turnAmount * PLAYER_TURN_BOOST * 0.08) * ramSpeedMultiplier(p);
  const distance = p.speed * TILE * speedMultiplier * dt;
  const nextX = p.px + input.x * distance;
  const nextY = p.py + input.y * distance;
  let moved = false;

  if (!circleOverlapsWall(nextX, p.py, PLAYER_COLLISION_RADIUS)) {
    p.px = nextX;
    moved = true;
  }
  if (!circleOverlapsWall(p.px, nextY, PLAYER_COLLISION_RADIUS)) {
    p.py = nextY;
    moved = true;
  }
  if (moved) p.lastMoveDir = { ...input };
  p.moving = moved;
  handlePseudopodRamHits();
}

function update(dt) {
  if (appMode === 'menu' || appMode === 'tutorialPrompt' || !state) return;
  if (state.paused) {
    updateComplementSirenLoop();
    updateHud();
    return;
  }
  if (state.contactGraceTicks > 0) state.contactGraceTicks = Math.max(0, state.contactGraceTicks - dt);
  if (state.cleanseTicks > 0) state.cleanseTicks = Math.max(0, state.cleanseTicks - dt);
  if (state.won || state.dead) {
    updateComplementSirenLoop();
    state.player.animTime += dt;
    updateHud();
    return;
  }
  vacuumAntibodies(dt);
  const tile = playerTile();
  const playerZone = zoneAt(state.zones, tile.x, tile.y);
  if (!state.isTutorial) state.fever = Math.min(100, state.fever + dt * feverRateFor(playerZone));
  state.player.animTime += dt;
  if (state.player.complementTicks > 0) state.player.complementTicks = Math.max(0, state.player.complementTicks - dt);
  updateComplementSirenLoop();

  if (state.fever >= 75 && !state.isTutorial) {
    const now = performance.now();
    if (now - lastFeverWarningSfxTime > 2600) {
      playSoundEffect(SFX.feverTickWarning, 0.26);
      lastFeverWarningSfxTime = now;
    }
  }

  if (RADIAL_MOVEMENT) {
    movePlayerRadially(dt);
    collectCurrentTile();
    if (!state.won) updateEnemies(dt);
    updateTutorialState(dt);
    updateHud();
    return;
  }

  updateEnemies(dt);
  if (state.dead) {
    updateHud();
    return;
  }

  if (state.player.moving) {
    const dx = state.player.targetPx - state.player.px;
    const dy = state.player.targetPy - state.player.py;
    const distance = Math.hypot(dx, dy);
    const directionScale = isDiagonalDir(state.player.dir) ? Math.SQRT2 : 1;
    const step = state.player.speed * dt * TILE * directionScale;

    if (distance <= step) {
      state.player.px = state.player.targetPx;
      state.player.py = state.player.targetPy;
      state.player.moving = false;
      collectCurrentTile();

      const queued = state.player.queued;
      const held = nextHeldDirection();
      state.player.queued = { ...ZERO_DIR };
      if (!isZeroDir(queued)) startStep(queued);
      else if (!isZeroDir(held)) startStep(held);
    } else {
      state.player.px += (dx / distance) * step;
      state.player.py += (dy / distance) * step;
    }
  } else {
    collectCurrentTile();
  }

  updateHud();
}

function finishAntibodyCollection(playSound = true) {
  state.collected++;
  if (playSound) playSoundEffect(SFX.eatAntibody);
  checkCollectionComplete();
}

function collectAntibodyAt(tx, ty) {
  if (tileAt(tx, ty) !== '.') return false;
  state.map[ty][tx] = ' ';
  finishAntibodyCollection();
  return true;
}

function activateComplementPower(tx, ty) {
  playSoundEffect(SFX.pickupComplement, 0.78);
  state.player.complementTicks = 7;
  updateComplementSirenLoop();
  collectNearbyAntibodies(tx, ty);
}

function collectComplementAt(tx, ty) {
  if (tileAt(tx, ty) !== 'o') return false;
  state.map[ty][tx] = ' ';
  activateComplementPower(tx, ty);
  return true;
}

function spawnVacuumedAntibody(tx, ty) {
  if (tileAt(tx, ty) !== '.') return false;
  const now = performance.now();
  if (now - lastVacuumStartSfxTime > 90) {
    playSoundEffect(SFX.antibodyVacuumStart, 0.24);
    lastVacuumStartSfxTime = now;
  }
  state.map[ty][tx] = ' ';
  state.vacuumedAntibodies.push({
    x: tx * TILE + TILE / 2,
    y: ty * TILE + TILE / 2,
    tx,
    ty,
    soundPlayed: false
  });
  return true;
}

function spawnVacuumedComplement(tx, ty) {
  if (tileAt(tx, ty) !== 'o') return false;
  state.map[ty][tx] = ' ';
  state.vacuumedComplements.push({
    x: tx * TILE + TILE / 2,
    y: ty * TILE + TILE / 2,
    tx,
    ty
  });
  return true;
}

function pullVacuumedPickup(pickup, speed, collectDistance, dt, onCollect) {
  const p = state.player;
  const dx = p.px - pickup.x;
  const dy = p.py - pickup.y;
  const distance = Math.hypot(dx, dy);
  if (distance <= collectDistance) {
    onCollect();
    return true;
  }
  const step = Math.min(distance, speed * dt);
  if (distance > 0) {
    pickup.x += (dx / distance) * step;
    pickup.y += (dy / distance) * step;
  }
  return false;
}

function maybePlayVacuumedAntibodySound(antibody) {
  if (antibody.soundPlayed) return;
  const p = state.player;
  const distance = Math.hypot(p.px - antibody.x, p.py - antibody.y);
  if (distance > ANTIBODY_TOUCH_SOUND_DISTANCE) return;
  antibody.soundPlayed = true;
  playSoundEffect(SFX.eatAntibody);
}

function vacuumAntibodies(dt) {
  if (!state.upgrades.antibodyVacuum) return;
  const p = state.player;
  const scanRange = Math.max(ANTIBODY_VACUUM_RANGE, COMPLEMENT_PICKUP_VACUUM_RANGE);
  const minTx = Math.max(1, Math.floor((p.px - scanRange) / TILE));
  const maxTx = Math.min(state.cols - 2, Math.floor((p.px + scanRange) / TILE));
  const minTy = Math.max(1, Math.floor((p.py - scanRange) / TILE));
  const maxTy = Math.min(state.rows - 2, Math.floor((p.py + scanRange) / TILE));

  for (let ty = minTy; ty <= maxTy; ty++) {
    for (let tx = minTx; tx <= maxTx; tx++) {
      const tile = tileAt(tx, ty);
      if (tile !== '.' && tile !== 'o') continue;
      const ax = tx * TILE + TILE / 2;
      const ay = ty * TILE + TILE / 2;
      const distance = Math.hypot(ax - p.px, ay - p.py);
      if (tile === '.' && distance <= ANTIBODY_VACUUM_RANGE) spawnVacuumedAntibody(tx, ty);
      if (tile === 'o' && distance <= COMPLEMENT_PICKUP_VACUUM_RANGE) spawnVacuumedComplement(tx, ty);
    }
  }

  for (let i = state.vacuumedAntibodies.length - 1; i >= 0; i--) {
    const antibody = state.vacuumedAntibodies[i];
    maybePlayVacuumedAntibodySound(antibody);
    if (pullVacuumedPickup(antibody, ANTIBODY_VACUUM_SPEED, ANTIBODY_COLLECT_DISTANCE, dt, () => {
      if (!antibody.soundPlayed) playSoundEffect(SFX.eatAntibody);
      finishAntibodyCollection(false);
    })) {
      state.vacuumedAntibodies.splice(i, 1);
    }
  }

  for (let i = state.vacuumedComplements.length - 1; i >= 0; i--) {
    const complement = state.vacuumedComplements[i];
    if (pullVacuumedPickup(complement, COMPLEMENT_PICKUP_VACUUM_SPEED, COMPLEMENT_PICKUP_COLLECT_DISTANCE, dt, () => activateComplementPower(complement.tx, complement.ty))) {
      state.vacuumedComplements.splice(i, 1);
    }
  }
}

function collectNearbyAntibodies(tx, ty) {
  let collected = 0;
  for (let y = ty - 1; y <= ty + 1; y++) {
    for (let x = tx - 1; x <= tx + 1; x++) {
      if (Math.abs(x - tx) + Math.abs(y - ty) > 1) continue;
      if (collectAntibodyAt(x, y)) collected++;
    }
  }
  return collected;
}

function collectCurrentTile() {
  const tx = Math.floor(state.player.px / TILE);
  const ty = Math.floor(state.player.py / TILE);
  const zone = zoneAt(state.zones, tx, ty);
  state.currentZone = zone ? zone.label : 'Tissue Conduit';

  const radius = RADIAL_MOVEMENT ? PICKUP_COLLECT_RADIUS : 1;
  const minTx = RADIAL_MOVEMENT ? Math.max(1, Math.floor((state.player.px - radius) / TILE)) : tx;
  const maxTx = RADIAL_MOVEMENT ? Math.min(state.cols - 2, Math.floor((state.player.px + radius) / TILE)) : tx;
  const minTy = RADIAL_MOVEMENT ? Math.max(1, Math.floor((state.player.py - radius) / TILE)) : ty;
  const maxTy = RADIAL_MOVEMENT ? Math.min(state.rows - 2, Math.floor((state.player.py + radius) / TILE)) : ty;

  for (let y = minTy; y <= maxTy; y++) {
    for (let x = minTx; x <= maxTx; x++) {
      if (RADIAL_MOVEMENT) {
        const center = tileCenter(x, y);
        if (Math.hypot(center.x - state.player.px, center.y - state.player.py) > radius) continue;
      }

      const tile = tileAt(x, y);
      if (tile === '.') {
        collectAntibodyAt(x, y);
        if (state.player.complementTicks > 0) collectNearbyAntibodies(x, y);
      } else if (tile === 'o') {
        collectComplementAt(x, y);
      } else if (tile === 'G' && state.collected >= state.totalAntibodies && !state.isTutorial) {
        playSoundEffect(SFX.levelClearGate, 0.86);
        stopAllSoundLoops();
        state.won = true;
        runState.textContent = 'Lymph gate cleared';
      }
    }
  }
}

function draw() {
  if (appMode === 'tutorialPrompt') {
    drawTutorialPrompt();
    return;
  }
  if (appMode === 'credits') {
    drawCreditsScreen();
    return;
  }
  if (appMode === 'resetConfirm') {
    drawResetConfirm();
    return;
  }
  if (appMode === 'error') {
    drawErrorScreen();
    return;
  }
  if (appMode === 'menu' || !state) {
    drawMenu();
    return;
  }
  drawBackground();
  drawFloorLayer();
  drawWallLayer();
  drawEnemyNest();
  drawPickupLayer();
  drawEnemies();
  drawVacuumedAntibodies();
  drawVacuumedComplements();
  drawPlayer();
  drawCanvasHud();
  drawMusicButton();
  drawPauseButton();
  drawTutorialOverlay();
  drawResultBanner();
  if (debug) drawDebug();
}

function textureReady() {
  return tissueTexture.complete && tissueTexture.naturalWidth > 0;
}

function drawImageCover(image, dx, dy, dw, dh, alpha = 1) {
  const imageAspect = image.naturalWidth / image.naturalHeight;
  const targetAspect = dw / dh;
  let sx = 0;
  let sy = 0;
  let sw = image.naturalWidth;
  let sh = image.naturalHeight;
  if (imageAspect > targetAspect) {
    sw = image.naturalHeight * targetAspect;
    sx = (image.naturalWidth - sw) / 2;
  } else {
    sh = image.naturalWidth / targetAspect;
    sy = (image.naturalHeight - sh) / 2;
  }
  ctx.save();
  ctx.globalAlpha = alpha;
  ctx.drawImage(image, sx, sy, sw, sh, dx, dy, dw, dh);
  ctx.restore();
}

function drawTextureCover(alpha = 1) {
  if (!textureReady()) return false;
  const imageAspect = tissueTexture.naturalWidth / tissueTexture.naturalHeight;
  const canvasAspect = canvas.width / canvas.height;
  let sx = 0;
  let sy = 0;
  let sw = tissueTexture.naturalWidth;
  let sh = tissueTexture.naturalHeight;
  if (imageAspect > canvasAspect) {
    sw = tissueTexture.naturalHeight * canvasAspect;
    sx = (tissueTexture.naturalWidth - sw) / 2;
  } else {
    sh = tissueTexture.naturalWidth / canvasAspect;
    sy = (tissueTexture.naturalHeight - sh) / 2;
  }

  ctx.save();
  ctx.globalAlpha = alpha;
  ctx.drawImage(tissueTexture, sx, sy, sw, sh, 0, 0, canvas.width, canvas.height);
  ctx.restore();
  return true;
}

function drawBackground() {
  ctx.fillStyle = '#050102';
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  if (drawTextureCover(0.24)) {
    ctx.fillStyle = 'rgba(7, 0, 3, 0.76)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    return;
  }
  const gradient = ctx.createRadialGradient(canvas.width / 2, canvas.height / 2, 40, canvas.width / 2, canvas.height / 2, canvas.width * 0.75);
  gradient.addColorStop(0, '#2a100c');
  gradient.addColorStop(0.55, '#130b09');
  gradient.addColorStop(1, '#070404');
  ctx.fillStyle = gradient;
  ctx.fillRect(0, 0, canvas.width, canvas.height);
}

function drawTileImage(index, dx, dy) {
  if (!tileSheet.complete || tileSheet.naturalWidth <= 0) return false;
  const sourceW = tileSheet.naturalWidth / 4;
  const sourceH = tileSheet.naturalHeight / 2;
  const sx = (index % 4) * sourceW;
  const sy = Math.floor(index / 4) * sourceH;
  ctx.drawImage(tileSheet, sx, sy, sourceW, sourceH, dx, dy, TILE, TILE);
  return true;
}

function tileNoise(x, y, salt = 0) {
  let n = x * 374761393 + y * 668265263 + (salt + generationSeed) * 1442695041;
  n = (n ^ (n >> 13)) * 1274126177;
  return ((n ^ (n >> 16)) >>> 0) / 4294967295;
}

function isWallTile(x, y) {
  return tileAt(x, y) === '#';
}

function isWalkableTile(x, y) {
  return !isWallTile(x, y);
}

function traceTileMask(predicate) {
  ctx.beginPath();
  for (let y = 0; y < state.rows; y++) {
    for (let x = 0; x < state.cols; x++) {
      if (predicate(x, y)) ctx.rect(x * TILE, y * TILE, TILE, TILE);
    }
  }
}

function drawMaskedTexture(predicate, alpha, tint, blendMode = 'source-over') {
  ctx.save();
  traceTileMask(predicate);
  ctx.clip();
  if (!drawTextureCover(alpha)) {
    ctx.fillStyle = tint;
    ctx.fillRect(0, 0, canvas.width, canvas.height);
  }
  ctx.globalCompositeOperation = blendMode;
  ctx.fillStyle = tint;
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.restore();
}

function drawFloorTexture(x, y, px, py, tile, zone) {
  const n = tileNoise(x, y, 21);
  ctx.fillStyle = `rgba(0, 0, 0, ${0.08 + n * 0.1})`;
  ctx.fillRect(px, py, TILE, TILE);

  if (tile === ' ') {
    ctx.fillStyle = 'rgba(0, 0, 0, 0.12)';
    ctx.fillRect(px, py, TILE, TILE);
  }
  if (zone && ((x + y) % 7 === 0)) {
    ctx.fillStyle = zoneAccentColor(zone);
    ctx.fillRect(px + 9, py + 9, TILE - 18, TILE - 18);
  }
}

function zoneFloorColor(zone) {
  if (!zone) return 'rgba(8, 1, 3, 0.86)';
  if (zone.type === 'marrow') return 'rgba(16, 3, 5, 0.84)';
  if (zone.type === 'capillary') return 'rgba(20, 2, 4, 0.82)';
  if (zone.type === 'complement') return 'rgba(20, 8, 2, 0.82)';
  if (zone.type === 'infection') return 'rgba(17, 0, 9, 0.86)';
  if (zone.type === 'necrotic') return 'rgba(8, 2, 11, 0.84)';
  if (zone.type === 'lymph') return 'rgba(2, 10, 7, 0.84)';
  return 'rgba(8, 1, 3, 0.86)';
}

function zoneAccentColor(zone) {
  if (!zone) return 'rgba(255, 96, 104, 0.12)';
  if (zone.type === 'marrow') return 'rgba(255, 124, 130, 0.12)';
  if (zone.type === 'capillary') return 'rgba(255, 42, 54, 0.13)';
  if (zone.type === 'complement') return 'rgba(255, 166, 55, 0.16)';
  if (zone.type === 'infection') return 'rgba(255, 50, 124, 0.18)';
  if (zone.type === 'necrotic') return 'rgba(174, 86, 255, 0.11)';
  if (zone.type === 'lymph') return 'rgba(105, 255, 171, 0.12)';
  return 'rgba(255, 96, 104, 0.12)';
}

function drawFloorLayer() {
  drawMaskedTexture(
    (x, y) => !isWallTile(x, y),
    0.72,
    'rgba(1, 0, 1, 0.72)',
    'multiply'
  );

  ctx.save();
  traceTileMask((x, y) => !isWallTile(x, y));
  ctx.clip();
  const g = ctx.createRadialGradient(canvas.width * 0.5, canvas.height * 0.45, 20, canvas.width * 0.5, canvas.height * 0.5, canvas.width * 0.7);
  g.addColorStop(0, 'rgba(120, 13, 24, 0.12)');
  g.addColorStop(0.65, 'rgba(17, 0, 4, 0.28)');
  g.addColorStop(1, 'rgba(0, 0, 0, 0.72)');
  ctx.fillStyle = g;
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.restore();

  for (let y = 0; y < state.rows; y++) {
    for (let x = 0; x < state.cols; x++) {
      const tile = state.map[y][x];
      if (tile === '#') continue;
      drawFloorTexture(x, y, x * TILE, y * TILE, tile, zoneAt(state.zones, x, y));
    }
  }
}

function wallEdgeBasePoint(px, py, side, t, offset) {
  if (side === 'top') return { x: px + t * TILE, y: py + 2 + offset };
  if (side === 'right') return { x: px + TILE - 2 - offset, y: py + t * TILE };
  if (side === 'bottom') return { x: px + (1 - t) * TILE, y: py + TILE - 2 - offset };
  return { x: px + 2 + offset, y: py + (1 - t) * TILE };
}

function sideNormal(side) {
  if (side === 'top') return { x: 0, y: -1 };
  if (side === 'right') return { x: 1, y: 0 };
  if (side === 'bottom') return { x: 0, y: 1 };
  return { x: -1, y: 0 };
}

function drawNoisyEdgeStroke(x, y, px, py, side, strokeStyle, lineWidth, salt, inset = 0) {
  const sideSalt = side === 'top' ? 11 : side === 'right' ? 23 : side === 'bottom' ? 37 : 51;
  ctx.strokeStyle = strokeStyle;
  ctx.lineWidth = lineWidth;
  ctx.lineCap = 'round';
  ctx.lineJoin = 'round';
  ctx.beginPath();
  for (let i = 0; i <= 8; i++) {
    const t = i / 8;
    const n = tileNoise(x * 9 + i, y * 7 + i * 3, salt + sideSalt) - 0.5;
    const ripple = Math.sin((t * Math.PI * 2) + tileNoise(x, y, salt + sideSalt + 5) * Math.PI) * 1.6;
    const point = wallEdgeBasePoint(px, py, side, t, inset + n * 7.5 + ripple);
    if (i === 0) ctx.moveTo(point.x, point.y);
    else ctx.lineTo(point.x, point.y);
  }
  ctx.stroke();
}

function drawCellularEdgePods(x, y, px, py, side) {
  const normal = sideNormal(side);
  const sideSalt = side === 'top' ? 101 : side === 'right' ? 131 : side === 'bottom' ? 163 : 197;
  for (let i = 0; i < 4; i++) {
    const n = tileNoise(x * 5 + i, y * 11 - i, sideSalt);
    if (n < 0.22) continue;
    const t = (i + 0.5 + (tileNoise(x, y, sideSalt + i) - 0.5) * 0.28) / 4;
    const base = wallEdgeBasePoint(px, py, side, clamp(t, 0.08, 0.92), -1.5);
    const radius = 3.2 + n * 5.4;
    const cx = base.x + normal.x * (radius * 0.38 + tileNoise(x, y, sideSalt + 40 + i) * 2.8);
    const cy = base.y + normal.y * (radius * 0.38 + tileNoise(x, y, sideSalt + 50 + i) * 2.8);
    ctx.save();
    ctx.translate(cx, cy);
    ctx.rotate(tileNoise(x, y, sideSalt + 60 + i) * Math.PI);
    ctx.fillStyle = `rgba(${34 + n * 30}, ${1 + n * 6}, ${8 + n * 12}, 0.78)`;
    ctx.strokeStyle = 'rgba(255, 150, 160, 0.36)';
    ctx.lineWidth = 1.4;
    ctx.beginPath();
    ctx.ellipse(0, 0, radius * (0.75 + n * 0.35), radius * (0.42 + tileNoise(x, y, sideSalt + 70 + i) * 0.38), 0, 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();
    ctx.restore();
  }
}

function drawWallEdge(x, y, px, py, side) {
  drawCellularEdgePods(x, y, px, py, side);
  drawNoisyEdgeStroke(x, y, px, py, side, 'rgba(14, 0, 5, 0.92)', 6.4, 70);
  drawNoisyEdgeStroke(x, y, px, py, side, 'rgba(255, 158, 166, 0.64)', 2.2, 91, 0.4);
  drawNoisyEdgeStroke(x, y, px, py, side, 'rgba(80, 4, 18, 0.46)', 1.1, 112, -1.2);
}

function drawWallLayer() {
  drawMaskedTexture(
    (x, y) => isWallTile(x, y),
    1,
    'rgba(110, 5, 18, 0.16)',
    'screen'
  );

  ctx.save();
  traceTileMask((x, y) => isWallTile(x, y));
  ctx.clip();
  ctx.fillStyle = 'rgba(255, 115, 132, 0.12)';
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  const g = ctx.createRadialGradient(canvas.width * 0.45, canvas.height * 0.35, 30, canvas.width * 0.55, canvas.height * 0.5, canvas.width * 0.72);
  g.addColorStop(0, 'rgba(255, 205, 205, 0.15)');
  g.addColorStop(0.52, 'rgba(255, 60, 78, 0.06)');
  g.addColorStop(1, 'rgba(24, 0, 6, 0.28)');
  ctx.fillStyle = g;
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.restore();

  for (let y = 0; y < state.rows; y++) {
    for (let x = 0; x < state.cols; x++) {
      if (!isWallTile(x, y)) continue;
      const px = x * TILE;
      const py = y * TILE;
      if (isWalkableTile(x, y - 1)) drawWallEdge(x, y, px, py, 'top');
      if (isWalkableTile(x + 1, y)) drawWallEdge(x, y, px, py, 'right');
      if (isWalkableTile(x, y + 1)) drawWallEdge(x, y, px, py, 'bottom');
      if (isWalkableTile(x - 1, y)) drawWallEdge(x, y, px, py, 'left');
    }
  }
}


function drawEnemyNest() {
  const nest = state.enemyNest;
  if (!nest) return;
  const pulse = 0.5 + Math.sin(state.player.animTime * 5.5) * 0.5;
  const clean = state.infectionNeutralized;
  const cleanseProgress = state.cleanseTicks > 0 ? 1 - state.cleanseTicks / NEST_CLEANSE_DURATION : (clean ? 1 : 0);
  const cx = nest.cx * TILE + TILE / 2;
  const cy = nest.cy * TILE + TILE / 2;
  const radius = Math.max(nest.w, nest.h) * TILE * (0.72 + cleanseProgress * 0.46);

  ctx.save();
  for (let y = nest.y - 1; y <= nest.y + nest.h; y++) {
    for (let x = nest.x - 1; x <= nest.x + nest.w; x++) {
      if (!isWalkableTile(x, y)) continue;
      const px = x * TILE;
      const py = y * TILE;
      ctx.fillStyle = clean
        ? `rgba(255, 207, 180, ${0.10 + cleanseProgress * 0.20})`
        : `rgba(97, 0, 44, ${0.18 + pulse * 0.10})`;
      ctx.fillRect(px + 2, py + 2, TILE - 4, TILE - 4);
    }
  }

  const aura = ctx.createRadialGradient(cx, cy, 4, cx, cy, radius);
  if (clean) {
    aura.addColorStop(0, `rgba(255, 244, 184, ${0.42 + cleanseProgress * 0.24})`);
    aura.addColorStop(0.38, `rgba(255, 149, 106, ${0.20 + cleanseProgress * 0.16})`);
    aura.addColorStop(1, 'rgba(255, 218, 168, 0)');
  } else {
    aura.addColorStop(0, `rgba(255, 32, 112, ${0.20 + pulse * 0.12})`);
    aura.addColorStop(0.55, 'rgba(73, 0, 40, 0.12)');
    aura.addColorStop(1, 'rgba(73, 0, 40, 0)');
  }
  ctx.fillStyle = aura;
  ctx.beginPath();
  ctx.arc(cx, cy, radius, 0, Math.PI * 2);
  ctx.fill();

  if (state.cleanseTicks > 0) {
    ctx.strokeStyle = `rgba(255, 241, 184, ${0.82 * (1 - cleanseProgress * 0.55)})`;
    ctx.lineWidth = 3.2;
    ctx.beginPath();
    ctx.arc(cx, cy, radius * (0.25 + cleanseProgress * 0.75), 0, Math.PI * 2);
    ctx.stroke();
  }

  for (const enemy of state.enemies) {
    const sx = enemy.spawnTx * TILE + TILE / 2;
    const sy = enemy.spawnTy * TILE + TILE / 2;
    ctx.strokeStyle = clean ? 'rgba(255, 235, 190, 0.78)' : `rgba(255, 84, 151, ${0.62 + pulse * 0.28})`;
    ctx.fillStyle = clean ? 'rgba(255, 221, 174, 0.16)' : 'rgba(34, 0, 21, 0.72)';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.arc(sx, sy, TILE * (0.22 + pulse * 0.04), 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();
    ctx.beginPath();
    ctx.arc(sx, sy, TILE * (0.34 + pulse * 0.08), 0, Math.PI * 2);
    ctx.stroke();
  }
  ctx.restore();
}

function drawPickupLayer() {
  for (let y = 0; y < state.rows; y++) {
    for (let x = 0; x < state.cols; x++) {
      const tile = state.map[y][x];
      const px = x * TILE;
      const py = y * TILE;
      if (tile === '.') drawAntibody(px + TILE / 2, py + TILE / 2, 4);
      if (tile === 'o') drawComplement(px + TILE / 2, py + TILE / 2, 10);
      if (tile === 'G') drawGate(px, py);
    }
  }
}


function prepareEnemyFrames() {
  if (enemyFrames || !enemySheet.complete || enemySheet.naturalWidth <= 0) return enemyFrames;
  const frameWidth = Math.floor(enemySheet.naturalWidth / 4);
  const frameHeight = enemySheet.naturalHeight;
  enemyFrames = [];
  for (let frame = 0; frame < 4; frame++) {
    const frameCanvas = document.createElement('canvas');
    frameCanvas.width = frameWidth;
    frameCanvas.height = frameHeight;
    const frameCtx = frameCanvas.getContext('2d');
    frameCtx.drawImage(enemySheet, frame * frameWidth, 0, frameWidth, frameHeight, 0, 0, frameWidth, frameHeight);
    const image = frameCtx.getImageData(0, 0, frameWidth, frameHeight);
    for (let i = 0; i < image.data.length; i += 4) {
      const r = image.data[i];
      const g = image.data[i + 1];
      const b = image.data[i + 2];
      const greenKey = g > 145 && r < 115 && b < 125 && g > r * 1.35 && g > b * 1.35;
      if (greenKey) image.data[i + 3] = 0;
    }
    frameCtx.putImageData(image, 0, 0);
    enemyFrames.push(frameCanvas);
  }
  return enemyFrames;
}

function drawEnemySprite(enemy, radius, dying) {
  const frames = prepareEnemyFrames();
  const archetype = archetypeById(enemy.archetype);
  const frame = frames?.[archetype.frame];
  if (!frame) return false;
  const size = radius * (dying ? 3.0 : 2.75);
  ctx.drawImage(frame, -size / 2, -size / 2, size, size);
  return true;
}

function drawEnemyBlobPath(enemy, radius, salt = 0) {
  const idSalt = Number(String(enemy.id).replace(/\D/g, '')) || 1;
  ctx.beginPath();
  for (let i = 0; i < 14; i++) {
    const angle = (i / 14) * Math.PI * 2;
    const n = tileNoise(idSalt * 17 + i, Math.floor(enemy.x / TILE) + Math.floor(enemy.y / TILE), salt + i * 9);
    const r = radius * (0.72 + n * 0.42);
    const x = Math.cos(angle) * r;
    const y = Math.sin(angle) * r * (0.82 + tileNoise(idSalt, i, salt + 60) * 0.24);
    if (i === 0) ctx.moveTo(x, y);
    else ctx.lineTo(x, y);
  }
  ctx.closePath();
}

function drawEnemy(enemy) {
  if (enemy.state === 'respawning') return;
  const dying = enemy.state === 'dying';
  const remaining = dying ? enemy.deathTicks / ENEMY_DEATH_DURATION : 1;
  const elapsed = dying ? 1 - remaining : 0;
  const shrinkT = dying ? clamp((elapsed * ENEMY_DEATH_DURATION - ENEMY_DEATH_EXPAND_DURATION) / ENEMY_DEATH_SHRINK_DURATION, 0, 1) : 0;
  const expandT = dying ? clamp((elapsed * ENEMY_DEATH_DURATION) / ENEMY_DEATH_EXPAND_DURATION, 0, 1) : 0;
  const expandEase = 1 + 0.18 * Math.sin(expandT * Math.PI);
  const deathScale = dying
    ? (shrinkT > 0 ? ENEMY_DEATH_EXPAND_SCALE * (1 - shrinkT) : 1 + (ENEMY_DEATH_EXPAND_SCALE - 1) * expandT * expandEase)
    : 1;
  const alpha = dying ? Math.max(0, 1 - shrinkT) : 1;
  const pulse = 0.5 + Math.sin(state.player.animTime * 7 + enemy.x * 0.03) * 0.5;
  const drawX = dying ? enemy.deathX : enemy.x;
  const drawY = dying ? enemy.deathY : enemy.y;
  const facing = Math.atan2(enemy.dir?.y || 0, enemy.dir?.x || 1);

  ctx.save();
  ctx.translate(drawX, drawY);
  ctx.rotate(facing + (dying ? elapsed * ENEMY_DEATH_SPIN : Math.sin(state.player.animTime * 2.4 + enemy.x) * 0.08));
  ctx.scale(deathScale * (1 + pulse * 0.035), deathScale * (0.96 - pulse * 0.025));
  ctx.globalAlpha = alpha;
  ctx.shadowColor = dying ? 'rgba(255, 140, 88, 0.62)' : 'rgba(166, 38, 112, 0.38)';
  ctx.shadowBlur = dying ? 18 : 9;

  const radius = enemyRadius(enemy);
  if (!drawEnemySprite(enemy, radius, dying)) {
    const archetype = archetypeById(enemy.archetype);
    const g = ctx.createRadialGradient(-radius * 0.18, -radius * 0.14, 2, 0, 0, radius * 1.08);
    g.addColorStop(0, dying ? 'rgba(255, 213, 144, 0.96)' : archetype.accent);
    g.addColorStop(0.52, dying ? 'rgba(212, 63, 35, 0.82)' : archetype.color);
    g.addColorStop(1, dying ? 'rgba(90, 0, 8, 0.18)' : 'rgba(10, 0, 9, 0.96)');
    ctx.fillStyle = g;
    ctx.strokeStyle = dying ? 'rgba(255, 214, 154, 0.72)' : archetype.accent;
    ctx.lineWidth = 1.8;
    drawEnemyBlobPath(enemy, radius, dying ? 411 : 307);
    ctx.fill();
    ctx.stroke();

    ctx.shadowBlur = 0;
    ctx.fillStyle = dying ? 'rgba(255, 236, 180, 0.62)' : 'rgba(24, 160, 94, 0.72)';
    drawEnemyBlobPath(enemy, radius * 0.34, dying ? 503 : 389);
    ctx.fill();

    ctx.fillStyle = dying ? 'rgba(255, 255, 225, 0.72)' : 'rgba(245, 122, 178, 0.68)';
    for (let i = 0; i < 4; i++) {
      const a = i * Math.PI * 0.5 + pulse * 0.4;
      ctx.beginPath();
      ctx.arc(Math.cos(a) * radius * 0.38, Math.sin(a) * radius * 0.34, dying ? 2.6 : 1.9, 0, Math.PI * 2);
      ctx.fill();
    }
  }

  ctx.restore();
}

function drawEnemies() {
  for (const enemy of state.enemies) drawEnemy(enemy);
}

function drawVacuumedAntibodies() {
  for (const antibody of state.vacuumedAntibodies) drawAntibody(antibody.x, antibody.y, 4);
}

function drawVacuumedComplements() {
  for (const complement of state.vacuumedComplements) drawComplement(complement.x, complement.y, 10);
}

function drawAntibody(cx, cy, r) {
  ctx.save();
  ctx.strokeStyle = '#f8ead3';
  ctx.lineWidth = 2;
  ctx.shadowColor = '#ffb43a';
  ctx.shadowBlur = 6;
  ctx.beginPath();
  ctx.moveTo(cx, cy + r);
  ctx.lineTo(cx, cy - r);
  ctx.moveTo(cx, cy - 1);
  ctx.lineTo(cx - r, cy - r - 3);
  ctx.moveTo(cx, cy - 1);
  ctx.lineTo(cx + r, cy - r - 3);
  ctx.stroke();
  ctx.restore();
}

function drawComplement(cx, cy, r) {
  const g = ctx.createRadialGradient(cx, cy, 1, cx, cy, r);
  g.addColorStop(0, '#fff3c0');
  g.addColorStop(0.45, '#ff9d20');
  g.addColorStop(1, 'rgba(212, 50, 18, 0.08)');
  ctx.fillStyle = g;
  ctx.beginPath();
  ctx.arc(cx, cy, r, 0, Math.PI * 2);
  ctx.fill();
}

function drawGate(px, py) {
  ctx.fillStyle = state.collected >= state.totalAntibodies ? '#214d32' : '#271b18';
  ctx.fillRect(px + 4, py + 4, TILE - 8, TILE - 8);
  ctx.strokeStyle = state.collected >= state.totalAntibodies ? '#9eff7b' : '#6b3824';
  ctx.lineWidth = 2;
  ctx.strokeRect(px + 6, py + 6, TILE - 12, TILE - 12);
}

function preparePlayerFrames() {
  if (playerFrames || !sprite.complete || sprite.naturalWidth <= 0) return playerFrames;

  const frameWidth = Math.floor(sprite.naturalWidth / 4);
  const frameHeight = sprite.naturalHeight;
  playerFrames = [];
  for (let frame = 0; frame < 4; frame++) {
    const frameCanvas = document.createElement('canvas');
    frameCanvas.width = frameWidth;
    frameCanvas.height = frameHeight;
    const frameCtx = frameCanvas.getContext('2d');
    frameCtx.drawImage(sprite, frame * frameWidth, 0, frameWidth, frameHeight, 0, 0, frameWidth, frameHeight);

    const image = frameCtx.getImageData(0, 0, frameWidth, frameHeight);
    for (let i = 0; i < image.data.length; i += 4) {
      const r = image.data[i];
      const g = image.data[i + 1];
      const b = image.data[i + 2];
      const maxChannel = Math.max(r, g, b);
      const warmGlow = r > 45 && g > 22 && r > b * 1.25;
      if (maxChannel < 34 || (maxChannel < 54 && !warmGlow)) image.data[i + 3] = 0;
    }
    frameCtx.putImageData(image, 0, 0);
    playerFrames.push(frameCanvas);
  }
  return playerFrames;
}

function playerAnimationState(player) {
  const framePhase = Math.floor(player.animTime / PLAYER_FRAME_TIME) % 2;
  if (player.ramTicks > 0) {
    const t = player.ramTicks / PSEUDOPOD_RAM_DURATION;
    return {
      frame: 3,
      scaleX: 1 + 0.18 * t,
      scaleY: 1 - 0.12 * t
    };
  }

  if (player.complementTicks > 0) {
    const pulse = Math.sin((player.animTime / PLAYER_FRAME_TIME) * Math.PI);
    return {
      frame: framePhase === 0 ? 0 : 3,
      scaleX: 1 + 0.1 * pulse,
      scaleY: 1 - 0.07 * pulse
    };
  }

  if (player.moving) {
    const pulse = Math.sin((player.animTime / PLAYER_FRAME_TIME) * Math.PI);
    return {
      frame: framePhase === 0 ? 0 : 1,
      scaleX: 1 + 0.08 * pulse,
      scaleY: 1 - 0.055 * pulse
    };
  }

  const idlePulse = Math.sin((player.animTime / IDLE_PULSE_TIME) * Math.PI * 2);
  return {
    frame: 0,
    scaleX: 1 + 0.025 * idlePulse,
    scaleY: 1 - 0.02 * idlePulse
  };
}

function shouldDrawCanvasHud() {
  return Boolean(document.fullscreenElement) || window.matchMedia('(max-width: 860px)').matches;
}

function drawCanvasHud() {
  if (!shouldDrawCanvasHud()) return;
  const p = state.player;
  const pad = 10;
  const panelW = Math.min(canvas.width - pad * 2, 270);
  const panelH = 54;
  ctx.save();
  ctx.fillStyle = 'rgba(5, 0, 2, 0.58)';
  ctx.fillRect(pad, pad, panelW, panelH);
  ctx.strokeStyle = 'rgba(255, 156, 92, 0.32)';
  ctx.lineWidth = 1;
  ctx.strokeRect(pad + 0.5, pad + 0.5, panelW - 1, panelH - 1);
  ctx.fillStyle = '#fff0d2';
  ctx.font = 'bold 13px Inter, ui-sans-serif, system-ui, sans-serif';
  ctx.fillText(`${state.collected}/${state.totalAntibodies}`, pad + 10, pad + 17);
  ctx.fillStyle = p.complementTicks > 0 ? '#ffcf55' : '#c9aa8e';
  ctx.font = '11px Inter, ui-sans-serif, system-ui, sans-serif';
  const activeEnemies = state.enemies.filter(enemy => enemy.state === 'active' || enemy.state === 'knockback').length;
  const mechanic = state.dead ? 'Membrane breached' : (state.infectionNeutralized ? 'Nest cleansed' : (p.ramTicks > 0 ? 'Pseudopod Ram' : (p.ramArmed ? 'Ram armed' : 'Ram spent')));
  ctx.fillText(`${mechanic}  ${activeEnemies}/${state.enemies.length}`, pad + 82, pad + 17);
  ctx.fillStyle = '#c9aa8e';
  ctx.fillText(`L${state.depth} ${state.currentZone}`, pad + 10, pad + 34);
  ctx.fillStyle = '#9f806a';
  ctx.font = '10px ui-monospace, SFMono-Regular, Menlo, Consolas, monospace';
  ctx.fillText(state.runSeed, pad + 10, pad + 48);
  ctx.fillStyle = '#ff684f';
  ctx.fillRect(pad + panelW - 74, pad + 40, 62 * (state.fever / 100), 4);
  ctx.strokeStyle = 'rgba(255, 180, 116, 0.42)';
  ctx.strokeRect(pad + panelW - 74.5, pad + 39.5, 63, 5);
  ctx.restore();
}


function tutorialCompleteButtonBounds() {
  const panelW = Math.min(canvas.width - 22, 500);
  const panelH = 292;
  const x = (canvas.width - panelW) / 2;
  const y = Math.max(18, (canvas.height - panelH) / 2);
  return [
    { x: x + 18, y: y + 176, w: panelW - 36, h: 58, action: () => completeTutorialAndStartRun() },
    { x: x + 18, y: y + 242, w: panelW - 36, h: 42, action: () => startTutorial(state.tutorialReturnSeed) }
  ];
}

function tutorialButton(label, x, y, w, h, action, sublabel = '') {
  state.tutorialButtons.push({ x, y, w, h, action });
  ctx.fillStyle = 'rgba(18, 4, 5, 0.86)';
  ctx.fillRect(x, y, w, h);
  ctx.strokeStyle = 'rgba(255, 226, 184, 0.76)';
  ctx.lineWidth = 1.6;
  ctx.strokeRect(x + 0.5, y + 0.5, w - 1, h - 1);
  ctx.textAlign = 'center';
  ctx.fillStyle = '#fff0d2';
  ctx.font = 'bold 20px Inter, ui-sans-serif, system-ui, sans-serif';
  ctx.fillText(label, x + w / 2, y + 29);
  if (sublabel) {
    ctx.fillStyle = '#c9aa8e';
    ctx.font = '13px Inter, ui-sans-serif, system-ui, sans-serif';
    ctx.fillText(sublabel, x + w / 2, y + 48);
  }
}

function drawTutorialOverlay() {
  if (!state?.isTutorial) return;
  state.tutorialButtons = [];
  const complete = state.tutorialComplete;
  const panelW = Math.min(canvas.width - 22, complete ? 500 : 430);
  const panelH = complete ? 292 : 152;
  const x = (canvas.width - panelW) / 2;
  const y = complete ? Math.max(18, (canvas.height - panelH) / 2) : Math.max(12, canvas.height - panelH - 18);
  ctx.save();
  ctx.fillStyle = complete ? 'rgba(5, 0, 2, 0.86)' : 'rgba(5, 0, 2, 0.76)';
  ctx.fillRect(x, y, panelW, panelH);
  ctx.strokeStyle = 'rgba(255, 156, 92, 0.54)';
  ctx.lineWidth = 1.6;
  ctx.strokeRect(x + 0.5, y + 0.5, panelW - 1, panelH - 1);
  ctx.textAlign = 'left';
  ctx.fillStyle = '#ffb35f';
  ctx.font = 'bold 15px Inter, ui-sans-serif, system-ui, sans-serif';
  ctx.fillText('PSEUDOPOD RAM TRAINING', x + 18, y + 32);
  ctx.fillStyle = '#fff0d2';
  ctx.font = 'bold 24px Inter, ui-sans-serif, system-ui, sans-serif';
  ctx.fillText(complete ? 'Chain reaction complete' : (state.tutorialChainStarted ? 'Observe the chain' : 'Dash into the first germ'), x + 18, y + 66);
  ctx.fillStyle = '#d5b69e';
  ctx.font = '16px Inter, ui-sans-serif, system-ui, sans-serif';
  if (complete) {
    ctx.fillText('Ram launches enemies forward.', x + 18, y + 100);
    ctx.fillText('Wall or enemy impact kills the launched germ.', x + 18, y + 124);
    ctx.fillText('A launched germ can launch the next one.', x + 18, y + 148);
    const [continueButton, repeatButton] = tutorialCompleteButtonBounds();
    const continueLabel = state.tutorialReturnMode === 'menu' ? 'Back to Menu' : 'Continue';
    const continueSublabel = state.tutorialReturnMode === 'menu' ? 'Training complete' : 'Start the generated run';
    tutorialButton(continueLabel, continueButton.x, continueButton.y, continueButton.w, continueButton.h, continueButton.action, continueSublabel);
    tutorialButton('Repeat', repeatButton.x, repeatButton.y, repeatButton.w, repeatButton.h, repeatButton.action, 'Practice again');
  } else if (state.tutorialChainStarted) {
    ctx.fillText('The first knocked germ should drive through the line.', x + 18, y + 98);
    ctx.fillText('Let it finish, then continue into the real run.', x + 18, y + 122);
  } else {
    ctx.fillText('Move right from rest to dash into the first germ.', x + 18, y + 98);
    ctx.fillText('Release input to rearm if the dash is spent.', x + 18, y + 122);
  }
  ctx.restore();
}

function maybeHandleTutorialPointer(event) {
  if (!state?.isTutorial || !state.tutorialComplete) return false;
  const point = canvasPoint(event);
  const buttons = (state.tutorialButtons && state.tutorialButtons.length) ? state.tutorialButtons : tutorialCompleteButtonBounds();
  const hit = buttons.find(button => pointInExpandedRect(point, button, 22));
  if (!hit) return false;
  playSoundEffect(SFX.uiSelect, 0.42);
  hit.action();
  event.preventDefault();
  return true;
}

function updateTutorialState(dt) {
  if (!state?.isTutorial) return;
  const affected = state.enemies.filter(enemy => enemy.rammed || enemy.state === 'knockback' || enemy.state === 'dying' || enemy.state === 'respawning').length;
  if (affected > 0) state.tutorialChainStarted = true;
  if (state.tutorialChainStarted) state.tutorialTicks += dt;
  if (!state.tutorialComplete && state.tutorialChainStarted && (affected >= Math.min(3, state.enemies.length) || state.tutorialTicks > 1.4)) {
    state.tutorialComplete = true;
    heldKeys.clear();
    resetJoystick();
  }
}

function drawMusicButton() {
  if (!state) return;
  const bounds = musicButtonBounds();
  state.musicButtonBounds = bounds;
  const cx = bounds.x + bounds.w / 2;
  const cy = bounds.y + bounds.h / 2;
  const scale = bounds.w / 34;
  ctx.save();
  ctx.fillStyle = musicPlayer.disabled ? 'rgba(60, 14, 18, 0.78)' : 'rgba(5, 0, 2, 0.66)';
  ctx.fillRect(bounds.x, bounds.y, bounds.w, bounds.h);
  ctx.strokeStyle = musicPlayer.disabled ? 'rgba(255, 116, 110, 0.70)' : 'rgba(255, 156, 92, 0.52)';
  ctx.lineWidth = 1.6;
  ctx.strokeRect(bounds.x + 0.5, bounds.y + 0.5, bounds.w - 1, bounds.h - 1);
  ctx.translate(cx - 17 * scale, cy - 17 * scale);
  ctx.scale(scale, scale);
  ctx.fillStyle = '#fff0d2';
  ctx.beginPath();
  ctx.moveTo(9, 13);
  ctx.lineTo(14, 13);
  ctx.lineTo(21, 8);
  ctx.lineTo(21, 26);
  ctx.lineTo(14, 21);
  ctx.lineTo(9, 21);
  ctx.closePath();
  ctx.fill();
  ctx.strokeStyle = '#fff0d2';
  ctx.lineWidth = 1.8;
  ctx.beginPath();
  if (musicPlayer.disabled) {
    ctx.moveTo(8, 8);
    ctx.lineTo(26, 26);
  } else {
    ctx.arc(22, 17, 5, -0.65, 0.65);
    ctx.moveTo(26, 11);
    ctx.arc(22, 17, 10, -0.55, 0.55);
  }
  ctx.stroke();
  ctx.restore();
}

function drawPauseButton() {
  if (state.dead || state.won) {
    state.pauseButtonBounds = null;
    return;
  }
  const bounds = pauseButtonBounds();
  state.pauseButtonBounds = bounds;

  ctx.save();
  if (state.paused) {
    ctx.fillStyle = 'rgba(5, 0, 2, 0.52)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    const buttons = pauseMenuButtonBounds();
    state.pauseMenuButtons = buttons;
    const panelW = buttons[0].w + 36;
    const panelH = 256;
    const x = (canvas.width - panelW) / 2;
    const y = buttons[0].y - 70;
    ctx.fillStyle = 'rgba(18, 4, 5, 0.88)';
    ctx.fillRect(x, y, panelW, panelH);
    ctx.strokeStyle = 'rgba(255, 226, 184, 0.62)';
    ctx.lineWidth = 1.5;
    ctx.strokeRect(x + 0.5, y + 0.5, panelW - 1, panelH - 1);
    ctx.textAlign = 'center';
    ctx.fillStyle = '#fff0d2';
    ctx.font = 'bold 24px Inter, ui-sans-serif, system-ui, sans-serif';
    ctx.fillText('Paused', canvas.width / 2, y + 36);
    ctx.fillStyle = '#d5b69e';
    ctx.font = '12px Inter, ui-sans-serif, system-ui, sans-serif';
    ctx.fillText('Resume, adjust music, or exit to the main menu.', canvas.width / 2, y + 58);
    for (const button of buttons) {
      ctx.fillStyle = button.id === 'menu' ? 'rgba(120, 22, 20, 0.42)' : 'rgba(255, 225, 183, 0.12)';
      ctx.fillRect(button.x, button.y, button.w, button.h);
      ctx.strokeStyle = button.id === 'menu' ? 'rgba(255, 116, 110, 0.72)' : 'rgba(255, 226, 184, 0.72)';
      ctx.strokeRect(button.x + 0.5, button.y + 0.5, button.w - 1, button.h - 1);
      ctx.fillStyle = '#fff0d2';
      ctx.font = 'bold 16px Inter, ui-sans-serif, system-ui, sans-serif';
      ctx.fillText(button.label, button.x + button.w / 2, button.y + 29);
    }
  } else {
    state.pauseMenuButtons = null;
  }

  ctx.fillStyle = state.paused ? 'rgba(255, 225, 183, 0.22)' : 'rgba(5, 0, 2, 0.66)';
  ctx.fillRect(bounds.x, bounds.y, bounds.w, bounds.h);
  ctx.strokeStyle = state.paused ? 'rgba(255, 226, 184, 0.78)' : 'rgba(255, 156, 92, 0.42)';
  ctx.lineWidth = 1.3;
  ctx.strokeRect(bounds.x + 0.5, bounds.y + 0.5, bounds.w - 1, bounds.h - 1);
  ctx.fillStyle = '#fff0d2';
  if (state.paused) {
    ctx.beginPath();
    ctx.moveTo(bounds.x + bounds.w * 0.38, bounds.y + bounds.h * 0.27);
    ctx.lineTo(bounds.x + bounds.w * 0.38, bounds.y + bounds.h * 0.73);
    ctx.lineTo(bounds.x + bounds.w * 0.70, bounds.y + bounds.h / 2);
    ctx.closePath();
    ctx.fill();
  } else {
    ctx.fillRect(bounds.x + bounds.w * 0.31, bounds.y + bounds.h * 0.25, bounds.w * 0.13, bounds.h * 0.50);
    ctx.fillRect(bounds.x + bounds.w * 0.56, bounds.y + bounds.h * 0.25, bounds.w * 0.13, bounds.h * 0.50);
  }
  ctx.restore();
}

function drawResultBanner() {
  if (!state.dead && !state.won) {
    state.restartButtonBounds = null;
    state.advanceButtonBounds = null;
    return;
  }
  const label = state.dead ? 'Membrane breached' : 'Lymph gate cleared';
  const sublabel = state.dead ? 'Infection reached the phagocyte' : `Seed ${state.runSeed}  |  Level ${state.depth} complete`;
  const w = Math.min(canvas.width - 36, 330);
  const h = state.won ? 108 : 98;
  const x = (canvas.width - w) / 2;
  const y = Math.max(68, canvas.height * 0.42);
  const restart = restartButtonBounds();
  state.restartButtonBounds = restart;
  state.advanceButtonBounds = null;
  ctx.save();
  ctx.fillStyle = state.dead ? 'rgba(23, 0, 7, 0.84)' : 'rgba(2, 20, 10, 0.80)';
  ctx.fillRect(x, y, w, h);
  ctx.strokeStyle = state.dead ? 'rgba(255, 116, 110, 0.68)' : 'rgba(126, 255, 164, 0.62)';
  ctx.lineWidth = 1.5;
  ctx.strokeRect(x + 0.5, y + 0.5, w - 1, h - 1);
  ctx.fillStyle = '#fff0d2';
  ctx.font = 'bold 16px Inter, ui-sans-serif, system-ui, sans-serif';
  ctx.textAlign = 'center';
  ctx.fillText(label, canvas.width / 2, y + 23);
  ctx.fillStyle = '#d5b69e';
  ctx.font = '11px Inter, ui-sans-serif, system-ui, sans-serif';
  ctx.fillText(sublabel, canvas.width / 2, y + 40);

  const buttons = state.won
    ? [
      { label: 'Advance', action: 'advance', x: x + 18, y: y + 56, w: (w - 46) / 2, h: RESTART_BUTTON_H },
      { label: 'Replay', action: 'restart', x: x + 28 + (w - 46) / 2, y: y + 56, w: (w - 46) / 2, h: RESTART_BUTTON_H }
    ]
    : [{ label: state.dead ? 'New Run' : 'Replay', action: 'restart', ...restart }];

  for (const button of buttons) {
    if (button.action === 'advance') state.advanceButtonBounds = button;
    if (button.action === 'restart') state.restartButtonBounds = button;
    ctx.fillStyle = button.action === 'advance' ? 'rgba(127, 255, 153, 0.14)' : 'rgba(255, 225, 183, 0.12)';
    ctx.fillRect(button.x, button.y, button.w, button.h);
    ctx.strokeStyle = button.action === 'advance' ? 'rgba(144, 255, 174, 0.74)' : 'rgba(255, 226, 184, 0.72)';
    ctx.lineWidth = 1.4;
    ctx.strokeRect(button.x + 0.5, button.y + 0.5, button.w - 1, button.h - 1);
    ctx.fillStyle = '#fff0d2';
    ctx.font = 'bold 13px Inter, ui-sans-serif, system-ui, sans-serif';
    ctx.fillText(button.label, button.x + button.w / 2, button.y + 22);
  }
  ctx.restore();
}

function drawPlayer() {
  const p = state.player;
  const animation = playerAnimationState(p);
  const mouthAngle = Math.atan2(p.dir.y, p.dir.x);
  const size = TILE * 1.62;
  ctx.save();
  ctx.translate(p.px, p.py);
  ctx.rotate(mouthAngle);
  ctx.scale(animation.scaleX, animation.scaleY);
  const frames = preparePlayerFrames();
  if (frames) {
    ctx.shadowColor = p.complementTicks > 0 ? 'rgba(255, 202, 82, 0.62)' : 'rgba(255, 157, 32, 0.42)';
    ctx.shadowBlur = p.complementTicks > 0 ? 16 : 10;
    ctx.drawImage(frames[animation.frame], -size / 2, -size / 2, size, size);
  } else {
    drawFallbackPlayer(size);
  }
  ctx.restore();
}

function drawFallbackPlayer(size) {
  ctx.fillStyle = '#f1ead7';
  ctx.strokeStyle = '#ff9d20';
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.arc(0, 0, size * 0.42, 0.25 * Math.PI, 1.75 * Math.PI);
  ctx.lineTo(size * 0.08, 0);
  ctx.closePath();
  ctx.fill();
  ctx.stroke();
  ctx.fillStyle = '#ff9d20';
  ctx.beginPath();
  ctx.arc(-size * 0.09, -size * 0.08, size * 0.08, 0, Math.PI * 2);
  ctx.fill();
}

function drawDebug() {
  ctx.fillStyle = 'rgba(0, 0, 0, 0.58)';
  ctx.fillRect(8, 8, 230, 102);
  ctx.fillStyle = '#f5ead8';
  ctx.font = '12px ui-monospace, monospace';
  const p = state.player;
  ctx.fillText(`tile ${Math.floor(p.px / TILE)},${Math.floor(p.py / TILE)}`, 16, 28);
  ctx.fillText(`dir ${p.dir.x},${p.dir.y} queued ${p.queued.x},${p.queued.y}`, 16, 46);
  ctx.fillText(`complement ${p.complementTicks.toFixed(1)}`, 16, 64);
  ctx.fillText(`ram ${p.ramTicks.toFixed(2)} armed ${p.ramArmed}`, 16, 82);
  ctx.fillText(`zone ${state.currentZone}`, 16, 100);
}

function updateHud() {
  antibodyCount.textContent = state.isTutorial ? 'Training' : `${state.collected} / ${state.totalAntibodies}`;
  complementState.textContent = state.player.complementTicks > 0 ? `${state.player.complementTicks.toFixed(1)}s` : 'Dormant';
  zoneState.textContent = state.currentZone;
  feverValue.textContent = `${Math.round(state.fever)}%`;
  feverFill.style.width = `${state.fever}%`;
  updateOverlayControls();
  if (state.isTutorial) {
    runState.textContent = state.tutorialComplete ? 'Training complete' : (state.tutorialChainStarted ? 'Observe knockback chain' : 'Dash into the first germ');
  } else if (state.dead) {
    runState.textContent = 'Infection breached the membrane';
  } else if (state.paused) {
    runState.textContent = 'Paused';
  } else if (!state.won) {
    if (state.infectionNeutralized && state.cleanseTicks > 0) runState.textContent = 'Infection nest neutralized';
    else runState.textContent = state.collected >= state.totalAntibodies ? 'Reach lymph gate' : 'Collect antibodies';
  }
}

function loop(now) {
  const previousTime = state ? state.lastTime : lastFrameTime;
  const dt = Math.min(0.05, (now - previousTime) / 1000);
  lastFrameTime = now;
  if (state) state.lastTime = now;
  update(dt);
  draw();
  requestAnimationFrame(loop);
}

function dirForKey(key) {
  if (key === 'arrowup' || key === 'w') return { x: 0, y: -1 };
  if (key === 'arrowdown' || key === 's') return { x: 0, y: 1 };
  if (key === 'arrowleft' || key === 'a') return { x: -1, y: 0 };
  if (key === 'arrowright' || key === 'd') return { x: 1, y: 0 };
  return null;
}

function bindInput() {
  window.addEventListener('keydown', event => {
    startAudioSystems();
    const key = event.key.toLowerCase();
    if (key === 'm') {
      toggleMusicPlayback();
      event.preventDefault();
      return;
    }
    if (key === 'p' || key === 'escape') {
      togglePause();
      event.preventDefault();
      return;
    }
    const dir = dirForKey(key);
    if (!dir) return;
    if (state?.paused) {
      event.preventDefault();
      return;
    }
    heldKeys.delete(key);
    heldKeys.set(key, dir);
    const held = combinedHeldDirection();
    setDirection(held.x, held.y);
    event.preventDefault();
  });
  window.addEventListener('keyup', event => {
    const key = event.key.toLowerCase();
    if (!dirForKey(key)) return;
    heldKeys.delete(key);
    if (!state) {
      event.preventDefault();
      return;
    }
    const held = combinedHeldDirection();
    if (isZeroDir(held)) state.player.queued = { ...ZERO_DIR };
    else setDirection(held.x, held.y);
    event.preventDefault();
  });
  gameSurface.addEventListener('pointerdown', beginJoystick);
  gameSurface.addEventListener('pointermove', updateJoystick);
  gameSurface.addEventListener('pointerup', endJoystick);
  gameSurface.addEventListener('pointercancel', endJoystick);
  gameSurface.addEventListener('lostpointercapture', endJoystick);
  restartButton.addEventListener('click', () => {
    startAudioSystems();
    if (state?.dead) startNewRun();
    else reset();
  });
  pauseToggle?.addEventListener('click', () => {
    startAudioSystems();
    togglePause();
  });
  mobilePauseToggle?.addEventListener('click', event => {
    event.stopPropagation();
    startAudioSystems();
    togglePause();
  });
  musicToggle?.addEventListener('click', () => toggleMusicPlayback());
  mobileMusicToggle?.addEventListener('click', event => {
    event.stopPropagation();
    startAudioSystems();
    toggleMusicPlayback();
  });
  fullscreenToggle?.addEventListener('click', () => {
    startAudioSystems();
    toggleFullscreen();
  });
  mobileFullscreenToggle?.addEventListener('click', event => {
    event.stopPropagation();
    startAudioSystems();
    toggleFullscreen();
  });
  menuToggle?.addEventListener('click', () => {
    startAudioSystems();
    playSoundEffect(SFX.uiSelect, 0.42);
    returnToMenu();
  });
  mobileMenuToggle?.addEventListener('click', event => {
    event.stopPropagation();
    startAudioSystems();
    playSoundEffect(SFX.uiSelect, 0.42);
    returnToMenu();
  });
  document.addEventListener('fullscreenchange', () => {
    updateOverlayControls();
    resetForViewportChange();
  });
  window.addEventListener('resize', () => resetForViewportChange());
  document.addEventListener('visibilitychange', () => handleMusicVisibilityChange());
  window.addEventListener('blur', () => pauseMusicForBackground());
  window.addEventListener('focus', () => handleWindowFocus());
  window.addEventListener('pagehide', () => pauseMusicForBackground());
  window.addEventListener('pageshow', () => resumeMusicFromBackground());
  debugToggle.addEventListener('click', () => { debug = !debug; });
}

function reset() {
  stopAllSoundLoops();
  heldKeys.clear();
  resetJoystick();
  if (!currentRun) currentRun = { seed: makeRunSeed(), depth: 1, startedAt: new Date().toISOString() };
  appMode = 'playing';
  state = buildState(level, currentRun);
  updateHud();
}

function resetForViewportChange() {
  const { cols, rows } = chooseGridDimensions();
  if (!state || appMode === 'menu' || appMode === 'tutorialPrompt') {
    resizeCanvas(cols, rows);
    return;
  }
  if (cols !== state.cols || rows !== state.rows) {
    if (appMode === 'tutorial') startTutorial(state.tutorialReturnSeed);
    else reset();
  }
}

function toggleFullscreen() {
  playSoundEffect(SFX.uiToggle, 0.42);
  if (!document.fullscreenElement) {
    const request = appShell.requestFullscreen || appShell.webkitRequestFullscreen;
    if (request) request.call(appShell);
  } else {
    const exit = document.exitFullscreen || document.webkitExitFullscreen;
    if (exit) exit.call(document);
  }
  window.setTimeout(() => updateOverlayControls(), 120);
}


function countTiles(tileType) {
  if (!state) return 0;
  let count = 0;
  for (const row of state.map) {
    for (const tile of row) if (tile === tileType) count++;
  }
  return count;
}

window.MarrowRunnerHarness = {
  getSnapshot() {
    if (!state) return null;
    return {
      canvasWidth: canvas.width,
      canvasHeight: canvas.height,
      cols: state.cols,
      rows: state.rows,
      totalAntibodies: state.totalAntibodies,
      collected: state.collected,
      remainingAntibodies: countTiles('.'),
      complementNodes: countTiles('o'),
      wallTiles: countTiles('#'),
      openTiles: countTiles(' '),
      vacuumedAntibodies: state.vacuumedAntibodies.length,
      vacuumedComplements: state.vacuumedComplements.length,
      enemies: state.enemies.length,
      runSeed: state.runSeed,
      depth: state.depth,
      enemyArchetypes: state.enemies.map(enemy => enemy.archetype),
      activeEnemies: state.enemies.filter(enemy => enemy.state === 'active').length,
      knockbackEnemies: state.enemies.filter(enemy => enemy.state === 'knockback').length,
      dyingEnemies: state.enemies.filter(enemy => enemy.state === 'dying').length,
      dead: state.dead,
      paused: state.paused,
      infectionNeutralized: state.infectionNeutralized,
      cleanseTicks: state.cleanseTicks,
      enemyNest: state.enemyNest ? { id: state.enemyNest.id, label: state.enemyNest.label, x: state.enemyNest.x, y: state.enemyNest.y, w: state.enemyNest.w, h: state.enemyNest.h } : null,
      pseudopodRamArmed: state.player.ramArmed,
      mechanicName: 'Pseudopod Ram',
      pseudopodRamTicks: state.player.ramTicks,
      movementMode: RADIAL_MOVEMENT ? 'radial' : 'stepped',
      gridNavHelper: GRID_NAV_HELPER,
      pinchWidening: PINCH_WIDENING,
      radialSpeed: PLAYER_RADIAL_SPEED,
      joystickResponseExponent: JOYSTICK_RESPONSE_EXPONENT,
      gridHelperStrength: GRID_HELPER_STRENGTH,
      turnBoost: PLAYER_TURN_BOOST,
      currentZone: state.currentZone,
      zones: state.zones.map(zone => ({ id: zone.id, label: zone.label, type: zone.type, x: zone.x, y: zone.y, w: zone.w, h: zone.h }))
    };
  },
  reset,
  chooseGridDimensions,
  setDebug(value) { debug = Boolean(value); }
};

async function main() {
  document.title = `Marrow Runner ${APP_VERSION}`;
  level = await loadLevel();
  loadSeedHistory();
  loadMusicPreference();
  updateOverlayControls();
  resizeCanvas(chooseGridDimensions().cols, chooseGridDimensions().rows);
  appMode = 'menu';
  bindInput();
  requestAnimationFrame(loop);
}

main().catch(error => {
  appErrorMessage = error?.message || 'Unknown startup error';
  appMode = 'error';
  if (runState) runState.textContent = appErrorMessage;
  resizeCanvas(chooseGridDimensions().cols, chooseGridDimensions().rows);
  bindInput();
  requestAnimationFrame(loop);
  console.error(error);
});
