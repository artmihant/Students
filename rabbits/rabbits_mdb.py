import numpy as np
import matplotlib.pyplot as plt


def draw_mandelbrot_rabbits_chart(a_range, r_max, r0, years):
    # число пикселей в одной единице
    dpu = 200

    x_points, y_points = dpu*(a_range[0][1]-a_range[0][0]), dpu*(a_range[1][1]-a_range[1][0])
    # число точек по горизонтали и вертикали
    # если ушли на это расстояние, считаем, что ушли на бесконечность
    image = np.zeros((y_points, x_points))
    # image — это двумерный массив, в котором будет записана наша картинка
    # по умолчанию он заполнен нулями
    for ix, x in enumerate(np.linspace(*a_range[0], x_points)):
        for iy, y in enumerate(np.linspace(*a_range[1], y_points)):
            a = x + 1j * y
            # буквой j обозначается мнимая единица: чтобы Python понимал, что речь
            # идёт о комплексном числе, а не о переменной j, мы пишем 1j
            r = r0
            for k in range(years):
                r = process(r, a)
                # Самая Главная Формула
                if abs(r) > r_max:
                    # если r достаточно большое, считаем, что последовательость
                    # ушла на бесконечность
                    # или уйдёт
                    # можно доказать, что r_max можно взять равным 1
                    image[iy, ix] = years-k+1
                    # находимся вне M: отметить точку как белую
                    break

    plt.title(f'Years = {years}')
    plt.xticks([])
    plt.yticks([])
    # выключим метки на осях

    # cmap in ['viridis', 'plasma', 'inferno', 'magma', 'cividis']
    plt.imshow(image, cmap="inferno")
    # plt.savefig(f'./rabbits_mdb/test.png')
    plt.show()


if __name__ == '__main__':
    def process(r, a):
        return a * r * (1 - r)

    # максимальное r
    r_max = 1

    r0 = 0.5

    years = 50

    # пусть a = x + iy и x меняется в диапазоне от 0 до 4; y - от -2 до 2
    a_range = [[-2, 4], [-2, 2]]

    # for years in range(100):
    draw_mandelbrot_rabbits_chart(a_range, r_max, r0, years)
