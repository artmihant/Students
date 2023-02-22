import matplotlib.pyplot as plt


def draw_rabbits_chart(r0, a, years, process):
    r = r0
    rabbits = []
    for i in range(years):
        rabbits.append(r)
        r = process(r, a)

    fig, ax = plt.subplots()
    plt.title(f'a = {a}')

    ax.plot(rabbits)
    ax.grid()
    #  Добавляем подписи к осям:
    ax.set_xlabel('years')
    ax.set_ylabel('rabbits')
    # plt.savefig(f'./rabbits1/{int(a*100000)}.png')
    plt.show()


if __name__ == '__main__':
    # общее число лет, пока мы выращиваем кроликов
    years = 300

    # итерационный процесс
    def process(r, a):
        return a * r * (1 - r)

    r0 = 0.3

    a = 3.6

    draw_rabbits_chart(r0, a, years, process)

    # for a in range(100):
    #     rabbits(i/10, years, process)
