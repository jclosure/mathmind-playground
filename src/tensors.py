#!/usr/bin/env python3
"""
Tensors Playground Module
=========================

Build intuition for a 3x3 tensor acting on vectors.
"""

from vpython import *
import numpy as np

print("🧮 Tensors Playground Loading...")

# ═══════════════════════════════════════════════════════════════════════════
# 🔧 ADJUST THIS - TENSOR COEFFICIENTS
# ═══════════════════════════════════════════════════════════════════════════

AUTO_OSCILLATE = True
TENSOR_INIT = np.array([
    [1.4, 0.3, 0.0],
    [0.3, 1.0, 0.2],
    [0.0, 0.2, 0.8],
], dtype=float)

scene = canvas(width=980, height=620)
scene.title = "Tensors Playground"
scene.range = 6
scene.background = vector(0.08, 0.1, 0.13)
scene.camera.pos = vector(9, 7, 9)
scene.camera.axis = vector(-9, -7, -9)
scene.caption = """
<b>Tensor action:</b><br>
• Red arrow: input vector v.<br>
• Yellow arrow: output T·v.<br>
• Points show a small directional field warped by T.<br>
"""

arrow(pos=vector(0, 0, 0), axis=vector(4, 0, 0), shaftwidth=0.04, color=color.red, opacity=0.4)
arrow(pos=vector(0, 0, 0), axis=vector(0, 4, 0), shaftwidth=0.04, color=color.green, opacity=0.4)
arrow(pos=vector(0, 0, 0), axis=vector(0, 0, 4), shaftwidth=0.04, color=color.blue, opacity=0.4)

input_arrow = arrow(pos=vector(0, 0, 0), axis=vector(1.4, 0.9, 0.8), shaftwidth=0.08, color=vector(1, 0.35, 0.35))
output_arrow = arrow(pos=vector(0, 0, 0), axis=vector(1.8, 1.2, 0.9), shaftwidth=0.08, color=vector(1, 0.85, 0.2))
quad_label = label(pos=vector(0, -4.2, 0), text="", height=13, box=False, color=vector(0.85, 0.95, 1))

field_points = []
for x in [-2, -1, 0, 1, 2]:
    for y in [-2, -1, 0, 1, 2]:
        p = sphere(pos=vector(x, y, 0), radius=0.05, color=vector(0.3, 0.75, 1), opacity=0.65)
        field_points.append(p)

scene.append_to_caption("<br><b>Controls</b><br>")

tensor = TENSOR_INIT.copy()
is_paused = not AUTO_OSCILLATE
readout = wtext(text="<br>")


def toggle(_):
    global is_paused
    is_paused = not is_paused
    play_btn.text = "Animate: Off" if is_paused else "Animate: On"


def set_txx(s):
    tensor[0, 0] = s.value
    txx_text.text = f" txx={tensor[0,0]:.2f}"


def set_txy(s):
    tensor[0, 1] = s.value
    tensor[1, 0] = s.value
    txy_text.text = f" txy={tensor[0,1]:.2f}"


def set_tyy(s):
    tensor[1, 1] = s.value
    tyy_text.text = f" tyy={tensor[1,1]:.2f}"


play_btn = button(text="Animate: On" if AUTO_OSCILLATE else "Animate: Off", bind=toggle)
scene.append_to_caption("  ")
slider(min=0.2, max=2.2, value=tensor[0, 0], length=180, bind=set_txx)
txx_text = wtext(text=f" txx={tensor[0,0]:.2f}")
scene.append_to_caption("  ")
slider(min=-1.2, max=1.2, value=tensor[0, 1], length=180, bind=set_txy)
txy_text = wtext(text=f" txy={tensor[0,1]:.2f}")
scene.append_to_caption("  ")
slider(min=0.2, max=2.2, value=tensor[1, 1], length=180, bind=set_tyy)
tyy_text = wtext(text=f" tyy={tensor[1,1]:.2f}")

t = 0.0
while True:
    rate(60)
    if not is_paused:
        t += 1.0 / 60.0

    v = np.array([
        1.8 * np.cos(0.9 * t),
        1.2 * np.sin(1.1 * t + 0.6),
        0.8 * np.sin(0.5 * t),
    ])
    Tv = tensor @ v

    input_arrow.axis = vector(v[0], v[1], v[2])
    output_arrow.axis = vector(Tv[0], Tv[1], Tv[2])

    for p in field_points:
        vv = np.array([p.pos.x * 0.3, p.pos.y * 0.3, 0.0])
        ww = tensor @ vv
        p.pos.z = ww[2]
        p.color = vector(0.25 + min(0.7, abs(ww[0]) * 0.2), 0.6, 0.9)

    q = float(v.T @ tensor @ v)
    quad_label.text = f"Quadratic form: v^T T v = {q: .3f}"
    readout.text = (
        f"<br>v=[{v[0]: .2f}, {v[1]: .2f}, {v[2]: .2f}]"
        f"<br>Tv=[{Tv[0]: .2f}, {Tv[1]: .2f}, {Tv[2]: .2f}]"
    )
