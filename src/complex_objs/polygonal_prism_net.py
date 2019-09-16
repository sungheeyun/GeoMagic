from typing import Union

from atoms.polygon import Polygon
from atoms.vector2d import Vector2D
from complex_objs.polygonal_net_base import PolygonalNetBase


class PolygonalPrismNet(PolygonalNetBase):
    """
    Implements a net for a polygonal prism.
    """

    def __init__(self, polygon: Polygon, height: Union[float, int]):
        super(PolygonalPrismNet, self).__init__([polygon])

        self.polygon: Polygon = polygon
        self.height: float = float(height)

        self._initialize()

    def _initialize(self):
        vector_list = [vector for vector in self.polygon.vertex_coor_array]
        vector_list.append(vector_list[0])

        print(vector_list)

        first_point_list = vector_list[1:]
        second_point_list = vector_list[:-1]

        print(first_point_list)
        print(second_point_list)

        for idx in range(len(first_point_list)):
            first_point: Vector2D = Vector2D(first_point_list[idx])
            second_point: Vector2D = Vector2D(second_point_list[idx])

            print(first_point)
            print(second_point)

            rectangle: Polygon = Polygon.get_polygon_from_edges_and_angles_with_two_start_points(
                first_point, second_point, [self.height, (first_point - second_point).norm()], [90, 90]
            )

            self.add_object(rectangle)

        delta_vec: Vector2D = Vector2D(rectangle.vertex_coor_array[2]) - rectangle.vertex_coor_array[1]
        top_polygon = self.polygon.get_mirror_symmetry(first_point, second_point).translate(delta_vec)

        self.add_object(top_polygon)
