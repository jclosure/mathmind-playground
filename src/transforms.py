#!/usr/bin/env python3
"""
Transforms Playground Module
============================

Visualize coordinate transforms between world and local frames.
"""

from vpython import *
import numpy as np

print("🔄 Transforms Playground Loading...")

# ═══════════════════════════════════════════════════════════════════════════
# 🔧 ADJUST THIS - TRANSFORM DEFAULTS
# ═══════════════════════════════════════════════════════════════════════════

AUTO_ANIMATE = True
FRAME_B_RADIUS = 2.6
INITIAL_ROT_DEG = 32.0
POINT_LOCAL = vector(1.2, 0.8, -0.6)

scene = canvas(width=980, height=620)
scene.title = "Transforms Playground"
scene.range = 7
scene.background = vector(0.08, 0.1, 0.14)
scene.camera.pos = vector(10, 7, 10)
scene.camera.axis = vector(-10, -7, -10)
scene.caption = """
<b>World ↔ Local coordinates:</b><br>
• Gray axes are world frame W.<br>
• Color axes are moving frame B.<br>
• A local point p_B is converted to world p_W.<br>
"""

box(pos=vector(0, -0.01, 0), size=vector(11, 0.02, 11), color=vector(0.35, 0.35, 0.35), opacity=0.2)

# World frame
arrow(pos=vector(0, 0, 0), axis=vector(4, 0, 0), shaftwidth=0.05, color=vector(0.8, 0.35, 0.35), opacity=0.45)
arrow(pos=vector(0, 0, 0), axis=vector(0, 4, 0), shaftwidth=0.05, color=vector(0.35, 0.8, 0.35), opacity=0.45)
arrow(pos=vector(0, 0, 0), axis=vector(0, 0, 4), shaftwidth=0.05, color=vector(0.35, 0.35, 0.9), opacity=0.45)
label(pos=vector(4.3, 0, 0), text="W.x", box=False, height=12)
label(pos=vector(0, 4.3, 0), text="W.y", box=False, height=12)
label(pos=vector(0, 0, 4.3), text="W.z", box=False, height=12)

frame_origin = sphere(pos=vector(FRAME_B_RADIUS, 1.0, 0), radius=0.09, color=vector(1, 1, 0.5))
b_x = arrow(pos=frame_origin.pos, axis=vector(1, 0, 0), shaftwidth=0.04, color=color.red)
b_y = arrow(pos=frame_origin.pos, axis=vector(0, 1, 0), shaftwidth=0.04, color=color.green)
b_z = arrow(pos=frame_origin.pos, axis=vector(0, 0, 1), shaftwidth=0.04, color=color.blue)

local_point = sphere(pos=vector(0, 0, 0), radius=0.12, color=vector(1, 0.75, 0.2))
world_link = arrow(pos=frame_origin.pos, axis=vector(1, 0, 0), shaftwidth=0.03, color=vector(1, 0.75, 0.2))
origin_link = curve(radius=0.01, color=vector(0.6, 0.8, 1))

readout = wtext(text="<br>")
scene.append_to_caption("<br><b>Controls</b><br>")

is_paused = not AUTO_ANIMATE
rot_deg = INITIAL_ROT_DEG


def toggle_anim(_):
    global is_paused
    is_paused = not is_paused
    anim_btn.text = "Animate: Off" if is_paused else "Animate: On"


def on_rot(s):
    global rot_deg
    rot_deg = s.value
    rot_text.text = f"  rot={rot_deg:.1f}°"


anim_btn = button(text="Animate: On" if AUTO_ANIMATE else "Animate: Off", bind=toggle_anim)
scene.append_to_caption("  rotation ")
slider(min=-180, max=180, value=rot_deg, length=240, bind=on_rot)
rot_text = wtext(text=f"  rot={rot_deg:.1f}°")

t = 0.0
while True:
    rate(60)
    if not is_paused:
        t += 1.0 / 60.0
        rot_deg = 30.0 * np.sin(0.7 * t) + INITIAL_ROT_DEG
        rot_text.text = f"  rot={rot_deg:.1f}°"

    theta = np.radians(rot_deg)
    origin = vector(FRAME_B_RADIUS * np.cos(0.5 * t), 1.0 + 0.6 * np.sin(0.8 * t), FRAME_B_RADIUS * np.sin(0.5 * t))
    frame_origin.pos = origin

    x_hat = vector(np.cos(theta), 0, np.sin(theta))
    y_hat = vector(0, 1, 0)
    z_hat = vector(-np.sin(theta), 0, np.cos(theta))

    b_x.pos = origin
    b_y.pos = origin
    b_z.pos = origin
    b_x.axis = x_hat * 2.0
    b_y.axis = y_hat * 2.0
    b_z.axis = z_hat * 2.0

    p_world = origin + POINT_LOCAL.x * x_hat + POINT_LOCAL.y * y_hat + POINT_LOCAL.z * z_hat
    local_point.pos = p_world
    world_link.pos = origin
    world_link.axis = p_world - origin
    origin_link.clear()
    origin_link.append(vector(0, 0, 0))
    origin_link.append(origin)

    readout.text = (
        f"<br>p_B = [{POINT_LOCAL.x:.2f}, {POINT_LOCAL.y:.2f}, {POINT_LOCAL.z:.2f}]"
        f"<br>p_W = [{p_world.x:.2f}, {p_world.y:.2f}, {p_world.z:.2f}]"
    )
