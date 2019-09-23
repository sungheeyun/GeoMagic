from typing import Union, List
from copy import deepcopy

from numpy import array, ndarray, eye

from utils import get_angle
from atoms.polygon_2d import Polygon
from atoms.directed_line_segment_ndim import DirectedLineSegmentNDim
from atoms.box_ndim import BoxNDim
from complex_objs.polygon_2d_ndim import Polygon2DInNDim
from complex_objs.seg_collection_ndim import SegCollectionNDim
from complex_objs.polygon_ndim import PolygonNDim
from transformation.rotation_around_3d_segment import RotationAround3dSegment
from transformation.symmetry_around_line import SymmetryAroundLine
from transformation.unitary_coordinate_change_around_subspace_axis import UnitaryCoordinateChangeAroundSubspaceAxis
from transformation.composite_transformer import CompositeTransformation
from transformation.shifting import Shifting
from transformation.linear_transformation import LinearTransformation


class PolygonalPyramid3D(SegCollectionNDim):
    """
    Implements a 3-D polygonal pyramid.
    """

    def __init__(self, polygon: Polygon, top_vertex: List[Union[float, int]], z_ground: Union[float, int] = 0.0):
        super(PolygonalPyramid3D, self).__init__(3)

        self.bottom_polygon: Polygon2DInNDim = Polygon2DInNDim(polygon, [float(z_ground)])
        self.top_vertex: ndarray = array(top_vertex, float)

        self._initialize()

    def _initialize(self):
        for segment_ndim in self.bottom_polygon.segment_ndim_list:
            self.segment_ndim_list.append(deepcopy(segment_ndim))

        for bottom_point in self.bottom_polygon.point_array_2d:
            self.add_segments((bottom_point, self.top_vertex))

    def get_side_face_list(self) -> List[PolygonNDim]:
        side_face_list: List[PolygonNDim] = list()

        bottom_point_array_2d: ndarray = self.bottom_polygon.point_array_2d
        num_points = bottom_point_array_2d.shape[0]
        for idx, bottom_point1 in enumerate(bottom_point_array_2d):
            bottom_point2: ndarray = bottom_point_array_2d[(idx + 1) % num_points]
            side_face_list.append(PolygonNDim((bottom_point1, bottom_point2, self.top_vertex)))

        return side_face_list

    def to_2d_net(self) -> SegCollectionNDim:
        seg_collection_ndim_list: List[SegCollectionNDim] = list()
        center_of_gravity: ndarray = self.bottom_polygon.get_center_of_gravity_point()

        seg_collection_ndim_list.append(deepcopy(self.bottom_polygon))

        bottom_point_array_2d: ndarray = self.bottom_polygon.point_array_2d

        num_points = self.bottom_polygon.get_num_vertices()
        for idx, bottom_point1 in enumerate(bottom_point_array_2d):
            bottom_point2: ndarray = bottom_point_array_2d[(idx + 1) % num_points]
            directed_bottom_line: DirectedLineSegmentNDim = DirectedLineSegmentNDim(bottom_point1, bottom_point2)

            outer_point: ndarray = SymmetryAroundLine(directed_bottom_line)(center_of_gravity)

            projection_for_angle_calc: CompositeTransformation = CompositeTransformation(
                (
                    Shifting(-bottom_point1),
                    UnitaryCoordinateChangeAroundSubspaceAxis([bottom_point2 - bottom_point1]),
                    LinearTransformation(eye(3)[:2, :]),
                )
            )

            rotation_angle = get_angle(
                projection_for_angle_calc(self.top_vertex), projection_for_angle_calc(outer_point)
            )

            side_face: SegCollectionNDim = SegCollectionNDim(3, (bottom_point1, self.top_vertex, bottom_point2))
            rotation_around_bottom_segment: RotationAround3dSegment = RotationAround3dSegment(
                rotation_angle, directed_bottom_line
            )

            seg_collection_ndim_list.append(side_face.apply_transformation(rotation_around_bottom_segment))

        resulting_net: SegCollectionNDim = sum(seg_collection_ndim_list, SegCollectionNDim(self.get_num_dimensions()))

        smallest_containing_box: BoxNDim = resulting_net.get_smallest_containing_box()

        assert smallest_containing_box.lower_left_point[2] > -1e-6
        assert smallest_containing_box.upper_right_point[2] < 1e-6

        return resulting_net
