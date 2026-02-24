#!/usr/bin/env python3
"""
MathMind Playground Launcher
Interactive menu to launch different mathematical explorations.
"""

import os
import sys
import subprocess

# Get the directory where this script lives
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

MODULES = {
    "1": ("linear_algebra", "Linear Algebra - Vectors, Matrices, Spaces"),
    "2": ("trigonometry", "Trigonometry - Circles, Waves, Identities"),
    "3": ("spatial_reasoning", "Spatial Reasoning - 3D Thinking"),
    "4": ("geometry_poses", "Geometry & Poses - Rigid Body Motion"),
    "5": ("binary_descriptors", "Binary Descriptors - Feature Matching"),
    "6": ("transforms", "Transforms - Coordinate Changes"),
    "7": ("tensors", "Tensors - Beyond Matrices"),
    "8": ("physics", "Physics - Forces & Motion"),
}
MODULE_COUNT = len(MODULES)

def print_banner():
    print("""
    ╭─────────────────────────────────────────────────────────────╮
    │                                                             │
    │     🧠  MathMind Playground  🧠                             │
    │                                                             │
    │     "Teaching the language of reality"                      │
    │                                                             │
    ╰─────────────────────────────────────────────────────────────╯
    
    Welcome! This is an interactive mathematical playground.
    Each module opens a 3D visualization you can manipulate.
    
    To hack: Open any src/*.py file, modify, and relaunch!
    """)

def print_menu():
    print("\n    Available Explorations:\n")
    for key, (module, desc) in MODULES.items():
        print(f"    {key}. {desc}")
    print("\n    q. Quit")
    print()

def launch_module(module_name):
    """Launch a VPython module in a subprocess."""
    module_path = os.path.join(SCRIPT_DIR, f"{module_name}.py")
    
    if not os.path.exists(module_path):
        print(f"❌ Module not found: {module_path}")
        return
    
    print(f"\n🚀 Launching {module_name}...")
    print("   A browser window should open with the 3D visualization.")
    print("   Close the browser tab to return to this menu.\n")
    
    try:
        # Run the module with the project root in Python path
        env = os.environ.copy()
        env["PYTHONPATH"] = PROJECT_ROOT + ":" + env.get("PYTHONPATH", "")
        
        result = subprocess.run(
            [sys.executable, module_path],
            cwd=PROJECT_ROOT,
            env=env
        )
        
        if result.returncode != 0:
            print(f"⚠️  Module exited with code {result.returncode}")
            
    except KeyboardInterrupt:
        print("\n\n👋 Interrupted by user.")
    except Exception as e:
        print(f"❌ Error launching module: {e}")

def main():
    print_banner()
    
    while True:
        print_menu()
        choice = input(f"    Enter your choice (1-{MODULE_COUNT}, or q): ").strip().lower()
        
        if choice == 'q':
            print("\n    Thanks for exploring! 🦞✨\n")
            break
        elif choice in MODULES:
            launch_module(MODULES[choice][0])
        else:
            print("\n    Invalid choice. Try again.")

if __name__ == "__main__":
    main()
