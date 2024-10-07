import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# PHYSICS #

Alpha = -2.5

def F(t,p):
    return Alpha*p

P_0 = 1.0

T_min, T_max = 0, 4


@np.vectorize
def P_analitical_solution(t):
    """ решение для проверки """
    return P_0*np.exp(Alpha*t)

# NUMERIC #

StepsNumber = 100

# PREPROCESSING #

T = np.linspace(T_min, T_max, StepsNumber+1)

P_cl = np.zeros(StepsNumber+1, dtype=np.float64)
P_an = P_analitical_solution(T) # сразу считаем аналитическое решение для всех точек.

DeltaT = (T_max-T_min)/StepsNumber


# FIGURE SETUP #

fig, ax = plt.subplots()


# за счет посчитанного аналитического решения, график заранее "знает" свою область отображения
LineCalculated = ax.plot(T[0], P_cl[0], label=f'P расчитанное')[0]
LineAnalitical = ax.plot(T, P_an, label=f'P аналитическое')[0]

ax.set(xlabel='T', ylabel='P')
ax.legend()


def init_animation():
    """ Инициализация. Установка начального условия. """

    P_cl.fill(0)
    P_cl[0] = P_0

    LineCalculated.set_data(T[0], P_cl[0])
    LineAnalitical.set_data(T[0], P_an[0])

    return (LineCalculated, LineAnalitical)


def loop_animation(i):
    """ Главный цикл вычисления/анимации """

    P_cl[i+1] = P_cl[i] + F(T[i], P_cl[i]) * DeltaT

    LineCalculated.set_data(T[:i+1], P_cl[:i+1])
    LineAnalitical.set_data(T[:i+1], P_an[:i+1])

    return (LineCalculated,LineAnalitical)


ani = animation.FuncAnimation(
    fig=fig, 
    func=loop_animation, 
    init_func=init_animation, 
    frames=StepsNumber, 
    interval=3000/StepsNumber, 
    repeat=True, 
    repeat_delay=1000
)

plt.show()

