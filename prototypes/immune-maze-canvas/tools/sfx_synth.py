#!/usr/bin/env python3
"""Dependency-free SFX synthesizer for Marrow Runner prototype.

Usage:
  python tools/sfx_synth.py eat_antibody assets/sfx/eat_antibody_01.wav
  python tools/sfx_synth.py --all
"""
from __future__ import annotations

import argparse
import math
import random
import struct
import wave
from pathlib import Path
from typing import Callable

SAMPLE_RATE = 44100
TWO_PI = math.pi * 2


def clamp(value: float, low: float = -0.98, high: float = 0.98) -> float:
    return max(low, min(high, value))


def sine(freq: float, t: float, phase: float = 0.0) -> float:
    return math.sin(TWO_PI * freq * t + phase)


def decay(t: float, duration: float, power: float = 2.0, attack: float = 0.002) -> float:
    if duration <= 0:
        return 0.0
    if t < attack:
        return t / max(attack, 0.0001)
    return max(0.0, 1.0 - (t - attack) / max(duration - attack, 0.0001)) ** power


def write_mono_wav(path: Path, samples: list[float], sample_rate: int = SAMPLE_RATE) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    peak = max((abs(sample) for sample in samples), default=1.0)
    norm = 0.96 / peak if peak > 0.98 else 1.0
    frames = [struct.pack('<h', int(clamp(sample * norm) * 32767)) for sample in samples]
    with wave.open(str(path), 'wb') as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)
        wav.writeframes(b''.join(frames))


def render(duration: float, fn: Callable[[float, int, random.Random], float], seed: int) -> list[float]:
    rng = random.Random(seed)
    count = int(SAMPLE_RATE * duration)
    return [fn(i / SAMPLE_RATE, i, rng) for i in range(count)]


def smooth_noise(rng: random.Random, state: list[float], amount: float = 0.25, keep: float = 0.75) -> float:
    state[0] = state[0] * keep + rng.uniform(-1, 1) * amount
    return state[0]


def eat_antibody(seed: int = 1701) -> list[float]:
    duration = 0.142
    noise_state = [0.0]

    def fn(t: float, i: int, rng: random.Random) -> float:
        if t < 0.002:
            envelope = 0.65 + 0.35 * (t / 0.002)
        else:
            envelope = max(0.0, (1.0 - (t - 0.002) / (duration - 0.002)) ** 2.2)
        low_freq = 310 - 135 * min(t / duration, 1)
        chirp_freq = 1250 + 1850 * min(t / duration, 1)
        pop = sine(low_freq, t, 0.7) * envelope * 0.38
        glint = sine(chirp_freq, t, 1.1) * (max(0.0, 1 - t / 0.055) ** 1.8) * 0.23
        wet = smooth_noise(rng, noise_state, 0.26, 0.74) * envelope * 0.15
        snap = sine(5200, t, 0.3) * (max(0.0, 1 - t / 0.018) ** 3.2) * 0.22
        return (pop + glint + wet + snap) * 0.88

    return render(duration, fn, seed)


def ui_select_soft(seed: int = 1101) -> list[float]:
    duration = 0.085
    noise_state = [0.0]

    def fn(t: float, i: int, rng: random.Random) -> float:
        e = decay(t, duration, 2.6, 0.001)
        click = sine(1650, t, 0.4) * decay(t, 0.028, 3.4, 0.0005) * 0.20
        body = sine(430 + 80 * t / duration, t, 0.2) * e * 0.24
        wet = smooth_noise(rng, noise_state, 0.18, 0.70) * e * 0.08
        return click + body + wet

    return render(duration, fn, seed)


def ui_toggle_pause(seed: int = 1102) -> list[float]:
    duration = 0.135
    noise_state = [0.0]

    def fn(t: float, i: int, rng: random.Random) -> float:
        first = decay(t, 0.055, 3.0, 0.001)
        second = decay(max(0, t - 0.062), 0.07, 2.4, 0.001) if t >= 0.062 else 0.0
        a = sine(520, t, 0.1) * first * 0.20 + sine(1800, t, 0.8) * first * 0.11
        b = sine(690, t - 0.062, 0.1) * second * 0.20 + sine(2300, t, 0.5) * second * 0.09
        wet = smooth_noise(rng, noise_state, 0.20, 0.72) * (first + second) * 0.07
        return a + b + wet

    return render(duration, fn, seed)


def pickup_complement_pellet(seed: int = 1201) -> list[float]:
    duration = 0.285
    noise_state = [0.0]

    def fn(t: float, i: int, rng: random.Random) -> float:
        e = decay(t, duration, 1.7, 0.004)
        rise = min(t / duration, 1)
        pulse = sine(170 - 45 * rise, t, 0.5) * e * 0.20
        shimmer = sine(760 + 980 * rise, t, 0.2) * e * 0.18
        shimmer += sine(1520 + 1200 * rise, t, 1.2) * e * 0.10
        spark = sine(4200 + 500 * rise, t, 0.3) * decay(t, 0.08, 2.8, 0.001) * 0.16
        wet = smooth_noise(rng, noise_state, 0.22, 0.76) * e * 0.12
        return pulse + shimmer + spark + wet

    return render(duration, fn, seed)


def complement_active_siren_loop(seed: int = 1202) -> list[float]:
    duration = 1.2
    noise_state = [0.0]

    def fn(t: float, i: int, rng: random.Random) -> float:
        phase = t / duration
        loop_env = 0.5 - 0.5 * math.cos(TWO_PI * phase)
        # Seamless amplitude pulse: never fully silent, peaks twice per loop.
        pulse = 0.45 + 0.55 * (0.5 - 0.5 * math.cos(TWO_PI * phase * 2))
        freq = 540 + 170 * (0.5 - 0.5 * math.cos(TWO_PI * phase))
        tone = sine(freq, t, 0.0) * 0.12 * pulse
        tone += sine(freq * 1.5, t, 0.9) * 0.045 * pulse
        bed = smooth_noise(rng, noise_state, 0.11, 0.91) * 0.045 * (0.35 + loop_env)
        return tone + bed

    samples = render(duration, fn, seed)
    # Equal-power taper both ends to hide loop seam.
    fade = int(SAMPLE_RATE * 0.035)
    for i in range(fade):
        g = math.sin((i / fade) * math.pi / 2) ** 2
        samples[i] *= g
        samples[-i - 1] *= g
    return samples


def complement_enemy_ingest(seed: int = 1203) -> list[float]:
    duration = 0.255
    noise_state = [0.0]

    def fn(t: float, i: int, rng: random.Random) -> float:
        e = decay(t, duration, 2.0, 0.003)
        down = 520 - 360 * min(t / duration, 1)
        gulp = sine(down, t, 1.1) * e * 0.34
        sub = sine(120 - 30 * t / duration, t, 0.5) * e * 0.18
        fizz = smooth_noise(rng, noise_state, 0.34, 0.68) * decay(t, duration, 2.8, 0.001) * 0.18
        return gulp + sub + fizz

    return render(duration, fn, seed)


def pseudopod_ram_start(seed: int = 1301) -> list[float]:
    duration = 0.128
    noise_state = [0.0]

    def fn(t: float, i: int, rng: random.Random) -> float:
        e = decay(t, duration, 2.2, 0.001)
        snap = sine(1500 - 850 * t / duration, t, 0.5) * decay(t, 0.045, 2.8, 0.0005) * 0.20
        thump = sine(120 - 30 * t / duration, t, 0.8) * e * 0.34
        stretch = sine(360 - 180 * t / duration, t, 0.1) * e * 0.22
        wet = smooth_noise(rng, noise_state, 0.24, 0.74) * e * 0.10
        return snap + thump + stretch + wet

    return render(duration, fn, seed)


def ram_enemy_launch(seed: int = 1302) -> list[float]:
    duration = 0.165
    noise_state = [0.0]

    def fn(t: float, i: int, rng: random.Random) -> float:
        e = decay(t, duration, 2.0, 0.001)
        slap = sine(190, t, 0.4) * e * 0.30
        smack = sine(950 - 320 * t / duration, t, 1.0) * decay(t, 0.07, 2.0, 0.0005) * 0.18
        whoosh = smooth_noise(rng, noise_state, 0.30, 0.70) * e * 0.16
        return slap + smack + whoosh

    return render(duration, fn, seed)


def knockback_chain_impact(seed: int = 1303) -> list[float]:
    duration = 0.118
    noise_state = [0.0]

    def fn(t: float, i: int, rng: random.Random) -> float:
        e = decay(t, duration, 2.5, 0.0005)
        crack = sine(2100, t, 0.7) * decay(t, 0.025, 2.5, 0.0003) * 0.18
        pop = sine(260 - 90 * t / duration, t, 0.2) * e * 0.28
        wet = smooth_noise(rng, noise_state, 0.36, 0.62) * e * 0.15
        return crack + pop + wet

    return render(duration, fn, seed)


def knockback_wall_kill(seed: int = 1304) -> list[float]:
    duration = 0.255
    noise_state = [0.0]

    def fn(t: float, i: int, rng: random.Random) -> float:
        e = decay(t, duration, 2.2, 0.001)
        thud = sine(86 - 18 * t / duration, t, 0.9) * e * 0.38
        splat = smooth_noise(rng, noise_state, 0.44, 0.66) * decay(t, 0.20, 2.0, 0.0005) * 0.26
        membrane = sine(360 - 120 * t / duration, t, 0.1) * e * 0.13
        return thud + splat + membrane

    return render(duration, fn, seed)


def enemy_death_spin(seed: int = 1305) -> list[float]:
    duration = 0.42
    noise_state = [0.0]

    def fn(t: float, i: int, rng: random.Random) -> float:
        e = decay(t, duration, 1.7, 0.003)
        spin = sine(620 - 420 * t / duration, t, 0.2) * e * 0.15
        fizz = smooth_noise(rng, noise_state, 0.28, 0.72) * e * 0.16
        sub = sine(150 - 60 * t / duration, t, 0.4) * e * 0.09
        return spin + fizz + sub

    return render(duration, fn, seed)


def player_death_membrane_breach(seed: int = 1401) -> list[float]:
    duration = 0.62
    noise_state = [0.0]

    def fn(t: float, i: int, rng: random.Random) -> float:
        e = decay(t, duration, 1.25, 0.002)
        sting = sine(1100 - 680 * min(t / 0.22, 1), t, 1.2) * decay(t, 0.28, 1.4, 0.0008) * 0.25
        tear = smooth_noise(rng, noise_state, 0.36, 0.70) * e * 0.22
        fail = sine(95 - 35 * t / duration, t, 0.5) * e * 0.30
        return sting + tear + fail

    return render(duration, fn, seed)


def nest_cleanse_wave(seed: int = 1501) -> list[float]:
    duration = 1.55
    noise_state = [0.0]

    def fn(t: float, i: int, rng: random.Random) -> float:
        rise = min(t / duration, 1)
        bloom = math.sin(rise * math.pi) ** 0.7
        low = sine(95 + 45 * rise, t, 0.2) * bloom * 0.18
        chord = (sine(330 + 80 * rise, t, 0.0) + sine(495 + 120 * rise, t, 0.3) + sine(660 + 130 * rise, t, 0.6)) * bloom * 0.055
        wash = smooth_noise(rng, noise_state, 0.14, 0.88) * bloom * 0.11
        sparkle = sine(2100 + 900 * rise, t, 1.1) * (rise ** 1.4) * decay(max(0, duration - t), duration, 0.7, 0.001) * 0.045
        return low + chord + wash + sparkle

    return render(duration, fn, seed)


def level_clear_gate(seed: int = 1502) -> list[float]:
    duration = 0.92
    noise_state = [0.0]

    def fn(t: float, i: int, rng: random.Random) -> float:
        rise = min(t / duration, 1)
        e = math.sin(math.pi * rise) ** 0.7
        portal = sine(220 + 90 * rise, t, 0.4) * e * 0.14
        shimmer = (sine(660 + 160 * rise, t, 0.0) + sine(990 + 230 * rise, t, 0.7)) * e * 0.08
        gate = smooth_noise(rng, noise_state, 0.12, 0.88) * e * 0.08
        return portal + shimmer + gate

    return render(duration, fn, seed)


def enemy_respawn_warning(seed: int = 1601) -> list[float]:
    duration = 0.24
    noise_state = [0.0]

    def fn(t: float, i: int, rng: random.Random) -> float:
        e = decay(t, duration, 1.8, 0.002)
        pulse = sine(180 + 80 * math.sin(TWO_PI * t / duration), t, 0.5) * e * 0.22
        bubble = smooth_noise(rng, noise_state, 0.28, 0.70) * e * 0.15
        warn = sine(720, t, 0.3) * decay(t, 0.10, 2.4, 0.001) * 0.08
        return pulse + bubble + warn

    return render(duration, fn, seed)


def fever_tick_warning(seed: int = 1602) -> list[float]:
    duration = 0.34
    noise_state = [0.0]

    def fn(t: float, i: int, rng: random.Random) -> float:
        e = decay(t, duration, 2.4, 0.002)
        beat = sine(72, t, 0.8) * e * 0.24
        grit = smooth_noise(rng, noise_state, 0.18, 0.80) * e * 0.08
        return beat + grit

    return render(duration, fn, seed)


def antibody_vacuum_start(seed: int = 1603) -> list[float]:
    duration = 0.055

    def fn(t: float, i: int, rng: random.Random) -> float:
        e = decay(t, duration, 2.0, 0.0005)
        return sine(980 - 340 * t / duration, t, 0.2) * e * 0.16 + sine(2600, t, 0.5) * e * 0.06

    return render(duration, fn, seed)


PRESETS: dict[str, Callable[[int], list[float]]] = {
    'eat_antibody': eat_antibody,
    'ui_select_soft': ui_select_soft,
    'ui_toggle_pause': ui_toggle_pause,
    'pickup_complement_pellet': pickup_complement_pellet,
    'complement_active_siren_loop': complement_active_siren_loop,
    'complement_enemy_ingest': complement_enemy_ingest,
    'pseudopod_ram_start': pseudopod_ram_start,
    'ram_enemy_launch': ram_enemy_launch,
    'knockback_chain_impact': knockback_chain_impact,
    'knockback_wall_kill': knockback_wall_kill,
    'enemy_death_spin': enemy_death_spin,
    'player_death_membrane_breach': player_death_membrane_breach,
    'nest_cleanse_wave': nest_cleanse_wave,
    'level_clear_gate': level_clear_gate,
    'enemy_respawn_warning': enemy_respawn_warning,
    'fever_tick_warning': fever_tick_warning,
    'antibody_vacuum_start': antibody_vacuum_start,
}

DEFAULT_OUTPUTS = {
    'eat_antibody': 'assets/sfx/eat_antibody_01.wav',
    'ui_select_soft': 'assets/sfx/ui_select_soft_01.wav',
    'ui_toggle_pause': 'assets/sfx/ui_toggle_pause_01.wav',
    'pickup_complement_pellet': 'assets/sfx/pickup_complement_pellet_01.wav',
    'complement_active_siren_loop': 'assets/sfx/complement_active_siren_loop_01.wav',
    'complement_enemy_ingest': 'assets/sfx/complement_enemy_ingest_01.wav',
    'pseudopod_ram_start': 'assets/sfx/pseudopod_ram_start_01.wav',
    'ram_enemy_launch': 'assets/sfx/ram_enemy_launch_01.wav',
    'knockback_chain_impact': 'assets/sfx/knockback_chain_impact_01.wav',
    'knockback_wall_kill': 'assets/sfx/knockback_wall_kill_01.wav',
    'enemy_death_spin': 'assets/sfx/enemy_death_spin_01.wav',
    'player_death_membrane_breach': 'assets/sfx/player_death_membrane_breach_01.wav',
    'nest_cleanse_wave': 'assets/sfx/nest_cleanse_wave_01.wav',
    'level_clear_gate': 'assets/sfx/level_clear_gate_01.wav',
    'enemy_respawn_warning': 'assets/sfx/enemy_respawn_warning_01.wav',
    'fever_tick_warning': 'assets/sfx/fever_tick_warning_01.wav',
    'antibody_vacuum_start': 'assets/sfx/antibody_vacuum_start_01.wav',
}


def write_preset(preset: str, output: Path, seed: int) -> None:
    samples = PRESETS[preset](seed)
    write_mono_wav(output, samples)
    print(f'wrote {output} ({len(samples) / SAMPLE_RATE:.3f}s)')


def main() -> None:
    parser = argparse.ArgumentParser(description='Generate Marrow Runner prototype sound effects.')
    parser.add_argument('preset', nargs='?', choices=sorted(PRESETS))
    parser.add_argument('output', nargs='?', type=Path)
    parser.add_argument('--seed', type=int, default=1701)
    parser.add_argument('--all', action='store_true', help='Generate every preset to its default output path.')
    args = parser.parse_args()

    if args.all:
        for index, preset in enumerate(DEFAULT_OUTPUTS):
            write_preset(preset, Path(DEFAULT_OUTPUTS[preset]), args.seed + index)
        return

    if not args.preset or not args.output:
        parser.error('preset and output are required unless --all is used')
    write_preset(args.preset, args.output, args.seed)


if __name__ == '__main__':
    main()
