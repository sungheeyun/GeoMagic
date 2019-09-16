import os

from matplotlib.axes import Axes
from matplotlib.figure import Figure

from atoms.regular_polygon import RegularPolygon
from atoms.vector2d import Vector2D
from drawing.utils import get_figure
from utils import FIGURES_DIR

if __name__ == '__main__':

    num_vertices: int = 5

    # polygon: RegularPolygon = RegularPolygon(num_vertices, (0, 0), 2, 0.0)
    polygon: RegularPolygon = RegularPolygon(num_vertices, Vector2D((0, 0)), 2, 0.0)

    figure: Figure = get_figure(1, 1)
    axis: Axes = figure.get_axes()[0]
    polygon.draw(axis)

    axis.set_xlim((-5, 5))
    axis.set_ylim((-5, 5))

    axis.axis('off')
    axis.axis('equal')

    figure.show()

    figure.savefig(os.path.join(FIGURES_DIR, 'regular_polygon'))
