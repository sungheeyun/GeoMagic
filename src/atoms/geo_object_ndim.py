from typing import Any
from abc import abstractmethod

from matplotlib.axes import Axes

from atoms.geo_object_base import GeoObject
from atoms.geo_object_2d import GeoObject2D
from transformation.transformation_base import TransformationBase


class GeoObjectNDim(GeoObject):
    @abstractmethod
    def apply_transformation(self, transformer: TransformationBase) -> Any:
        pass

    @abstractmethod
    def draw2d(self, axis: Axes, **kwargs):
        # TODO reconsider the name.. it's actually drawing the projection onto x-y plane, a very specific 2D plane
        pass

    @abstractmethod
    def draw3d(self, axis: Axes, **kwargs):
        pass

    @abstractmethod
    def get_projection_onto_2d_plane(self, first_coordinate_index: int, second_coordinate_index: int) -> GeoObject2D:
        """
        Returns a projection of this GeoObjectNDim onto 2D plane by choosing two coordinate values.
        Note that this is NOT a generic projection onto 2D plane, rather to one of those n(n+2)/2 vertical planes.
        TODO Thus I need to find a better name for this method!

        Parameters
        ----------
        first_coordinate_index:
            The 1st coordinate index
        second_coordinate_index:
            The 2st coordinate index
        Returns
        -------
        geo_object_2d:
            The resulting GeoObeject2D instance obtained by the projection.
        """
        pass
