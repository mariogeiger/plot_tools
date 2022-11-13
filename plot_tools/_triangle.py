import math
import matplotlib.pyplot as plt


def log_log_triangle(
    x1: float,
    x2: float,
    y1: float,
    y2: float = None,
    *,
    slope: float = None,
    text: str = None,
):
    if y2 is None and slope is None:
        raise ValueError("Either y2 or slope must be specified")

    if y2 is None:
        y2 = y1 * (x2 / x1) ** slope

    if text is None:
        text = f"{math.log(y2 / y1) / math.log(x2 / x1):.2f}"

    plt.plot([x1, x2, x2, x1], [y1, y2, y1, y1], "k-")

    plt.annotate(
        text,
        ((x1 * x2**2) ** (1 / 3), (y1**2 * y2) ** (1 / 3)),
        horizontalalignment="center",
        verticalalignment="center",
    )
