#!/bin/python
from PIL import Image
import numpy as np

image = Image.open("owl.jpg")

pixels = np.array(image)

pixels = np.transpose(pixels, axes=(1,0,2))

new_image = Image.fromarray(pixels)

new_image.save('new_owl.jpg')

# def encode():

# 1) Кодировать сову
# 2) Повернуть сову на 90
# 3) Декодировать сову
