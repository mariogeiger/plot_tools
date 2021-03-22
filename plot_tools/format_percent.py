import matplotlib.ticker as ticker


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
