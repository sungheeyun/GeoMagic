from typing import List
import unittest

from numpy import sqrt
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D

from drawing.utils import get_figure
from atoms.polygon_2d import Polygon
from atoms.regular_polygon import RegularPolygon
from complex_objs.seg_collection_ndim import SegCollectionNDim
from complex_objs.polygonal_prism_3d import PolygonalPrism3D
from complex_objs.polygonal_pyramid_3d import PolygonalPyramid3D
from complex_objs.polygon_ndim import PolygonNDim
from transformation.transformer_base import TransformerBase
from transformation.scaling import Scaling
from transformation.shifting import Shifting
from transformation.rotation import Rotation
from transformation.transformations import get_3d_rotaiton_around_segment


class Test3DObjectTransformation(unittest.TestCase):

    SCALE_FACTOR = 1.1
    SHIFT_DELTA = 1.0
    ROTATION_ANGLE = 30.0

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

        fig: Figure = get_figure(1, 1, projection="3d")
        axis, = fig.get_axes()

        polygonal_prism_3d.draw3d(axis)

        axis.axis("off")

        fig.show()

        self.assertTrue(True)

    def test_polygonal_pyramid_3d(self) -> None:
        polygon: Polygon = RegularPolygon(9)
        # polygon = Polygon([[0, 0], [1, 1], [-2, 10], [-3, 1]])
        polygonal_pyramid_3d = PolygonalPyramid3D(polygon, [0, 1, 3])

        side_face_list: List[PolygonNDim] = polygonal_pyramid_3d.get_side_face_list()

        fig: Figure = get_figure(1, 1, projection="3d")
        axis, = fig.get_axes()

        polygonal_pyramid_3d.draw3d(axis)

        for side_face in side_face_list:
            rotation: TransformerBase = get_3d_rotaiton_around_segment(80, side_face.segment_ndim_list[0])
            side_face.apply_transformation(rotation).draw3d(axis)

        axis.axis("off")

        fig.show()

        self.assertTrue(True)

    def _test_basic_transformations(self) -> None:
        regular_tetrahedron: PolygonalPyramid3D = Test3DObjectTransformation.regular_tetrahedron

        scaling: Scaling = Scaling(Test3DObjectTransformation.SCALE_FACTOR)
        shift: Shifting = Shifting(Test3DObjectTransformation.SHIFT_DELTA)
        rotation: Rotation = Rotation(Test3DObjectTransformation.ROTATION_ANGLE, ((0, 0, 1),))

        scaled_regular_tetrahedron: SegCollectionNDim = regular_tetrahedron.apply_transformation(scaling)
        shifted_regular_tetrahedron: SegCollectionNDim = regular_tetrahedron.apply_transformation(shift)
        rotated_regular_tetrahedron: SegCollectionNDim = regular_tetrahedron.apply_transformation(rotation)

        fig: Figure = get_figure(1, 1, projection="3d")
        axis1 = fig.get_axes()[0]

        regular_tetrahedron.draw3d(axis1)

        scaled_regular_tetrahedron.draw3d(axis1)
        shifted_regular_tetrahedron.draw3d(axis1)

        for idx in range(10):
            rotated_regular_tetrahedron: SegCollectionNDim = rotated_regular_tetrahedron.apply_transformation(rotation)
            rotated_regular_tetrahedron.draw3d(axis1)

        rotated_regular_tetrahedron.draw3d(axis1)

        axis1.axis("off")

        fig.show()

        self.assertEqual(True, True)


if __name__ == "__main__":
    unittest.main()
