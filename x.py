import os, sys
from PIL import Image, ImageOps

im = Image.open(sys.stdin.buffer)
ImageOps.mirror(im).save(sys.stdout.buffer, "PNG")
