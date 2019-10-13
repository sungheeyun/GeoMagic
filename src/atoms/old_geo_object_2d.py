from typing import List

from matplotlib.axes import Axes
from matplotlib.patches import Patch

from atoms.geo_object_base import GeoObject


class OldGeoObject2D(GeoObject):
    component_list: List[GeoObject] = list()
    DEFAULT_KWARGS = dict()

    def __init__(self, default_plotting_kwargs, plotting_kwargs_):
        OldGeoObject2D.component_list.append(self)

        self.plotting_kwargs = OldGeoObject2D.DEFAULT_KWARGS.copy()
        self.plotting_kwargs.update(default_plotting_kwargs)
        self.plotting_kwargs.update(plotting_kwargs_)

    def get_name(self) -> str:
        return "OldGeoObject2D (Needs to be overridden!)"

    def get_num_dimensions(self):
        return 2

    def get_plotting_kwargs(self) -> dict:
        return self.plotting_kwargs

    def update_plotting_kwargs(self, **kwargs) -> None:
        self.plotting_kwargs.udpate(**kwargs)

    def draw_all_components(axis: Axes) -> List[Patch]:
        # figure = get_figure(1, 1, 0, 0, 0, 0, 10, 8)
        # axis = figure.get_axes()[0]

        return [component.draw(axis) for component in OldGeoObject2D.component_list]

        # axis.axis('equal')
        # axis.axis('off')

        # figure.show()
