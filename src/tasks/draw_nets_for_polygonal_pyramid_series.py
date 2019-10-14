from typing import List
import logging
import os

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from mpl_toolkits.mplot3d import Axes3D

from atoms.regular_polygon import RegularPolygon
from atoms.box_ndim import BoxNDim
from complex_objs.polygonal_pyramid_3d import PolygonalPyramid3D
from complex_objs.geo_object_collection_2d import GeoObjectCollection2D
from drawing.utils import get_figure
from utils import set_logger_config, FIGURES_DIR

Axes3D
logger = logging.getLogger("geomagic")


if __name__ == "__main__":
    set_logger_config(logger, __file__, logging.INFO)

    num_vertices: int = 6
    polygon_radius: float = 2.0
    num_right_pyramids: int = 3
    num_pyramids: int = num_right_pyramids * 2 + 1
    pyramid_height: float = 3.0
    far_right_apex_x_coordinate: float = 1.5

    # polygonal pyramids

    polygon: RegularPolygon = RegularPolygon(num_vertices, (0, 0), 1, 0.0)

    apex_x_coordinate_array: np.ndarray = np.linspace(
        -far_right_apex_x_coordinate, far_right_apex_x_coordinate, num_pyramids
    )

    polygonal_pyramid_list: List[PolygonalPyramid3D] = [
        PolygonalPyramid3D(polygon, (apex_x_coordinate, 0.0, pyramid_height))
        for apex_x_coordinate in apex_x_coordinate_array
    ]

    figure: Figure = get_figure(num_pyramids, 1, vertical_padding=0.0, projection="3d")
    idx: int
    axis: Axes
    for idx, axis in enumerate(figure.get_axes()):
        polygonal_pyramid = polygonal_pyramid_list[idx]
        polygonal_pyramid.draw3d(axis)

    figure.show()

    # polygonal pyramid nets

    polygonal_pyramid_net_list: List[GeoObjectCollection2D] = [
        polygonal_pyramid.to_2d_net() for polygonal_pyramid in polygonal_pyramid_list
    ]

    smallest_containing_box: BoxNDim = sum(
        [
            polygonal_pyramid_net.get_smallest_containing_box()
            for polygonal_pyramid_net in polygonal_pyramid_net_list
        ]
    )

    logger.info(f"smallest_containing_box = {smallest_containing_box}")

    x_min: float
    x_max: float
    y_min: float
    y_max: float

    x_min, y_min = smallest_containing_box.lower_left_point
    x_max, y_max = smallest_containing_box.upper_right_point

    x_lim = x_min, x_max
    y_lim = y_min, y_max

    axis_width: float
    axis_height: float
    axis_width, axis_height = smallest_containing_box.get_edge_length_array()

    for idx, polygonal_pyramid_net in enumerate(polygonal_pyramid_net_list):
        figure: Figure = get_figure(
            1, 1, 0.5, 0.5, 0.5, 0.5, axis_width, axis_height
        )
        axis: Axes = figure.get_axes()[0]

        polygonal_pyramid_net.draw(axis)

        # axis.grid(True)
        axis.set_xlim(x_lim)
        axis.set_ylim(y_lim)

        figure_save_file_full_path = os.path.join(FIGURES_DIR, f"polygonal_pyramid_net_{idx}.pdf")
        figure.savefig(figure_save_file_full_path)

        figure.show()

    if "__file__" in dir():
        plt.show()
