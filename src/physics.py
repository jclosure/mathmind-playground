#!/usr/bin/env python3
"""
Physics Playground Module
=========================

Mass-spring-damper simulation with force visualization.
"""

from vpython import *
import numpy as np

print("⚙️ Physics Playground Loading...")

# ═══════════════════════════════════════════════════════════════════════════
# 🔧 ADJUST THIS - SYSTEM CONSTANTS
# ═══════════════════════════════════════════════════════════════════════════

MASS = 1.0
SPRING_K = 12.0
DAMPING_C = 0.8
GRAVITY = 9.8
REST_LENGTH = 2.2
DT = 0.01
AUTO_RUN = True

scene = canvas(width=980, height=620)
scene.title = "Physics Playground: Mass-Spring-Damper"
scene.range = 5
scene.background = vector(0.09, 0.1, 0.14)
scene.camera.pos = vector(0, 2.5, 10)
scene.camera.axis = vector(0, -1.0, -10)
scene.caption = """
<b>System:</b> one vertical mass-spring-damper<br>
• Hooke force: F_s = -k(x - L0)<br>
• Damping: F_d = -c v<br>
• Gravity: F_g = -mg<br>
"""

ceiling = box(pos=vector(0, 3, 0), size=vector(2.5, 0.2, 2.5), color=vector(0.5, 0.55, 0.62))
anchor = vector(0, 2.9, 0)
mass = sphere(pos=vector(0, 0.0, 0), radius=0.28, color=vector(1, 0.55, 0.25), make_trail=True, interval=2, retain=350)
spring = helix(pos=anchor, axis=mass.pos - anchor, radius=0.18, coils=16, thickness=0.05, color=vector(0.8, 0.85, 0.95))

force_spring = arrow(pos=mass.pos, axis=vector(0, 0, 0), shaftwidth=0.05, color=vector(0.2, 0.9, 1))
force_damping = arrow(pos=mass.pos, axis=vector(0, 0, 0), shaftwidth=0.05, color=vector(1, 0.9, 0.2))
force_gravity = arrow(pos=mass.pos, axis=vector(0, 0, 0), shaftwidth=0.05, color=vector(1, 0.35, 0.35))

readout = wtext(text="<br>")
scene.append_to_caption("<br><b>Controls</b><br>")

is_paused = not AUTO_RUN
k = SPRING_K
c = DAMPING_C
v = vector(0, 0, 0)


def toggle(_):
    global is_paused
    is_paused = not is_paused
    run_btn.text = "Run" if is_paused else "Pause"


def reset(_):
    global v
    mass.pos = vector(0, 0.0, 0)
    v = vector(0, 0, 0)
    mass.clear_trail()


def on_k(s):
    global k
    k = s.value
    k_text.text = f"  k={k:.1f}"


def on_c(s):
    global c
    c = s.value
    c_text.text = f"  c={c:.2f}"


run_btn = button(text="Pause" if AUTO_RUN else "Run", bind=toggle)
scene.append_to_caption("  ")
button(text="Reset", bind=reset)
scene.append_to_caption("<br>spring k ")
slider(min=2.0, max=25.0, value=k, length=220, bind=on_k)
k_text = wtext(text=f"  k={k:.1f}")
scene.append_to_caption("  damping c ")
slider(min=0.0, max=3.5, value=c, length=220, bind=on_c)
c_text = wtext(text=f"  c={c:.2f}")

while True:
    rate(120)
    if is_paused:
        continue

    displacement = mass.pos - anchor
    current_length = mag(displacement)
    if current_length < 1e-6:
        direction = vector(0, -1, 0)
    else:
        direction = displacement / current_length

    spring_force = -k * (current_length - REST_LENGTH) * direction
    damping_force = -c * v
    gravity_force = vector(0, -MASS * GRAVITY, 0)
    net_force = spring_force + damping_force + gravity_force

    a = net_force / MASS
    v = v + a * DT
    mass.pos = mass.pos + v * DT
    spring.axis = mass.pos - anchor

    force_spring.pos = mass.pos
    force_damping.pos = mass.pos
    force_gravity.pos = mass.pos
    force_spring.axis = spring_force * 0.04
    force_damping.axis = damping_force * 0.08
    force_gravity.axis = gravity_force * 0.02

    energy_k = 0.5 * MASS * mag(v) ** 2
    energy_s = 0.5 * k * (current_length - REST_LENGTH) ** 2
    readout.text = (
        f"<br>y={mass.pos.y: .3f} m  |  vy={v.y: .3f} m/s"
        f"<br>E_kin={energy_k: .3f} J  |  E_spring={energy_s: .3f} J"
    )
