import unittest

from numpy import sqrt
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D

from drawing.utils import get_figure
from atoms.polygon_2d import Polygon
from atoms.regular_polygon import RegularPolygon
from complex_objs.seg_collection_ndim import SegCollectionNDim
from complex_objs.polygon_ndim import PolygonNDim
from complex_objs.polygonal_prism_3d import PolygonalPrism3D
from complex_objs.polygonal_pyramid_3d import PolygonalPyramid3D
from transformation.scaling import Scaling
from transformation.shift import Shift
from transformation.rotation import Rotation


class Test3DObjectTransformation(unittest.TestCase):

    SCALE_FACTOR = 2.0
    SHIFT_DELTA = 1.0
    ROTATION_ANGLE = 30.

    @classmethod
    def setUpClass(cls) -> None:
        # create 3-dimensional segment collection
        regular_triangle: Polygon = RegularPolygon(3)

        north_point = [0, 0, sqrt(2.0)]

        cls.regular_tetrahedron: PolygonalPyramid3D = PolygonalPyramid3D(regular_triangle, north_point)

    @classmethod
    def tearDownClass(cls) -> None:
        plt.show()

    def _test_polygonal_prism_3d(self) -> None:
        polygon: Polygon = RegularPolygon(5)
        # polygon = Polygon([[0, 0], [1, 1], [5, 8], [-2, 10], [-3, 1]])
        polygonal_prism_3d = PolygonalPrism3D(polygon, 2.0)

        fig: Figure = get_figure(1, 1, projection='3d')
        axis, = fig.get_axes()

        polygonal_prism_3d.draw3d(axis)

        axis.axis('off')

        fig.show()

        self.assertTrue(True)

    def _test_polygonal_pyramid_3d(self) -> None:
        polygon: Polygon = RegularPolygon(6)
        # polygon = Polygon([[0, 0], [1, 1], [-2, 10], [-3, 1]])
        polygonal_pyramid_3d = PolygonalPyramid3D(polygon, [0, 1, 3])

        fig: Figure = get_figure(1, 1, projection='3d')
        axis, = fig.get_axes()

        polygonal_pyramid_3d.draw3d(axis)

        axis.axis('off')

        fig.show()

        self.assertTrue(True)

    def test_basic_transformations(self) -> None:
        regular_tetrahedron: PolygonalPyramid3D = Test3DObjectTransformation.regular_tetrahedron

        scaling: Scaling = Scaling(Test3DObjectTransformation.SCALE_FACTOR)
        shift: Shift = Shift(Test3DObjectTransformation.SHIFT_DELTA)
        rotation: Rotation = Rotation(Test3DObjectTransformation.ROTATION_ANGLE)

        scaled_regular_tetrahedron: SegCollectionNDim = regular_tetrahedron.apply_transformation(scaling)
        shifted_regular_tetrahedron: SegCollectionNDim = regular_tetrahedron.apply_transformation(shift)
        rotated_regular_tetrahedron: SegCollectionNDim = regular_tetrahedron.apply_transformation(rotation)

        fig: Figure = get_figure(1, 2, projection='3d')
        axis1, axis2 = fig.get_axes()

        regular_tetrahedron.draw3d(axis1)
        regular_tetrahedron.draw3d(axis2)

        scaled_regular_tetrahedron.draw3d(axis1)
        shifted_regular_tetrahedron.draw3d(axis2)

        rotated_regular_tetrahedron.draw3d(axis1)

        axis1.axis('off')

        fig.show()

        self.assertEqual(True, True)

    def _test_polygon_ndim(self) -> None:
        regular_polygon = RegularPolygon(5)
        polygon_3d = PolygonNDim(regular_polygon, [0.0])

        fig: Figure = get_figure(1, 1, projection='3d')
        axis, = fig.get_axes()

        polygon_3d.draw3d(axis)

        axis.axis('off')

        fig.show()

        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
