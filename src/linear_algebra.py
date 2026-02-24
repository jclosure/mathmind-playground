#!/usr/bin/env python3
"""
Linear Algebra Playground Module
================================

Discover vectors, matrices, and linear transformations in 3D space.
Drag vectors. Watch the span grow. See matrices warp reality.

HACKABLE PARAMETERS (look for 🔧 comments):
- Vector colors, magnitudes, directions
- Matrix transformation values
- Animation speeds
- Grid density
"""

from vpython import *
import numpy as np

print("🧮 Linear Algebra Playground Loading...")
print("Drag the RED vector to explore!")

# ═══════════════════════════════════════════════════════════════════════════
# 🔧 CONFIGURATION - ADJUST THESE VALUES AND RE-RUN
# ═══════════════════════════════════════════════════════════════════════════

SHOW_GRID = True          # Toggle reference grid
SHOW_SPAN = True          # Show vector span (combination of red & cyan vectors)
ANIMATE_GROWTH = True     # Animate vectors growing from origin
EIGEN_MODE = False        # Highlight eigen-directions

# Matrix transformation (try different ones!)
# Identity: [[1,0,0],[0,1,0],[0,0,1]]
# Rotation 90° Z: [[0,-1,0],[1,0,0],[0,0,1]]
# Scale X by 2: [[2,0,0],[0,1,0],[0,0,1]]
# Shear: [[1,0.5,0],[0.5,1,0],[0,0,1]]
TRANSFORM_MATRIX = [
    [1.5, 0.5, 0],
    [0.3, 1.2, 0],
    [0,   0,   1]
]

# Colors
COLOR_VECTOR_U = vector(1, 0.3, 0.3)     # Red-ish
COLOR_VECTOR_V = vector(0.3, 0.8, 1)     # Cyan-ish
COLOR_SUM = vector(0.3, 1, 0.3)          # Green
COLOR_TRANSFORMED = vector(1, 1, 0.3)    # Yellow

# ═══════════════════════════════════════════════════════════════════════════
# SETUP THE SCENE
# ═══════════════════════════════════════════════════════════════════════════

scene = canvas(width=800, height=600)
scene.title = "Linear Algebra Playground"
scene.caption = """
<b>Instructions:</b><br>
• Drag the <span style='color:red'>RED</span> vector to move it!<br>
• Watch the span (yellow pins) show all combinations<br>
• See how the <span style='color:green'>GREEN</span> sum updates<br>
Arrow keys: rotate view | Scroll: zoom<br>
"""
scene.range = 5
scene.background = vector(0.1, 0.1, 0.15)

# Camera position
scene.camera.pos = vector(8, 8, 8)
scene.camera.axis = vector(-8, -8, -8)

# ═══════════════════════════════════════════════════════════════════════════
# DRAW COORDINATE SYSTEM
# ═══════════════════════════════════════════════════════════════════════════

# X, Y, Z axes
x_axis = arrow(pos=vector(0, 0, 0), axis=vector(4, 0, 0), 
               shaftwidth=0.03, color=vector(0.8, 0.2, 0.2), opacity=0.5)
y_axis = arrow(pos=vector(0, 0, 0), axis=vector(0, 4, 0), 
               shaftwidth=0.03, color=vector(0.2, 0.8, 0.2), opacity=0.5)
z_axis = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, 4), 
               shaftwidth=0.03, color=vector(0.2, 0.2, 0.8), opacity=0.5)

# Axis labels
label(pos=vector(4.2, 0, 0), text='X', height=14, color=vector(1, 0.5, 0.5))
label(pos=vector(0, 4.2, 0), text='Y', height=14, color=vector(0.5, 1, 0.5))
label(pos=vector(0, 0, 4.2), text='Z', height=14, color=vector(0.5, 0.5, 1))

# Grid planes
if SHOW_GRID:
    # XY plane grid
    for i in range(-4, 5):
        curve(pos=[vector(-4, i, 0), vector(4, i, 0)], 
              color=vector(0.3, 0.3, 0.4), radius=0.01)
        curve(pos=[vector(i, -4, 0), vector(i, 4, 0)], 
              color=vector(0.3, 0.3, 0.4), radius=0.01)

# ═══════════════════════════════════════════════════════════════════════════
# INTERACTIVE VECTORS
# ═══════════════════════════════════════════════════════════════════════════

class DraggableVector:
    """A vector that can be dragged around in 3D space."""
    
    def __init__(self, position, color, label_text="v"):
        self.initial_pos = position
        self.color = color
        self.label_text = label_text
        self.dragging = False
        
        # The tip of the arrow (draggable sphere)
        self.tip = sphere(pos=position, radius=0.15, color=color,
                         make_trail=False, trail_type="points",
                         interval=10, retain=50)
        
        # The arrow shaft
        self.arrow = arrow(pos=vector(0,0,0), axis=position, 
                          shaftwidth=0.08, color=color)
        
        # Label showing [x, y, z]
        self.label_obj = label(pos=position, text=self._format_text(position),
                              height=12, color=color, box=False)
        
        # Drag events
        self.tip.bind("mousedown", self._on_down)
        self.tip.bind("mouseup", self._on_up)
        
    def _format_text(self, pos):
        return f"{self.label_text} = [{pos.x:.2f}, {pos.y:.2f}, {pos.z:.2f}]"
    
    def _on_down(self, evt):
        self.dragging = True
        self.tip.color = vector(1, 1, 0)  # Highlight yellow
        
    def _on_up(self, evt):
        self.dragging = False
        self.tip.color = self.color
        
    def update(self, other_vector=None):
        """Update position and visuals."""
        if self.dragging:
            # Project mouse to 3D point on z=0 plane (rough approximation)
            # VPython handles this through pick position
            if scene.mouse.pos:
                new_pos = scene.mouse.pos
                new_pos.z = 0  # Keep in XY plane for simplicity
                self.tip.pos = new_pos
                self.arrow.axis = new_pos
                self.label_obj.pos = new_pos
                self.label_obj.text = self._format_text(new_pos)

# Create draggable vectors
u_vec = DraggableVector(vector(2, 1, 0), COLOR_VECTOR_U, "u")
v_vec = DraggableVector(vector(1, 2, 0), COLOR_VECTOR_V, "v")

# ═══════════════════════════════════════════════════════════════════════════
# VISUALIZATIONS
# ═══════════════════════════════════════════════════════════════════════════

# Sum vector
sum_arrow = arrow(pos=vector(0,0,0), axis=vector(3,3,0),
                  shaftwidth=0.06, color=COLOR_SUM, visible=False)
sum_label = label(pos=vector(3,3,0), text="u+v", height=12, 
                  color=COLOR_SUM, visible=False)

# Parallelogram for visualizing vector addition
parallelogram = curve(pos=[vector(0,0,0), u_vec.initial_pos,
                           u_vec.initial_pos + v_vec.initial_pos, 
                           v_vec.initial_pos, vector(0,0,0)],
                      color=vector(1,1,0.3), radius=0.02, visible=False)

# Span visualization (grid of points showing all combinations)
span_points = []
for a in [0.25, 0.5, 0.75, 1.0, 1.25, 1.5]:
    for b in [0.25, 0.5, 0.75, 1.0, 1.25, 1.5]:
        pin = box(pos=vector(a * 2, b * 2, 0), size=vector(0.1,0.1,0.1),
                  color=vector(1, 0.8, 0.3), visible=SHOW_SPAN, opacity=0.3)
        span_points.append(pin)

# Matrix transformation visualization
transform_label = label(pos=vector(0, -3.5, 0), 
                        text="Matrix Transform: View spawn_transforms.py",
                        height=14, color=vector(1, 0.7, 0.3))

# ═══════════════════════════════════════════════════════════════════════════
# UI CONTROLS
# ═══════════════════════════════════════════════════════════════════════════

scene.append_to_caption("<br><b>Display Options:</b><br>")

def toggle_span(evt):
    """Toggle span visualization on/off."""
    global SHOW_SPAN
    SHOW_SPAN = not SHOW_SPAN
    for pin in span_points:
        pin.visible = SHOW_SPAN
        
button(bind=toggle_span, text="Toggle Span Grid",
       background=vector(0.3, 0.5, 0.7))

scene.append_to_caption("<br><br><b>Snap Vectors:</b><br>")

def snap_to_grid(evt):
    """Snap vectors to integer grid."""
    u_vec.tip.pos = vector(round(u_vec.tip.pos.x), 
                           round(u_vec.tip.pos.y), 0)
    u_vec.arrow.axis = u_vec.tip.pos
    u_vec.label_obj.pos = u_vec.tip.pos

    v_vec.tip.pos = vector(round(v_vec.tip.pos.x),
                           round(v_vec.tip.pos.y), 0)
    v_vec.arrow.axis = v_vec.tip.pos
    v_vec.label_obj.pos = v_vec.tip.pos

button(bind=snap_to_grid, text="Snap to Integer Grid",
       background=vector(0.35, 0.6, 0.35))

scene.append_to_caption("<br><br><b>Reset:</b><br>")


def reset_vectors(evt):
    """Reset both vectors to the defaults."""
    u_vec.tip.pos = u_vec.initial_pos
    v_vec.tip.pos = v_vec.initial_pos
    u_vec.arrow.axis = u_vec.tip.pos
    v_vec.arrow.axis = v_vec.tip.pos
    u_vec.label_obj.pos = u_vec.tip.pos
    v_vec.label_obj.pos = v_vec.tip.pos
    u_vec.label_obj.text = u_vec._format_text(u_vec.tip.pos)
    v_vec.label_obj.text = v_vec._format_text(v_vec.tip.pos)


button(bind=reset_vectors, text="Reset Vectors",
       background=vector(0.6, 0.4, 0.4))

# ═══════════════════════════════════════════════════════════════════════════
# ANIMATION LOOP
# ═══════════════════════════════════════════════════════════════════════════

while True:
    rate(60)

    u_vec.update()
    v_vec.update()

    u = u_vec.tip.pos
    v = v_vec.tip.pos
    s = u + v

    sum_arrow.visible = True
    sum_label.visible = True
    parallelogram.visible = True

    sum_arrow.axis = s
    sum_label.pos = s + vector(0.1, 0.1, 0)
    sum_label.text = f"u+v = [{s.x:.2f}, {s.y:.2f}, {s.z:.2f}]"

    parallelogram.clear()
    parallelogram.append(vector(0, 0, 0))
    parallelogram.append(u)
    parallelogram.append(s)
    parallelogram.append(v)
    parallelogram.append(vector(0, 0, 0))

    if SHOW_SPAN:
        idx = 0
        for a in [0.25, 0.5, 0.75, 1.0, 1.25, 1.5]:
            for b in [0.25, 0.5, 0.75, 1.0, 1.25, 1.5]:
                span_points[idx].pos = a * u + b * v
                idx += 1
