# MathMind Playground 🧠✨

> *"Teaching the fundamental structures of thought — to ourselves and our descendants."*

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![VPython](https://img.shields.io/badge/powered-VPython-orange.svg)](https://www.glowscript.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**An interactive, 3D mathematical playground for understanding reality through code.**

No equations to memorize. Just grab, rotate, manipulate, and *see* how math works. Built with VPython for real-time 3D visualization.

---

## 🎬 What's Inside (Demo Reel)

> *Videos and screenshots will be populated here once generated.*

| Linear Algebra | Trigonometry | Spatial Reasoning |
|:---|:---|:---|
| ![vectors_demo](assets/vectors.gif) | ![waves_demo](assets/waves.gif) | ![3d_demo](assets/3d_space.gif) |
| *See vectors, spans, and matrix transformations in 3D* | *Watch the unit circle breathe life into sine waves* | *Understand orientation, cross products, coordinate frames* |

| Geometry & Poses | Binary Descriptors | Transforms |
|:---|:---|:---|
| ![kinematics_demo](assets/robot_arm.gif) | ![orb_demo](assets/orb_matcher.gif) | ![transforms_demo](assets/coordinate_frames.gif) |
| *Build a robot arm, learn forward kinematics* | *Visualize feature matching like a SLAM system* | *Jump between coordinate frames effortlessly* |

| Tensors | Physics |
|:---|:---|
| ![tensors_demo](assets/tensors.gif) | ![physics_demo](assets/physics.gif) |
| *Beyond matrices: stress, strain, index gymnastics* | *Forces, harmonic motion, angular momentum* |

---

## 🌟 Why This Isn't Like Other Math Tutors

| Traditional Learning | MathMind Playground |
|:---|:---|
| Static equations on paper | Live, manipulatable 3D objects |
| "Trust the formula" | "See *why* it works" |
| Memorize then apply | Experiment, discover, internalize |
| Abstract symbols | Immediate visual feedback |
| One correct path | Hack it, break it, rebuild it |

**Every concept is interactive.** Grab a vector and drag it. Rotate a coordinate frame. Watch what happens when you change parameters. The code is **right there** — uncomment a line, change a value, see the result instantly.

---

## 🚀 Quick Start (30 seconds)

```bash
# Clone and enter
cd math_playground

# Install (it'll handle VPython + dependencies)
pip install -r requirements.txt

# Launch the playground
python -m src.launcher

# A menu appears. Pick a number. Browser opens. Explore.
```

No Jupyter. No setup.py. Just run and play.

---

## 🎮 The Eight Realms

### 1️⃣ Linear Algebra — *The Language of Structure*
What is a vector? It's not just `[1, 2, 3]`. It's an **arrow** in space. A **combination** of basis directions. A **transformation** waiting to happen.

**You'll interact with:**
- Vector addition visually (parallelogram rule)
- Span visualization (grids warping under transformations)
- Eigenvectors that refuse to change direction
- Matrices as functions that reshape space

```python
# Hackable: Change this matrix, see space warp
transform = matrix([[2, 1], [0, 1]])  # Try [1,0],[0,1] (identity) or [0,-1],[1,0] (90° rotation)
```

---

### 2️⃣ Trigonometry — *The Language of Cycles*
The unit circle is the **heartbeat of mathematics**. Every wave, every oscillation, every periodic thing in nature traces back here.

**You'll interact with:**
- Circle unrolling into sine waves
- Phase and frequency in real-time
- Polar coordinates: distance + angle
- Why sin² + cos² = 1 (it's Pythagoras!)

---

### 3️⃣ Spatial Reasoning — *The Language of 3D*
Humans evolved in 3D space, but we often think in 2D. Time to reclaim your native intuition.

**You'll interact with:**
- The right-hand rule (grab it, feel it)
- Cross products as surface normals
- Dot products as projections
- Determinants as signed volumes

---

### 4️⃣ Geometry, Poses & Movement — *The Language of Robots*
How do you describe where something is AND which way it's facing? Welcome to **SE(3)** — the Special Euclidean group.

**You'll interact with:**
- A 3-joint robot arm you control
- Forward kinematics (joint angles → end effector position)
- Euler angles vs. quaternions (gimbal lock in action!)
- Rigid body transforms (translation + rotation)

---

### 5️⃣ Binary Descriptors — *The Language of Recognition*
How does a robot recognize places it's seen before? How does your phone track features in AR?

**You'll interact with:**
- ORB feature descriptors visualized
- Hamming distance for matching
- Binary patterns encoding image patches
- A mini visual SLAM simulation

---

### 6️⃣ Transforms — *The Language of Perspective*
"It's all relative" — Einstein knew it, and so do coordinate frames. How do you convert between "my view" and "your view"?

**You'll interact with:**
- Homogeneous coordinates (why 4D for 3D?)
- Transform composition (multiplying matrices)
- World coordinates vs. camera coordinates
- Inverse transforms (going backwards)

---

### 7️⃣ Tensors — *The Language of Fields*
Matrices were just the beginning. Tensors describe **how things change in every direction at once**.

**You'll interact with:**
- Rank-0 (scalars), Rank-1 (vectors), Rank-2 (matrices), Rank-3+
- Stress tensors (pressure from all sides)
- Index notation un-dumbed-down
- Tensor transformations

---

### 8️⃣ Physics — *The Language of Change*
Math describes structure. Physics describes **dynamics**.

**You'll interact with:**
- Forces as vectors (push, pull, accelerate)
- Simple harmonic motion (pendulums, springs)
- Angular momentum conservation
- Energy transformations

---

## 🛠️ Hacking the Playground

Each module is designed to be **modified live**:

1. Open `src/linear_algebra.py` (or any module)
2. Find the parameters (they're commented: `# 🔧 ADJUST THIS`)
3. Change values, save
4. Re-launch the module from the menu

```python
# Example from linear_algebra.py
eigen_scale = 2.0      # 🔧 ADJUST THIS: Change eigenvalue magnitude
vector_color = color.red  # 🔧 ADJUST THIS: Try color.cyan, color.green
show_grid = True       # 🔧 ADJUST THIS: Toggle reference grid
```

The code is your **world editor**. Treat it that way.

---

## 📚 The Philosophy

> *"We are teaching ourselves the thoughts of God."*

Linear algebra is how **structure** speaks.  
Trigonometry is how **cycles** speak.  
Geometry is how **form** speaks.  
Transforms are how **relationships** speak.  
Physics is how **change** speaks.

Together, they form the **language of reality**.

We aren't memorizing formulas. We're **building intuition** for how the universe works. This knowledge belongs to humanity — to you, to your children, to anyone curious enough to play.

---

## 🖥️ System Requirements

- **Python 3.9+**
- **Modern web browser** (Chrome, Firefox, Safari, Edge)
- **Graphics:** WebGL support for 3D

**Tested on:** macOS, Linux, Windows (with WSL/Native)

---

## 🧪 Development

```bash
# Run specific module directly (skips menu)
python src/linear_algebra.py

# With verbose VPython debugging
export VPYTHON_DEBUG=1
python src/transforms.py
```

---

## 🙏 Acknowledgments

- **VPython/GlowScript** — For making 3D web visualization accessible
- **David Hestenes** — Geometric Algebra as unified language
- **Grant Sanderson (3Blue1Brown)** — Essence of Linear Algebra inspiration
- **Joel & The Lobster** — For hacking late into the night 🦞

---

## 📜 License

MIT License — Share, modify, teach with it. We're building public knowledge here.

---

<p align="center">
  <i>"The most incomprehensible thing about the world is that it is comprehensible."</i><br>
  — Albert Einstein
</p>

<p align="center">
  <b><a href="https://github.com/joel/">⭐ Star this repo</a> • <a href="https://github.com/joel