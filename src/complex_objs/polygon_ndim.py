from typing import Iterable, Union
from numpy import ndarray, array, vstack

from complex_objs.seg_collection_ndim import SegCollectionNDim


class PolygonNDim(SegCollectionNDim):
    """
    Implements connected N-dimensional segments.
    """
    def __init__(self, iter_iter: Iterable[Iterable[Union[float, int]]]):
        self.point_array_2d: ndarray = array(iter_iter, float)
        super(PolygonNDim, self).__init__(
            self.point_array_2d.shape[1],
            vstack((self.point_array_2d, self.point_array_2d[0]))
        )
