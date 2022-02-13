import sys
from PIL import Image

path = sys.argv[1] if len(sys.argv) == 2 else "./example/example.png"

image = Image.open(path)
image = image.convert("RGBA")
width, height = image.size

for x in range(width):
    for y in range(height):
        color = image.getpixel((x, y))
        if color[0] >= 220 and color[1] >= 220 and color[2] >= 220:
            newColor = (255, 255, 255,0)
            image.putpixel((x,y), newColor)

image.show()
image.save("out.png")
