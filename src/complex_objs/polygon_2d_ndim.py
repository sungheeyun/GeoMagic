from typing import List, Union

from numpy import array, hstack, ndarray

from atoms.polygon_2d import Polygon
from complex_objs.polygon_ndim import PolygonNDim


class Polygon2DInNDim(PolygonNDim):
    """
    Implements a polygon in 2-D plane in N-dimensional space.
    """

    def __init__(self, polygon: Polygon, rest_coordinate: List[Union[float, int]]):
        self.polygon: Polygon = polygon
        self.rest_coordinate: ndarray = array(rest_coordinate, float)

        rest_coordinate_2d_array: ndarray = array([self.rest_coordinate])
        # coor_2d_array: ndarray = vstack((self.polygon.vertex_coor_array, self.polygon.vertex_coor_array[0]))
        coor_2d_array: ndarray = self.polygon.vertex_coor_array

        coor_3d_array: ndarray = hstack(
            (coor_2d_array, rest_coordinate_2d_array.repeat(coor_2d_array.shape[0], axis=0))
        )

        super(Polygon2DInNDim, self).__init__(coor_3d_array)
