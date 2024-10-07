import numpy as np
from PIL import Image
from random import randint

if __name__ == '__main__':
    image = Image.open("./cow.jpg")
    image_array = np.array(image)

    shape = image_array.shape
    for i in range(shape[0]):
        for j in range(shape[1]):
            # image_array[i][j][0] = randint(0, 255)
            image_array[i][j][1] = 0
            image_array[i][j][2] = 0

    # image_array = image_array.T

    pil_image = Image.fromarray(image_array)
    pil_image.show()
    pil_image.save("./cow_red.jpg")
