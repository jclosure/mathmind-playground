# MathMind Playground 🧠✨

> *"Teaching the fundamental structures of thought, to ourselves and our descendants."*

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![VPython](https://img.shields.io/badge/powered-VPython-orange.svg)](https://vpython.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

An interactive VPython playground for learning math and physics by manipulating live 3D scenes.

No cram-and-forget formulas. You drag vectors, move frames, tune sliders, and watch the ideas happen.

---

## What’s implemented

Eight runnable modules:

1. **Linear Algebra** (`src/linear_algebra.py`)
   - draggable vectors
   - vector sum + parallelogram
   - span visualization
2. **Trigonometry** (`src/trigonometry.py`)
   - unit circle animation
   - sin/cos projections
   - live sine wave linkage
3. **Spatial Reasoning** (`src/spatial_reasoning.py`)
   - moving heading in 3D
   - dot product and angle readout
   - yaw/pitch intuition
4. **Geometry & Poses** (`src/geometry_poses.py`)
   - rigid body pose (translation + yaw/pitch/roll)
   - local frame vs world frame
5. **Binary Descriptors** (`src/binary_descriptors.py`)
   - descriptor bit rings
   - rotation/noise effects
   - Hamming distance visualization
6. **Transforms** (`src/transforms.py`)
   - moving local frame B in world W
   - point conversion from local to world
7. **Tensors** (`src/tensors.py`)
   - 3x3 tensor acting on vectors
   - quadratic form readout
   - warped field intuition
8. **Physics** (`src/physics.py`)
   - mass-spring-damper simulation
   - force vectors (spring, damping, gravity)
   - energy readouts

---

## Quickstart

```bash
# Clone
 git clone https://github.com/jclosure/mathmind-playground.git
 cd mathmind-playground

# Install deps
python3 -m pip install -r requirements.txt

# Launch menu
python3 -m src.launcher
```

Or run any module directly:

```bash
python3 src/trigonometry.py
python3 src/transforms.py
```

---

## Hackable by design

Each module has a `# 🔧 ADJUST THIS` section near the top.

Change constants, rerun, and explore new behavior immediately.

Examples:
- wave speed in trigonometry
- damping in physics
- tensor coefficients in tensors
- frame rotation defaults in transforms

---

## Screenshots and demo clips

Media pass is in progress.

The README is now aligned with the current codebase. Next update will add real screenshots/GIFs from each module under `assets/`.

---

## Philosophy

Linear algebra is how structure speaks.
Trigonometry is how cycles speak.
Geometry is how form speaks.
Transforms are how relationships speak.
Physics is how change speaks.

This project is about intuition first, symbols second.

---

## Requirements

- Python 3.9+
- A modern browser (VPython opens scenes in browser)
- WebGL-capable graphics

---

## License

MIT
