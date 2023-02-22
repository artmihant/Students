# библиотеки
# инициализиация
import math

from PIL import Image, ImageDraw, ImageFont
import numpy as np

if __name__ == '__main__':

    # пусть c = p + iq и p меняется в диапазоне от pmin до pmax,
    # а q меняется в диапазоне от qmin до qmax
    pmin, pmax, qmin, qmax = -2.5, 1.5, -2, 2

    # число точек по горизонтали и вертикали
    ppoints, qpoints = 1000, 1000
    # максимальное количество итераций
    max_iterations = 25

    # если ушли на это расстояние, считаем, что ушли на бесконечность
    infinity_border = 10

    fl = 100

    frames = []
    for t in range(0, fl):
        print(t)
        image = Image.new('RGB', (ppoints, qpoints), 'black')
        canvas = np.array(image)
        p, q = np.mgrid[pmin:pmax:(ppoints * 1j), qmin:qmax:(qpoints * 1j)]

        alpha = 2*t*math.pi/fl
        c = 1*math.cos(alpha) + 1j*math.sin(alpha)

        z = p + 1j*q
        value = np.zeros((ppoints, qpoints))

        for k in range(max_iterations):
            z = c*z*(1-z)
            mask = (np.abs(z) > infinity_border) & (value == np.array(0))
            canvas[mask] = np.array([255-k*10, 255-k*10, 255-k*10])
            z[mask] = np.nan

        image = Image.fromarray(canvas)
        frames.append(image)

    frames[0].save(
        'julia.gif',
        save_all=True,
        append_images=frames[1:],  # Срез который игнорирует первый кадр.
        optimize=True,
        duration=100,
        loop=0
    )
