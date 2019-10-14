from typing import Tuple, Union, Any
from abc import abstractmethod
from copy import deepcopy

from atoms.geo_object_base import GeoObject


class GeoObject2D(GeoObject):
    """
    TODO Think again whether GeoObject2D really has to defined all the abstract methods below.
    """

    def get_num_dimensions(self):
        return 2

    def get_smallest_containing_box(self) -> Any:
        # TODO (2) implement get_smallest_containing_box(self) for all the subclasses of GeoObject2D!
        assert False

    @abstractmethod
    def get_mirror_symmetry(
            self,
            first_point: Union[object, Tuple[Union[float, int], Union[float, int]]],
            second_point: Union[object, Tuple[Union[float, int], Union[float, int]]],
    ) -> Any:
        """
        TODO remove deepcopy for all abstract methods of this class and tests whether it doesn't break anything
        """
        pass
        return deepcopy(self)

    @abstractmethod
    def translate(self, delta: Union[object, Tuple[Union[float, int], Union[float, int]]]) -> Any:
        """
        TODO change the signature of this function and make proper changes at all subclasses
        """
        pass
        return deepcopy(self)

    @abstractmethod
    def rotate(self, angle: Union[float, int]) -> Any:
        pass
        return deepcopy(self)

    @abstractmethod
    def draw(self, ax) -> None:
        pass
