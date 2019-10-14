from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from atoms.regular_polygon import RegularPolygon
from complex_objs.polygonal_prism_3d import PolygonalPrism3D

Axes3D


if __name__ == "__main__":

    num_vertices = 20
    polygon = RegularPolygon(num_vertices, (0, 0), 2, 0.0)

    # obj3d = PolygonalPyramid3D(base_polygon, (2, 0, 4))
    obj3d = PolygonalPrism3D(polygon, 2)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    obj3d.draw3d(ax)

    fig.show()
    plt.show()

    if "__file__" in dir():
        plt.show()
