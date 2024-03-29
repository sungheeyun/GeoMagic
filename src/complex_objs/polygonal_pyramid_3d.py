from typing import Union, List, Iterable
from copy import deepcopy

from numpy import array, ndarray, eye

from utils import get_angle
from atoms.polygon import Polygon
from atoms.directed_line_segment_ndim import DirectedLineSegmentNDim
from atoms.box_ndim import BoxNDim
from complex_objs.polygon_2d_ndim import Polygon2DInNDim
from complex_objs.line_segment_ndim_collection import LineSegmentNDimCollection
from complex_objs.polygon_ndim import PolygonNDim
from complex_objs.geo_object_collection_2d import GeoObjectCollection2D
from transformation.rotation_around_3d_segment import RotationAround3dSegment
from transformation.symmetry_around_line import SymmetryAroundLine
from transformation.unitary_coordinate_change_around_subspace_axis import (
    UnitaryCoordinateChangeAroundSubspaceAxis,
)
from transformation.composite_transformer import CompositeTransformation
from transformation.shifting import Shifting
from transformation.linear_transformation import LinearTransformation
from exceptions.geo_magic_exception import GeoMagicException


class PolygonalPyramid3D(LineSegmentNDimCollection):
    """
    Implements a 3-D polygonal pyramid.
    """

    def __init__(
        self,
        polygon: Polygon,
        apex_coordinate: Iterable[Union[float, int]],
        z_ground: Union[float, int] = 0.0,
    ):
        super(PolygonalPyramid3D, self).__init__(3)

        self.bottom_polygon: Polygon2DInNDim = Polygon2DInNDim(
            polygon, [float(z_ground)]
        )
        self.apex_coordinate: ndarray = array(apex_coordinate, float)

        self._initialize()

    def _check_attributes(self):
        if self.apex_coordinate.shape != (3,):
            raise GeoMagicException(
                f"`apex_coordinate` should represent a 3-d coordinate; its dimension is {str(self.apex_coordinate)}."
            )

    def _initialize(self):
        for segment_ndim in self.bottom_polygon.line_segment_ndim_list:
            self.line_segment_ndim_list.append(deepcopy(segment_ndim))

        for bottom_point in self.bottom_polygon.point_array_2d:
            self.add_segments((bottom_point, self.apex_coordinate))

    def get_side_face_list(self) -> List[PolygonNDim]:
        side_face_list: List[PolygonNDim] = list()

        bottom_point_array_2d: ndarray = self.bottom_polygon.point_array_2d
        num_points = bottom_point_array_2d.shape[0]
        for idx, bottom_point1 in enumerate(bottom_point_array_2d):
            bottom_point2: ndarray = bottom_point_array_2d[(idx + 1) % num_points]
            side_face_list.append(
                PolygonNDim((bottom_point1, bottom_point2, self.apex_coordinate))
            )

        return side_face_list

    def to_2d_net(self) -> GeoObjectCollection2D:
        # TODO (5) probably should be renamed as "to_net" ? since every net is a 2D net.. ??
        return self._to_3d_net().get_projection_onto_2d_plane(0, 1)

    def _to_3d_net(self) -> LineSegmentNDimCollection:
        seg_collection_ndim_list: List[LineSegmentNDimCollection] = list()
        center_of_gravity: ndarray = self.bottom_polygon.get_center_of_gravity_point()

        seg_collection_ndim_list.append(deepcopy(self.bottom_polygon))

        bottom_point_array_2d: ndarray = self.bottom_polygon.point_array_2d

        num_points = self.bottom_polygon.get_num_vertices()
        for idx, bottom_point1 in enumerate(bottom_point_array_2d):
            bottom_point2: ndarray = bottom_point_array_2d[(idx + 1) % num_points]
            directed_bottom_line: DirectedLineSegmentNDim = DirectedLineSegmentNDim(
                bottom_point1, bottom_point2
            )

            outer_point: ndarray = SymmetryAroundLine(directed_bottom_line)(
                center_of_gravity
            )

            projection_for_angle_calc: CompositeTransformation = CompositeTransformation(
                (
                    Shifting(-bottom_point1),
                    UnitaryCoordinateChangeAroundSubspaceAxis(
                        [bottom_point2 - bottom_point1]
                    ),
                    LinearTransformation(eye(3)[:2, :]),
                )
            )

            rotation_angle = get_angle(
                projection_for_angle_calc(self.apex_coordinate),
                projection_for_angle_calc(outer_point),
            )

            side_face: LineSegmentNDimCollection = LineSegmentNDimCollection(
                3, (bottom_point1, self.apex_coordinate, bottom_point2)
            )
            rotation_around_bottom_segment: RotationAround3dSegment = RotationAround3dSegment(
                rotation_angle, directed_bottom_line
            )

            seg_collection_ndim_list.append(
                side_face.apply_transformation(rotation_around_bottom_segment)
            )

        resulting_net: LineSegmentNDimCollection = sum(
            seg_collection_ndim_list,
            LineSegmentNDimCollection(self.get_num_dimensions()),
        )

        smallest_containing_box: BoxNDim = resulting_net.get_smallest_containing_box()

        assert smallest_containing_box.lower_left_point[2] > -1e-6
        assert smallest_containing_box.upper_right_point[2] < 1e-6

        return resulting_net
