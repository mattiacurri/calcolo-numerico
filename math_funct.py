import matplotlib.pyplot as plt
import numpy as np

def f(x: float) -> float:
    return x - np.cos(x)

def h(x: float) -> float:
    return x - np.e**-x


def show_plot(function, s_range = -20, e_range = 20):
    plot = np.linspace(s_range, e_range)

    # setting the axes at the centre
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # plot the function
    plt.plot(plot, function(plot), 'r')
    plt.grid()
    # show the plot
    plt.show()


