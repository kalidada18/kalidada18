"""Convert assets/avatar.jpeg into terminal-ready ASCII art for the README."""
from PIL import Image, ImageOps

SRC = "assets/avatar.jpeg"
OUT = "scratch/avatar_ascii.txt"

COLS = 80                      # output width in characters
CELL_RATIO = 0.5               # chars are ~2x taller than wide
RAMP = "@%#*+=-:. "            # dark -> light

img = Image.open(SRC).convert("RGB")
w, h = img.size

# square crop centered on the face, excluding the watermark corner
side = int(min(w, h) * 0.86)
cx = w // 2
cy = int(h * 0.44)
img = img.crop((cx - side // 2, cy - side // 2, cx + side // 2, cy + side // 2))

# background mask: uniform red backdrop -> blank space in the output
r, g, b = img.split()
pxrgb = img.load()
mask = Image.new("L", img.size, 0)
mk = mask.load()
for y in range(img.size[1]):
    for x in range(img.size[0]):
        rr, gg, bb = pxrgb[x, y][:3]
        if rr > 80 and gg < 70 and bb < 75 and rr - gg > 40:
            mk[x, y] = 255                      # red backdrop pixel

gray = img.convert("L")
gray = ImageOps.autocontrast(gray, cutoff=2)

rows = int(COLS * (gray.size[1] / gray.size[0]) * CELL_RATIO)
gray = gray.resize((COLS, rows), Image.LANCZOS)
mask = mask.resize((COLS, rows), Image.BILINEAR)

px = gray.load()
mp = mask.load()
n = len(RAMP)
lines = []
for y in range(rows):
    line = "".join(
        " " if mp[x, y] > 128 else RAMP[min(n - 1, px[x, y] * n // 256)]
        for x in range(COLS)
    )
    lines.append(line.rstrip())

art = "\n".join(lines)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(art + "\n")
print(art)
