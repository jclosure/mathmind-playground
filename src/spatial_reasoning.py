#!/usr/bin/env python3
"""
Spatial Reasoning Playground Module
==================================

Train intuition for direction, angle, and projection in 3D.
"""

from vpython import *
import numpy as np

print("🧭 Spatial Reasoning Playground Loading...")

# ═══════════════════════════════════════════════════════════════════════════
# 🔧 ADJUST THIS - CORE PARAMETERS
# ═══════════════════════════════════════════════════════════════════════════

AUTO_ROTATE = True
ORBIT_RADIUS = 3.2
YAW_SPEED = 0.9
PITCH_AMPLITUDE = 0.8
SHOW_PLANES = True

scene = canvas(width=980, height=620)
scene.title = "Spatial Reasoning Playground"
scene.range = 6
scene.background = vector(0.08, 0.11, 0.15)
scene.camera.pos = vector(9, 6, 9)
scene.camera.axis = vector(-9, -6, -9)
scene.caption = """
<b>Goal:</b> understand direction in 3D from yaw/pitch and projections.<br>
• Yellow arrow: moving direction vector.<br>
• Cyan arrow: fixed target vector.<br>
• White text: dot product and angle between vectors.<br>
"""

# World axes
arrow(pos=vector(0, 0, 0), axis=vector(4, 0, 0), shaftwidth=0.04, color=color.red)
arrow(pos=vector(0, 0, 0), axis=vector(0, 4, 0), shaftwidth=0.04, color=color.green)
arrow(pos=vector(0, 0, 0), axis=vector(0, 0, 4), shaftwidth=0.04, color=color.blue)
label(pos=vector(4.3, 0, 0), text="X", box=False, height=12, color=color.red)
label(pos=vector(0, 4.3, 0), text="Y", box=False, height=12, color=color.green)
label(pos=vector(0, 0, 4.3), text="Z", box=False, height=12, color=color.blue)

if SHOW_PLANES:
    box(pos=vector(0, -0.001, 0), size=vector(8, 0.002, 8), color=vector(0.25, 0.3, 0.35), opacity=0.2)
    box(pos=vector(0, 0, -0.001), size=vector(8, 8, 0.002), color=vector(0.3, 0.22, 0.35), opacity=0.12)

# Moving probe and vectors
probe = sphere(pos=vector(ORBIT_RADIUS, 0, 0), radius=0.17, color=vector(1, 0.75, 0.2),
               make_trail=True, retain=220, interval=4)
dir_arrow = arrow(pos=vector(0, 0, 0), axis=norm(probe.pos) * 3.5,
                  shaftwidth=0.07, color=vector(1, 0.75, 0.2))

target_dir = norm(vector(-1.3, 1.0, 0.8))
target_arrow = arrow(pos=vector(0, 0, 0), axis=target_dir * 3.5, shaftwidth=0.07, color=vector(0.2, 0.9, 1))

shadow = sphere(pos=vector(probe.pos.x, 0, probe.pos.z), radius=0.08, color=vector(0.7, 0.7, 0.7), opacity=0.6)
drop_line = curve(radius=0.01, color=vector(0.8, 0.8, 0.8), opacity=0.6)

readout = wtext(text="<br>")

scene.append_to_caption("<br><b>Controls</b><br>")

is_paused = not AUTO_ROTATE
yaw_scale = 1.0


def toggle_motion(_):
    global is_paused
    is_paused = not is_paused
    play_btn.text = "Play" if is_paused else "Pause"


def on_yaw_scale(s):
    global yaw_scale
    yaw_scale = s.value
    yaw_text.text = f"  yaw-speed x{yaw_scale:.2f}"


play_btn = button(text="Pause" if AUTO_ROTATE else "Play", bind=toggle_motion)
scene.append_to_caption("  ")
yaw_slider = slider(min=0.2, max=2.2, value=1.0, length=220, bind=on_yaw_scale)
yaw_text = wtext(text="  yaw-speed x1.00")

t = 0.0
while True:
    rate(60)
    if not is_paused:
        t += 1.0 / 60.0

    yaw = t * YAW_SPEED * yaw_scale
    pitch = PITCH_AMPLITUDE * np.sin(0.9 * t)
    px = ORBIT_RADIUS * np.cos(yaw) * np.cos(pitch)
    py = ORBIT_RADIUS * np.sin(pitch)
    pz = ORBIT_RADIUS * np.sin(yaw) * np.cos(pitch)

    probe.pos = vector(px, py, pz)
    shadow.pos = vector(px, 0, pz)
    drop_line.clear()
    drop_line.append(probe.pos)
    drop_line.append(shadow.pos)

    heading = norm(probe.pos)
    dir_arrow.axis = heading * 3.5

    d = dot(heading, target_dir)
    d = max(-1.0, min(1.0, d))
    angle_deg = np.degrees(np.arccos(d))
    readout.text = (
        f"<br>yaw={yaw: .2f} rad, pitch={pitch: .2f} rad"
        f"<br>dot(heading,target)={d: .3f}  |  angle={angle_deg: .1f}°"
    )
