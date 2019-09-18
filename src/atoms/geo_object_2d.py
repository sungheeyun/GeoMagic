from abc import abstractmethod
from typing import Tuple, Union

from matplotlib.axes import Axes
from matplotlib.patches import Patch

from atoms.geo_object_base import GeoObject


class GeoObject2D(GeoObject):
    component_list = list()
    DEFAULT_KARGS = dict()

    def __init__(self, default_plotting_kargs, plotting_kargs_):
        GeoObject2D.component_list.append(self)

        self.plotting_kargs = GeoObject2D.DEFAULT_KARGS.copy()
        self.plotting_kargs.update(default_plotting_kargs)
        self.plotting_kargs.update(plotting_kargs_)

    def get_num_dimensions(self):
        return 2

    @abstractmethod
    def get_mirror_symmetry(
        self,
        first_point: Union[object, Tuple[Union[float, int], Union[float, int]]],
        second_point: Union[object, Tuple[Union[float, int], Union[float, int]]],
    ) -> object:
        pass

    @abstractmethod
    def translate(self, delta: Union[object, Tuple[Union[float, int], Union[float, int]]]) -> object:
        pass

    @abstractmethod
    def rotate(self, angle: Union[float, int]) -> object:
        pass

    def get_plotting_kargs(self) -> dict:
        return self.plotting_kargs

    def update_plotting_kargs(self, **kargs) -> None:
        self.plotting_kargs.udpate(**kargs)

    @abstractmethod
    def draw(self, ax) -> Patch:
        pass

    def draw_all_components(axis: Axes) -> None:
        # fig = get_figure(1, 1, 0, 0, 0, 0, 10, 8)
        # ax = fig.get_axes()[0]

        for component in GeoObject2D.component_list:
            component.draw(axis)

        # axis.axis('equal')
        # axis.axis('off')

        # fig.show()
