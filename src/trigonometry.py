#!/usr/bin/env python3
"""
Trigonometry Playground Module
==============================

Explore the unit circle and sine/cosine relationships with animation.
"""

from vpython import *
import numpy as np

print("📐 Trigonometry Playground Loading...")

# ═══════════════════════════════════════════════════════════════════════════
# 🔧 ADJUST THIS - QUICK EXPERIMENT SETTINGS
# ═══════════════════════════════════════════════════════════════════════════

AUTO_PLAY = True
ANGULAR_SPEED = 0.9
UNIT_RADIUS = 2.0
WAVE_LENGTH = 12.0
TRACE_POINTS = 240

# ═══════════════════════════════════════════════════════════════════════════
# SCENE SETUP
# ═══════════════════════════════════════════════════════════════════════════

scene = canvas(width=980, height=620)
scene.title = "Trigonometry Playground"
scene.range = 7
scene.background = vector(0.08, 0.1, 0.14)
scene.camera.pos = vector(0, 0, 16)
scene.camera.axis = vector(0, 0, -16)
scene.caption = """
<b>What to watch:</b><br>
• The orbiting point is angle θ on the unit circle.<br>
• Horizontal projection = cos(θ), vertical projection = sin(θ).<br>
• The sine wave to the right is built from the same motion.<br>
"""

# Reference plane and axes
ring(pos=vector(0, 0, 0), axis=vector(0, 0, 1), radius=UNIT_RADIUS,
     thickness=0.02, color=vector(0.8, 0.8, 0.95), opacity=0.7)
arrow(pos=vector(0, 0, 0), axis=vector(4.2, 0, 0), shaftwidth=0.03, color=color.red)
arrow(pos=vector(0, 0, 0), axis=vector(0, 4.2, 0), shaftwidth=0.03, color=color.green)
label(pos=vector(4.5, 0, 0), text="cos(θ)", box=False, height=12, color=color.red)
label(pos=vector(0, 4.5, 0), text="sin(θ)", box=False, height=12, color=color.green)

# Dynamic geometry
radius_arrow = arrow(pos=vector(0, 0, 0), axis=vector(UNIT_RADIUS, 0, 0),
                     shaftwidth=0.07, color=vector(1, 0.75, 0.2))
orbit_dot = sphere(pos=vector(UNIT_RADIUS, 0, 0), radius=0.12, color=vector(1, 0.8, 0.3),
                   make_trail=True, trail_type="points", interval=5, retain=250)

proj_x = curve(radius=0.015, color=vector(1, 0.4, 0.4))
proj_y = curve(radius=0.015, color=vector(0.4, 1, 0.4))
phase_link = curve(radius=0.01, color=vector(0.4, 0.9, 1), opacity=0.7)

wave_origin = vector(4.5, 0, 0)
wave = curve(radius=0.02, color=vector(0.4, 0.9, 1))

info = wtext(text="<br>")
speed_readout = wtext(text="")

scene.append_to_caption("<br><b>Controls</b><br>")

is_paused = not AUTO_PLAY
current_speed = ANGULAR_SPEED


def toggle_play(_):
    global is_paused
    is_paused = not is_paused
    play_btn.text = "Play" if is_paused else "Pause"


def on_speed(s):
    global current_speed
    current_speed = s.value
    speed_readout.text = f"  speed={current_speed:.2f} rad/s"


play_btn = button(text="Pause" if AUTO_PLAY else "Play", bind=toggle_play)
scene.append_to_caption("  speed ")
speed_slider = slider(min=0.1, max=2.4, value=ANGULAR_SPEED, length=240, bind=on_speed)
speed_readout.text = f"  speed={current_speed:.2f} rad/s"

# Pre-draw wave x coordinates
xs = np.linspace(0.0, WAVE_LENGTH, TRACE_POINTS)
theta = 0.0

while True:
    rate(60)

    if not is_paused:
        theta += current_speed / 60.0

    c = np.cos(theta)
    s = np.sin(theta)
    p = vector(UNIT_RADIUS * c, UNIT_RADIUS * s, 0)

    orbit_dot.pos = p
    radius_arrow.axis = p

    proj_x.clear()
    proj_x.append(vector(0, p.y, 0))
    proj_x.append(p)

    proj_y.clear()
    proj_y.append(vector(p.x, 0, 0))
    proj_y.append(p)

    ys = UNIT_RADIUS * np.sin(theta - xs)
    wave.clear()
    for x, y in zip(xs, ys):
        wave.append(wave_origin + vector(x, y, 0))

    tip = wave_origin + vector(0, p.y, 0)
    phase_link.clear()
    phase_link.append(p)
    phase_link.append(tip)

    info.text = (
        f"<br>θ={theta:5.2f} rad  |  sin(θ)={s: .3f}  |  cos(θ)={c: .3f}"
        f"<br>Identity check: sin²(θ)+cos²(θ)={s*s + c*c: .3f}"
    )
