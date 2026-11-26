"""One-Liner Laughs entry: write a single funny line to /output/entry.txt."""

import os

JOKE = "I asked an AI to write my wedding vows \u2014 it said 'I do', then auto-updated overnight and left me at the altar for a newer model."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
