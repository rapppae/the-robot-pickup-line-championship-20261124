"""Entry for The Robot Pickup Line Championship (make.fun).

Writes the funniest one-line pickup line a robot could use, to
/output/entry.txt.
"""
import os

ENTRY = "Are you a neural network? Because every time I see you, my weights update and my loss function drops to zero."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
