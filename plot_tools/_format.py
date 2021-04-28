import matplotlib.ticker as ticker
import math


@ticker.FuncFormatter
def format_percent(x, _pos=None):
    """
    plt.gca().yaxis.set_major_formatter(format_percent)
    """
    x = 100 * x
    if abs(x - round(x)) > 0.05:
        return r"${:.1f}\%$".format(x)
    else:
        return r"${:.0f}\%$".format(x)


@ticker.FuncFormatter
def format_binary(x, _pos=None):
    """
    plt.gca().yaxis.set_major_formatter(format_binary)
    """
    if x <= 0:
        return x
    e = math.log2(x)
    return fr"$2^{{{e:.0f}}}$"


@ticker.FuncFormatter
def format_empty(x, _pos=None):
    """
    plt.gca().yaxis.set_minor_formatter(format_empty)
    """
    return ""
