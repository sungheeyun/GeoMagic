from typing import Union

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.figure import Figure


def get_figure(
    num_rows: int,
    num_cols: int,
    left_margin: Union[int, float] = 1.0,
    right_margin: Union[int, float] = 1.0,
    bottom_margin: Union[int, float] = 1.0,
    top_margin: Union[int, float] = 1.0,
    axis_width: Union[int, float] = 6.0,
    axis_height: Union[int, float] = 5.0,
    horizontal_padding: Union[int, float] = 1.0,
    vertical_padding: Union[int, float] = 1.0,
    **kwargs
) -> Figure:
    left_margin = float(left_margin)
    right_margin = float(right_margin)
    bottom_margin = float(bottom_margin)
    top_margin = float(top_margin)
    axis_width = float(axis_width)
    axis_height = float(axis_height)
    horizontal_padding = float(horizontal_padding)
    vertical_padding = float(vertical_padding)

    num = kwargs.pop("num", None)

    def tolist(value, n):
        assert n >= 0, ("FATAL", n)
        if n == 0:
            return []

        if isinstance(value, int):
            value = float(value)

        if isinstance(value, float):
            value = [value] * n

        return np.array(value, float)

    axis_width_list = tolist(axis_width, num_cols)
    axis_height_list = tolist(axis_height, num_rows)
    horizontal_padding_list = tolist(horizontal_padding, num_cols - 1)
    vertical_padding_list = tolist(vertical_padding, num_rows - 1)

    figure_width = left_margin + right_margin + sum(axis_width_list) + sum(horizontal_padding_list)
    figure_height = bottom_margin + top_margin + sum(axis_height_list) + sum(vertical_padding_list)

    fig = plt.figure(num=num, figsize=(figure_width, figure_height))

    for i in range(num_rows):
        for j in range(num_cols):
            left_position = (left_margin + sum(axis_width_list[:j]) + sum(horizontal_padding_list[:j])) / figure_width
            bottom_position = (
                bottom_margin + sum(axis_height_list[i + 1:]) + sum(vertical_padding_list[i:])
            ) / figure_height
            width = axis_width_list[j] / figure_width
            height = axis_height_list[i] / figure_height

            fig.add_axes([left_position, bottom_position, width, height], **kwargs)

    return fig
