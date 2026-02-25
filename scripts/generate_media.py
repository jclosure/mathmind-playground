#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import math
from pathlib import Path

W, H = 1280, 720
ASSETS = Path(__file__).resolve().parents[1] / "assets"
ASSETS.mkdir(exist_ok=True)

try:
    FONT_TITLE = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 64)
    FONT_SUB = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 30)
except Exception:
    FONT_TITLE = ImageFont.load_default()
    FONT_SUB = ImageFont.load_default()

CARDS = [
    ("linear_algebra.png", "Linear Algebra", (28, 42, 76), (193, 72, 72)),
    ("trigonometry.png", "Trigonometry", (16, 57, 76), (82, 206, 255)),
    ("spatial_reasoning.png", "Spatial Reasoning", (34, 35, 82), (125, 248, 206)),
    ("geometry_poses.png", "Geometry & Poses", (66, 32, 72), (255, 159, 67)),
    ("binary_descriptors.png", "Binary Descriptors", (20, 46, 44), (78, 205, 196)),
    ("transforms.png", "Transforms", (44, 36, 86), (161, 140, 209)),
    ("tensors.png", "Tensors", (45, 25, 60), (247, 121, 125)),
    ("physics.png", "Physics", (26, 44, 73), (255, 206, 84)),
]

def gradient(c1, c2):
    img = Image.new("RGB", (W, H), c1)
    px = img.load()
    for y in range(H):
        for x in range(W):
            t = (x * 0.7 + y * 0.6) / (W + H)
            r = int(c1[0] * (1 - t) + c2[0] * t)
            g = int(c1[1] * (1 - t) + c2[1] * t)
            b = int(c1[2] * (1 - t) + c2[2] * t)
            px[x, y] = (r, g, b)
    return img

for fname, title, c1, c2 in CARDS:
    img = gradient(c1, c2)
    d = ImageDraw.Draw(img)

    # grid + circles for "engineering candy"
    for x in range(0, W, 60):
        d.line([(x, 0), (x, H)], fill=(255, 255, 255, 40), width=1)
    for y in range(0, H, 60):
        d.line([(0, y), (W, y)], fill=(255, 255, 255, 40), width=1)
    for r in range(80, 500, 80):
        d.ellipse([(W*0.72-r, H*0.5-r), (W*0.72+r, H*0.5+r)], outline=(255,255,255), width=2)

    d.rounded_rectangle((60, 440, 820, 660), radius=24, fill=(0, 0, 0, 140), outline=(255,255,255), width=2)
    d.text((90, 485), title, fill=(255,255,255), font=FONT_TITLE)
    d.text((90, 575), "MathMind Playground • Interactive VPython Module", fill=(230, 245, 255), font=FONT_SUB)

    img.save(ASSETS / fname)

# simple animated teaser GIF
frames = []
for i in range(36):
    img = gradient((20, 24, 48), (82, 29, 124))
    d = ImageDraw.Draw(img)
    t = i / 36.0
    d.text((80, 90), "MathMind Playground", fill=(255,255,255), font=FONT_TITLE)
    d.text((84, 178), "Teaching the language of reality", fill=(210,220,255), font=FONT_SUB)

    cx, cy = int(900 + math.cos(t * math.tau) * 120), int(360 + math.sin(t * math.tau) * 120)
    for k in range(1, 7):
        rr = 60 * k
        alpha = max(20, 180 - k * 25)
        d.ellipse((cx-rr, cy-rr, cx+rr, cy+rr), outline=(120, 255, 220, alpha), width=2)

    # moving waveform
    pts = []
    for x in range(80, 1200, 8):
        y = int(560 + 42 * math.sin((x / 80) + t * math.tau))
        pts.append((x, y))
    d.line(pts, fill=(255, 210, 90), width=4)

    frames.append(img)

frames[0].save(ASSETS / "teaser.gif", save_all=True, append_images=frames[1:], duration=70, loop=0)
print("Generated media in", ASSETS)
