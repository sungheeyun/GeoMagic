from typing import Any
from abc import abstractmethod

from matplotlib.axes import Axes

from atoms.geo_object_base import GeoObject
from transformation.transformation_base import TransformationBase


class GeoObjectNDim(GeoObject):
    @abstractmethod
    def apply_transformation(self, transformer: TransformationBase) -> Any:
        pass

    @abstractmethod
    def draw2d(self, axis: Axes, **kwargs):
        pass

    @abstractmethod
    def draw3d(self, axis: Axes, **kwargs):
        pass

    @abstractmethod
    def get_smallest_containing_box(self) -> GeoObject:
        pass
