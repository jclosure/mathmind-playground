#!/usr/bin/env python3
"""
Binary Descriptors Playground Module
===================================

Visualize binary feature descriptors and Hamming distance.
"""

from vpython import *
import numpy as np

print("🧬 Binary Descriptors Playground Loading...")

# ═══════════════════════════════════════════════════════════════════════════
# 🔧 ADJUST THIS - DESCRIPTOR SETTINGS
# ═══════════════════════════════════════════════════════════════════════════

BIT_COUNT = 24
NOISE_PROBABILITY = 0.15
ROTATION_OFFSET = 3
AUTO_SHIFT = True

scene = canvas(width=980, height=620)
scene.title = "Binary Descriptors Playground"
scene.range = 6
scene.background = vector(0.09, 0.11, 0.15)
scene.caption = """
<b>Descriptor matching intuition:</b><br>
• Top ring = descriptor A bits sampled around a patch.<br>
• Bottom ring = descriptor B (rotated + noisy).<br>
• Hamming distance = number of mismatched bits.<br>
"""


def make_bits(seed, n):
    rng = np.random.default_rng(seed)
    return (rng.random(n) > 0.5).astype(int)


def rotate_bits(bits, offset):
    n = len(bits)
    k = offset % n
    return np.concatenate((bits[-k:], bits[:-k])) if k else bits.copy()


base_bits = make_bits(seed=7, n=BIT_COUNT)
offset = ROTATION_OFFSET
noise_p = NOISE_PROBABILITY
phase = 0.0
is_paused = not AUTO_SHIFT

top_markers = []
bottom_markers = []
for i in range(BIT_COUNT):
    angle = 2.0 * np.pi * i / BIT_COUNT
    top_pos = vector(2.5 * np.cos(angle), 1.8, 2.5 * np.sin(angle))
    bottom_pos = vector(2.5 * np.cos(angle), -1.8, 2.5 * np.sin(angle))
    top_markers.append(box(pos=top_pos, size=vector(0.24, 0.24, 0.24), opacity=0.95))
    bottom_markers.append(box(pos=bottom_pos, size=vector(0.24, 0.24, 0.24), opacity=0.95))

match_lines = [curve(radius=0.01, color=vector(0.8, 0.8, 0.95), opacity=0.3) for _ in range(BIT_COUNT)]
readout = wtext(text="<br>")

scene.append_to_caption("<br><b>Controls</b><br>")


def toggle_auto(_):
    global is_paused
    is_paused = not is_paused
    auto_btn.text = "Auto shift: Off" if is_paused else "Auto shift: On"


def on_offset(s):
    global offset
    offset = int(round(s.value))
    offset_text.text = f"  offset={offset}"


def on_noise(s):
    global noise_p
    noise_p = s.value
    noise_text.text = f"  noise={noise_p:.2f}"


auto_btn = button(text="Auto shift: On" if AUTO_SHIFT else "Auto shift: Off", bind=toggle_auto)
scene.append_to_caption("  offset ")
slider(min=0, max=BIT_COUNT - 1, value=offset, length=200, bind=on_offset)
offset_text = wtext(text=f"  offset={offset}")
scene.append_to_caption("  noise ")
slider(min=0.0, max=0.5, value=noise_p, length=200, bind=on_noise)
noise_text = wtext(text=f"  noise={noise_p:.2f}")

rng = np.random.default_rng(42)

while True:
    rate(30)
    if not is_paused:
        phase += 0.08
        offset = int((ROTATION_OFFSET + 6 * np.sin(phase)) % BIT_COUNT)
        offset_text.text = f"  offset={offset}"

    bits_a = base_bits
    bits_b = rotate_bits(bits_a, offset)
    flips = (rng.random(BIT_COUNT) < noise_p).astype(int)
    bits_b = np.bitwise_xor(bits_b, flips)

    mismatches = 0
    for i in range(BIT_COUNT):
        a = bits_a[i]
        b = bits_b[i]
        top_markers[i].color = vector(0.2, 0.95, 0.35) if a else vector(0.2, 0.25, 0.8)
        bottom_markers[i].color = vector(0.2, 0.95, 0.35) if b else vector(0.2, 0.25, 0.8)
        match_lines[i].clear()
        match_lines[i].append(top_markers[i].pos)
        match_lines[i].append(bottom_markers[(i + offset) % BIT_COUNT].pos)
        if a != b:
            mismatches += 1
            match_lines[i].color = vector(1, 0.35, 0.25)
            match_lines[i].radius = 0.016
        else:
            match_lines[i].color = vector(0.6, 0.9, 1)
            match_lines[i].radius = 0.008

    readout.text = (
        f"<br>descriptor length={BIT_COUNT} bits"
        f"<br>Hamming distance={mismatches} ({100.0*mismatches/BIT_COUNT: .1f}%)"
    )
