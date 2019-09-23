import unittest

from numpy import vstack, hstack, zeros, sqrt
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D

from drawing.utils import get_figure
from atoms.polygon_2d import Polygon
from atoms.regular_polygon import RegularPolygon
from complex_objs.seg_collection_ndim import SegCollectionNDim
from complex_objs.polygon_2d_ndim import Polygon2DInNDim
from complex_objs.polygonal_prism_3d import PolygonalPrism3D
from complex_objs.polygonal_pyramid_3d import PolygonalPyramid3D

Axes3D


class TestSegmentCollection(unittest.TestCase):

    @classmethod
    def tearDownClass(cls) -> None:
        plt.show()

    def test_polygonal_prism_3d(self) -> None:
        polygon: Polygon = RegularPolygon(123)
        # polygon = Polygon([[0, 0], [1, 1], [5, 8], [-2, 10], [-3, 1]])
        polygonal_prism_3d = PolygonalPrism3D(polygon, 2.0)

        fig: Figure = get_figure(1, 1, projection="3d")
        axis, = fig.get_axes()

        polygonal_prism_3d.draw3d(axis)

        axis.axis("off")

        fig.show()

        self.assertTrue(True)

    def test_polygonal_pyramid_3d(self) -> None:
        polygon: Polygon = RegularPolygon(6)
        # polygon = Polygon([[0, 0], [1, 1], [-2, 10], [-3, 1]])
        polygonal_pyramid_3d = PolygonalPyramid3D(polygon, [0, 1, 3])

        fig: Figure = get_figure(1, 1, projection="3d")
        axis, = fig.get_axes()

        polygonal_pyramid_3d.draw3d(axis)

        axis.axis("off")

        fig.show()

        self.assertTrue(True)

    def test_basic_functionalities(self) -> None:
        # create 3-dimnesional segment collection
        regular_triangle = RegularPolygon(3)

        coor_2d_array = vstack((regular_triangle.vertex_coor_array, regular_triangle.vertex_coor_array[0]))
        coor_3d_array = hstack((coor_2d_array, zeros((coor_2d_array.shape[0], 1))))

        north_point = [0, 0, sqrt(2.0)]

        seg_collection_ndim = SegCollectionNDim(3, coor_3d_array)
        for idx in range(len(coor_3d_array) - 1):
            vertex = coor_3d_array[idx]
            print(vertex.shape)
            seg_collection_ndim.add_segments(vstack((vertex, north_point)))

        for segment in seg_collection_ndim.segment_ndim_list:
            print(segment)

        fig: Figure = get_figure(1, 2, projection="3d")
        axis1, axis2 = fig.get_axes()

        seg_collection_ndim.draw3d(axis1)
        seg_collection_ndim.draw3d(axis2)

        axis1.axis("off")

        fig.show()

        self.assertEqual(True, True)

    def test_polygon_ndim(self) -> None:
        regular_polygon = RegularPolygon(5)
        polygon_3d = Polygon2DInNDim(regular_polygon, [0.0])

        fig: Figure = get_figure(1, 1, projection="3d")
        axis, = fig.get_axes()

        polygon_3d.draw3d(axis)

        axis.axis("off")

        fig.show()

        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
