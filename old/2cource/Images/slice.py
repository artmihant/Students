#!/bin/python
from PIL import Image
import numpy as np

image = Image.open("pie.png")

width, height = image.size

pixels = np.array(image)

pixels = pixels[: , : , :-1]

N = 7

steps = [width//N+1] * (width%N) + [width//N] * (N-width%N)

pieces, offset = [], 0
for step in steps:
    pieces.append((offset, offset+step))
    offset += step

for i, piece in enumerate(pieces):
    pixels_piece = pixels[:, piece[0]:piece[1]]
    new_image = Image.fromarray(pixels_piece)
    new_image.save(f'piece_{i+1}.jpg')



# for i in range(7):
#     pixels[i:10:5]

# # pixels = np.transpose(pixels, axes=(1,0,2))

# new_image = Image.fromarray(pixels)

# new_image.save('new_owl.jpg')

# def encode():

# 1) Кодировать сову
# 2) Повернуть сову на 90
# 3) Декодировать сову
