from abc import abstractmethod
from typing import Tuple, Union, List
from copy import deepcopy

from matplotlib.axes import Axes
from matplotlib.patches import Patch

from atoms.geo_object_base import GeoObject


class GeoObject2D(GeoObject):
    component_list: List[GeoObject] = list()
    DEFAULT_KARGS = dict()

    def __init__(self, default_plotting_kargs, plotting_kargs_):
        GeoObject2D.component_list.append(self)

        self.plotting_kargs = GeoObject2D.DEFAULT_KARGS.copy()
        self.plotting_kargs.update(default_plotting_kargs)
        self.plotting_kargs.update(plotting_kargs_)

    def get_num_dimensions(self):
        return 2

    # @abstractmethod
    def get_mirror_symmetry(
        self,
        first_point: Union[object, Tuple[Union[float, int], Union[float, int]]],
        second_point: Union[object, Tuple[Union[float, int], Union[float, int]]],
    ) -> object:
        pass
        return deepcopy(self)

    # @abstractmethod
    def translate(self, delta: Union[object, Tuple[Union[float, int], Union[float, int]]]) -> object:
        pass
        return deepcopy(self)

    # @abstractmethod
    def rotate(self, angle: Union[float, int]) -> object:
        pass
        return deepcopy(self)

    def get_plotting_kargs(self) -> dict:
        return self.plotting_kargs

    def update_plotting_kargs(self, **kargs) -> None:
        self.plotting_kargs.udpate(**kargs)

    @abstractmethod
    def draw(self, ax) -> Patch:
        pass

    def draw_all_components(axis: Axes) -> List[Patch]:
        # fig = get_figure(1, 1, 0, 0, 0, 0, 10, 8)
        # axis = fig.get_axes()[0]

        return [component.draw(axis) for component in GeoObject2D.component_list]

        # axis.axis('equal')
        # axis.axis('off')

        # fig.show()
