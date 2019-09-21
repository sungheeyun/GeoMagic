from abc import abstractmethod

from atoms.geo_object_base import GeoObject
from transformation.transformer_base import TransformerBase


class GeoObjectNDim(GeoObject):
    @abstractmethod
    def apply_transformation(self, transformer: TransformerBase) -> GeoObject:
        pass
