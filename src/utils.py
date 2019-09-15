import numpy as np
from matplotlib import pyplot as plt


def get_figure(
        nrow, ncol,
        l_margin, r_margin, b_margin, t_margin,
        spWidth, spHeight,
        wPadding=0.0, hPadding=0.0,
        **kargs
):
    num = kargs.pop('num', None)

    l_margin, r_margin, b_margin, t_margin \
        = float(l_margin), float(r_margin), float(b_margin), float(t_margin)

    def tolist(value, n):
        assert n >= 0, ('FATAL', n)
        if n == 0:
            return []

        if isinstance(value, int):
            value = float(value)

        if isinstance(value, float):
            value = [value] * n

        return np.array(value, float)

    spWidthList = tolist(spWidth, ncol)
    spHeightList = tolist(spHeight, nrow)
    wPaddingList = tolist(wPadding, ncol-1)
    hPaddingList = tolist(hPadding, nrow-1)

    figwidth = l_margin + r_margin + sum(spWidthList) + sum(wPaddingList)
    figheight = b_margin + t_margin + sum(spHeightList) + sum(hPaddingList)

    fig = plt.figure(num=num, figsize=(figwidth, figheight))

    for i in range(nrow):
        for j in range(ncol):
            left_position = (l_margin + sum(spWidthList[:j]) + sum(wPaddingList[:j])) / figwidth
            bottom_position = (b_margin + sum(spHeightList[i + 1:]) + sum(hPaddingList[i:])) / figheight
            width = spWidthList[j] / figwidth
            height = spHeightList[i] / figheight

            fig.add_axes([left_position, bottom_position, width, height], **kargs)

    return fig
