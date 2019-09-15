from abc import ABC, abstractmethod

from utils import get_figure


class GeoObject2D(ABC):
    component_list = list()
    DEFAULT_KARGS = dict()

    def __init__(self, default_plotting_kargs, plotting_kargs_):
        GeoObject2D.component_list.append(self)

        self.plotting_kargs = GeoObject2D.DEFAULT_KARGS.copy()
        self.plotting_kargs.update(default_plotting_kargs)
        self.plotting_kargs.update(plotting_kargs_)

    def get_plotting_kargs(self):
        return self.plotting_kargs

    @abstractmethod
    def draw(self, ax):
        pass

    @staticmethod
    def draw_all_components(**kargs):
        fig = get_figure(1, 1, 0, 0, 0, 0, 10, 8)
        ax = fig.get_axes()[0]

        for component in GeoObject2D.component_list:
            component.draw(ax)

        ax.axis('equal')
        ax.axis('off')

        fig.show()

        return fig
