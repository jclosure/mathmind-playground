# MathMind Playground 🧠✨

> *Teaching the fundamental structures of thought, to ourselves and our descendants.*

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![VPython](https://img.shields.io/badge/powered-VPython-orange.svg)](https://vpython.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

An interactive 3D playground for mathematical intuition. Built with VPython, designed for hacking.

![MathMind teaser](assets/teaser.gif)

---

## Why this exists

Most math education asks you to trust symbols first and intuition later.

This project flips that.
You manipulate vectors, rotate frames, tune physical systems, and watch the math respond in real time.

This is math as engineering candy.

---

## The Eight Realms

### 1) Linear Algebra
![Linear Algebra](assets/linear_algebra.png)
- draggable vectors, sums, span grid
- geometric vector addition and basis intuition

### 2) Trigonometry
![Trigonometry](assets/trigonometry.png)
- unit circle, live sin/cos projections
- wave generation from rotational motion

### 3) Spatial Reasoning
![Spatial Reasoning](assets/spatial_reasoning.png)
- moving 3D heading vector
- dot-product and angle interpretation in motion

### 4) Geometry & Poses
![Geometry & Poses](assets/geometry_poses.png)
- pose control via translation + yaw/pitch/roll
- world frame vs local body frame

### 5) Binary Descriptors
![Binary Descriptors](assets/binary_descriptors.png)
- visual bit-ring descriptors
- rotation/noise effects + Hamming distance

### 6) Transforms
![Transforms](assets/transforms.png)
- local-to-world coordinate conversion
- moving frame dynamics

### 7) Tensors
![Tensors](assets/tensors.png)
- 3x3 tensor acting on vectors and local field points
- quadratic form intuition

### 8) Physics
![Physics](assets/physics.png)
- mass-spring-damper simulation
- force vectors + energy readouts

---

## Quickstart

```bash
git clone https://github.com/jclosure/mathmind-playground.git
cd mathmind-playground

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python3 -m src.launcher
```

Or run any module directly:

```bash
python3 src/trigonometry.py
python3 src/physics.py
```

---

## Hackability

Every module includes a clearly marked `# 🔧 ADJUST THIS` section near the top.

Change constants, rerun, and observe the system immediately.

Good first tweaks:
- `ANGULAR_SPEED` in `trigonometry.py`
- `DAMPING_C` in `physics.py`
- `TENSOR_INIT` in `tensors.py`
- `POINT_LOCAL` in `transforms.py`

---

## Current Scope

Implemented and runnable now:
- `src/linear_algebra.py`
- `src/trigonometry.py`
- `src/spatial_reasoning.py`
- `src/geometry_poses.py`
- `src/binary_descriptors.py`
- `src/transforms.py`
- `src/tensors.py`
- `src/physics.py`
- `src/launcher.py`

---

## Philosophy

Linear algebra is how structure speaks.
Trigonometry is how cycles speak.
Geometry is how form speaks.
Transforms are how relationships speak.
Physics is how change speaks.

The goal is not to memorize formulas.
The goal is to *feel* the machinery of thought.

---

## Requirements

- Python 3.9+
- modern browser (VPython renders there)
- WebGL-capable graphics

---

## License

MIT
