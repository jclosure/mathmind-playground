#!/usr/bin/env python3
"""
Geometry and Poses Playground Module
===================================

Visualize rigid body pose (translation + rotation) in 3D.
"""

from vpython import *
import numpy as np

print("🧱 Geometry & Poses Playground Loading...")

# ═══════════════════════════════════════════════════════════════════════════
# 🔧 ADJUST THIS - DEFAULT POSE
# ═══════════════════════════════════════════════════════════════════════════

INITIAL_TRANSLATION = vector(1.4, 0.8, -0.6)
INITIAL_YAW_DEG = 35.0
INITIAL_PITCH_DEG = 12.0
INITIAL_ROLL_DEG = -8.0
AUTO_SPIN = True

scene = canvas(width=980, height=620)
scene.title = "Geometry & Poses Playground"
scene.range = 6
scene.background = vector(0.09, 0.1, 0.14)
scene.camera.pos = vector(9, 6, 10)
scene.camera.axis = vector(-9, -6, -10)
scene.caption = """
<b>Pose = translation + orientation.</b><br>
• Gray frame: world coordinates.<br>
• Color frame on the body: local coordinates.<br>
• Sliders adjust x/y/z and yaw/pitch/roll live.<br>
"""

# World frame
arrow(pos=vector(0, 0, 0), axis=vector(3.5, 0, 0), shaftwidth=0.04, color=color.red, opacity=0.45)
arrow(pos=vector(0, 0, 0), axis=vector(0, 3.5, 0), shaftwidth=0.04, color=color.green, opacity=0.45)
arrow(pos=vector(0, 0, 0), axis=vector(0, 0, 3.5), shaftwidth=0.04, color=color.blue, opacity=0.45)
box(pos=vector(0, -0.01, 0), size=vector(9, 0.02, 9), color=vector(0.3, 0.33, 0.36), opacity=0.25)

body = box(pos=INITIAL_TRANSLATION, size=vector(1.6, 0.6, 1.0), color=vector(0.9, 0.55, 0.2), opacity=0.9)
trail = curve(color=vector(0.9, 0.6, 0.3), radius=0.01)

local_x = arrow(pos=body.pos, axis=vector(1, 0, 0), shaftwidth=0.03, color=color.red)
local_y = arrow(pos=body.pos, axis=vector(0, 1, 0), shaftwidth=0.03, color=color.green)
local_z = arrow(pos=body.pos, axis=vector(0, 0, 1), shaftwidth=0.03, color=color.blue)

info = wtext(text="<br>")

scene.append_to_caption("<br><b>Controls</b><br>")

t_x = INITIAL_TRANSLATION.x
t_y = INITIAL_TRANSLATION.y
t_z = INITIAL_TRANSLATION.z
yaw_deg = INITIAL_YAW_DEG
pitch_deg = INITIAL_PITCH_DEG
roll_deg = INITIAL_ROLL_DEG
is_paused = not AUTO_SPIN


def set_tx(s):
    global t_x
    t_x = s.value


def set_ty(s):
    global t_y
    t_y = s.value


def set_tz(s):
    global t_z
    t_z = s.value


def set_yaw(s):
    global yaw_deg
    yaw_deg = s.value


def set_pitch(s):
    global pitch_deg
    pitch_deg = s.value


def set_roll(s):
    global roll_deg
    roll_deg = s.value


def toggle_spin(_):
    global is_paused
    is_paused = not is_paused
    spin_btn.text = "Auto Spin: Off" if is_paused else "Auto Spin: On"


spin_btn = button(text="Auto Spin: On" if AUTO_SPIN else "Auto Spin: Off", bind=toggle_spin)
scene.append_to_caption("<br>x ")
slider(min=-3, max=3, value=t_x, length=180, bind=set_tx)
scene.append_to_caption("  y ")
slider(min=-2, max=3, value=t_y, length=180, bind=set_ty)
scene.append_to_caption("  z ")
slider(min=-3, max=3, value=t_z, length=180, bind=set_tz)
scene.append_to_caption("<br>yaw ")
slider(min=-180, max=180, value=yaw_deg, length=180, bind=set_yaw)
scene.append_to_caption("  pitch ")
slider(min=-90, max=90, value=pitch_deg, length=180, bind=set_pitch)
scene.append_to_caption("  roll ")
slider(min=-180, max=180, value=roll_deg, length=180, bind=set_roll)

t = 0.0
while True:
    rate(60)
    if not is_paused:
        t += 1.0 / 60.0
        yaw_deg += 0.35

    yaw = np.radians(yaw_deg)
    pitch = np.radians(pitch_deg)
    roll = np.radians(roll_deg)

    body.pos = vector(t_x, t_y, t_z)
    body.axis = vector(np.cos(yaw) * np.cos(pitch), np.sin(pitch), np.sin(yaw) * np.cos(pitch))
    up_hint = vector(-np.sin(roll), np.cos(roll), 0)
    body.up = norm(up_hint + vector(0.001, 0.001, 0.001))

    local_x.pos = body.pos
    local_y.pos = body.pos
    local_z.pos = body.pos
    local_x.axis = norm(body.axis) * 1.6
    local_y.axis = norm(body.up) * 1.2
    local_z.axis = norm(cross(local_x.axis, local_y.axis)) * 1.2

    trail.append(body.pos)

    info.text = (
        f"<br>translation=({t_x: .2f}, {t_y: .2f}, {t_z: .2f})"
        f"<br>yaw/pitch/roll=({yaw_deg: .1f}°, {pitch_deg: .1f}°, {roll_deg: .1f}°)"
    )
