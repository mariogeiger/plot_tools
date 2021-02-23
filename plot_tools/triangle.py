import math
import matplotlib.pyplot as plt


def log_log_triangle(x1, x2, y1, y2=None, slope=None, text=None):
    if y2 is None:
        y2 = y1 * (x2 / x1)**slope

    if text is None:
        text = math.log(y2 / y1) / math.log(x2 / x1)

    plt.plot([x1, x2, x2, x1], [y1, y2, y1, y1], 'k-')
    plt.annotate(
        text,
        ((x1*x2**2)**(1/3), (y1**2*y2)**(1/3)),
        horizontalalignment='center',
        verticalalignment='center'
    )
