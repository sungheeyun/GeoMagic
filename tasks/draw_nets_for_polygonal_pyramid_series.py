import numpy as np
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from mpl_toolkits.mplot3d import Axes3D

from atoms.regular_polygon import RegularPolygon
from complex_objs.polygonal_pyramid_3d import PolygonalPyramid3D
from drawing.utils import get_figure

Axes3D


if __name__ == "__main__":

    num_vertices: int = 6
    polygon_radius: float = 2.0
    num_right_pyramids: int = 2
    num_pyramids: int = num_ridfasdfht_pyramids * 2 + 1
    pyramid_hegiht: float = 3.0
    axis_side_length_inches: float = 5.0
    far_right_apex_x_coordinate: float = 2.5

    apex_x_coordinate_array: np.ndarray = np.linspace(
        - far_right_apex_x_coordinate,
        far_right_apex_x_coordinate,
        num_pyramids
    )

    polygon: RegularPolygon = RegularPolygon(num_vertices, (0, 0), 1, 0.0)

    fig, ax = plt.subplots()
    polygon.draw(ax)
    ax.axis('equal')
    fig.show()

    figure: Figure = get_figure(
        num_pyramids,
        1,
        vertical_padding=0.0,
        projection="3d",
    )

    axis: Axes
    idx: int
    for idx, axis in enumerate(figure.get_axes()):
        apex_x_coordinate: float = apex_x_coordinate_array[idx]

        polygonal_pyramid: PolygonalPyramid3D = PolygonalPyramid3D(
            polygon,
            (apex_x_coordinate, 0.0, pyramid_hegiht)
        )
        polygonal_pyramid.draw3d(axis)

        each_figure: Figure = get_figure(1, 1, 0, 0, 0, 0, axis_side_length_inches, axis_side_length_inches)
        polygonal_pyramid.to_2d_net().draw2d(each_figure.get_axes()[0])
        each_figure.show()

    figure.show()

    if "__file__" in dir():
        plt.show()
