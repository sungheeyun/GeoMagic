from abc import abstractmethod
from typing import Tuple, Union, List
from copy import deepcopy

from matplotlib.axes import Axes
from matplotlib.patches import Patch

from atoms.geo_object_base import GeoObject


class GeoObject2D(GeoObject):
    component_list: List[GeoObject] = list()
    DEFAULT_KARGS = dict()

    def __init__(self, default_plotting_kwargs, plotting_kwargs_):
        GeoObject2D.component_list.append(self)

        self.plotting_kwargs = GeoObject2D.DEFAULT_KARGS.copy()
        self.plotting_kwargs.update(default_plotting_kwargs)
        self.plotting_kwargs.update(plotting_kwargs_)

    def get_num_dimensions(self):
        return 2

    @abstractmethod
    def get_mirror_symmetry(
        self,
        first_point: Union[object, Tuple[Union[float, int], Union[float, int]]],
        second_point: Union[object, Tuple[Union[float, int], Union[float, int]]],
    ) -> object:
        pass
        return deepcopy(self)

    @abstractmethod
    def translate(self, delta: Union[object, Tuple[Union[float, int], Union[float, int]]]) -> object:
        pass
        return deepcopy(self)

    @abstractmethod
    def rotate(self, angle: Union[float, int]) -> object:
        pass
        return deepcopy(self)

    def get_plotting_kwargs(self) -> dict:
        return self.plotting_kwargs

    def update_plotting_kwargs(self, **kwargs) -> None:
        self.plotting_kwargs.udpate(**kwargs)

    @abstractmethod
    def draw(self, ax) -> Patch:
        pass

    def draw_all_components(axis: Axes) -> List[Patch]:
        # figure = get_figure(1, 1, 0, 0, 0, 0, 10, 8)
        # axis = figure.get_axes()[0]

        return [component.draw(axis) for component in GeoObject2D.component_list]

        # axis.axis('equal')
        # axis.axis('off')

        # figure.show()
