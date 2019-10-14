import os

from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from atoms.regular_polygon import RegularPolygon
from drawing.utils import get_figure
from utils import FIGURES_DIR

if __name__ == "__main__":

    num_vertices: int = 5

    polygon: RegularPolygon = RegularPolygon(num_vertices, (0, 0), 2, 0.0)
    polygon: RegularPolygon = RegularPolygon(
        num_vertices=5,
        center=(0, 1),
        radius=3,
        angle_of_one_point=60
    )

    figure: Figure = get_figure(1, 1)
    axis: Axes = figure.get_axes()[0]
    polygon.draw(axis)

    for angle in [0, 60, 90, 180]:
        polygon: RegularPolygon = RegularPolygon(
            num_vertices=5,
            center=(0, 1),
            radius=3,
            angle_of_one_point=angle
        )
        polygon.draw(axis)

    axis.set_xlim((-5, 5))
    axis.set_ylim((-5, 5))

    # axis.axis("off")
    axis.axis("equal")
    axis.grid(True)

    figure.show()

    figure.savefig(os.path.join(FIGURES_DIR, "regular_polygon"))

    if "__file__" in dir():
        plt.show()
