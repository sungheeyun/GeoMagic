import unittest

from numpy import sqrt, ones, ndarray
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from mpl_toolkits.mplot3d import Axes3D

from drawing.utils import get_figure
from atoms.polygon import Polygon
from atoms.regular_polygon import RegularPolygon
from complex_objs.line_segment_ndim_collection import LineSegmentNDimCollection
from complex_objs.polygonal_prism_3d import PolygonalPrism3D
from complex_objs.polygonal_pyramid_3d import PolygonalPyramid3D
from transformation.scaling import Scaling
from transformation.shifting import Shifting
from transformation.rotation_around_subspace_axis import RotationAroundSubspaceAxis

Axes3D


class Test3DObjectTransformation(unittest.TestCase):

    SCALE_FACTOR = 1.1
    SHIFT_DELTA = 1.0
    ROTATION_ANGLE = 30.0

    @classmethod
    def setUpClass(cls) -> None:
        # create 3-dimensional segment collection
        regular_triangle: Polygon = RegularPolygon(3)

        north_point = [0, 0, sqrt(2.0)]

        cls.regular_tetrahedron: PolygonalPyramid3D = PolygonalPyramid3D(
            regular_triangle, north_point
        )

    def test_polygonal_prism_3d(self) -> None:
        polygon: Polygon = RegularPolygon(5)
        # base_polygon = Polygon([[0, 0], [1, 1], [5, 8], [-2, 10], [-3, 1]])
        polygonal_prism_3d = PolygonalPrism3D(polygon, 2.0)

        fig: Figure = get_figure(1, 1, projection="3d")
        axis, = fig.get_axes()

        polygonal_prism_3d.draw3d(axis)

        axis.axis("off")

        fig.show()

        self.assertTrue(True)

    def test_beths_curriculum(self) -> None:
        polygon: Polygon = RegularPolygon(4)
        # base_polygon = Polygon([[0, 0], [1, 1], [-2, 10], [-3, 1]])
        polygonal_pyramid_3d = PolygonalPyramid3D(polygon, [0, 1, sqrt(2)])

        fig: Figure = plt.figure(figsize=(6, 10))
        axis1: Axes = fig.add_subplot(211, projection="3d")
        axis2: Axes = fig.add_subplot(212)

        # polygonal_pyramid_3d.draw3d(axis1)
        polygonal_pyramid_3d.draw3d(axis1)
        polygonal_pyramid_3d.to_2d_net().draw(axis2, color="k")

        # axis1.axis("off")
        axis2.axis("off")
        axis2.axis("equal")

        fig.show()

        self.assertTrue(True)

    def test_polygonal_pyramid_3d(self) -> None:
        polygon: Polygon = RegularPolygon(6)
        # base_polygon = Polygon([[0, 0], [1, 1], [-2, 10], [-3, 1]])
        polygonal_pyramid_3d = PolygonalPyramid3D(polygon, [0, 1, 2.5])

        fig: Figure = plt.figure(figsize=(6, 10))
        axis1: Axes = fig.add_subplot(211, projection="3d")
        axis2: Axes = fig.add_subplot(212)

        # polygonal_pyramid_3d.draw3d(axis1)
        polygonal_pyramid_3d.draw3d(axis1)
        polygonal_pyramid_3d.to_2d_net().draw(axis2, color="k")

        # axis1.axis("off")
        axis2.axis("off")
        axis2.axis("equal")

        fig.show()

        self.assertTrue(True)

    def test_basic_transformations(self) -> None:
        regular_tetrahedron: PolygonalPyramid3D = Test3DObjectTransformation.regular_tetrahedron

        shift_vector: ndarray = Test3DObjectTransformation.SHIFT_DELTA * ones(regular_tetrahedron.get_num_dimensions())

        scaling: Scaling = Scaling(Test3DObjectTransformation.SCALE_FACTOR)
        shift: Shifting = Shifting(shift_vector)
        rotation: RotationAroundSubspaceAxis = RotationAroundSubspaceAxis(
            Test3DObjectTransformation.ROTATION_ANGLE, ((0, 0, 1),)
        )

        scaled_regular_tetrahedron: LineSegmentNDimCollection = regular_tetrahedron.apply_transformation(
            scaling
        )
        shifted_regular_tetrahedron: LineSegmentNDimCollection = regular_tetrahedron.apply_transformation(
            shift
        )
        rotated_regular_tetrahedron: LineSegmentNDimCollection = regular_tetrahedron.apply_transformation(
            rotation
        )

        fig: Figure = get_figure(1, 1, projection="3d")
        axis1 = fig.get_axes()[0]

        regular_tetrahedron.draw3d(axis1)

        scaled_regular_tetrahedron.draw3d(axis1)
        shifted_regular_tetrahedron.draw3d(axis1)

        for idx in range(10):
            rotated_regular_tetrahedron: LineSegmentNDimCollection = rotated_regular_tetrahedron.apply_transformation(
                rotation
            )
            rotated_regular_tetrahedron.draw3d(axis1)

        rotated_regular_tetrahedron.draw3d(axis1)

        axis1.axis("off")

        fig.show()

        self.assertEqual(True, True)


if __name__ == "__main__":
    unittest.main()
