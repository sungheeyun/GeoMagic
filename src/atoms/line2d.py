import numpy as np

from atoms.geo_object_2d import GeoObject2D


class Line2D(GeoObject2D):
    LINE_DEFAULT_PLOTTING_KARGS = dict(
        color='k',
        linewidth=.5,
    )

    def __init__(self, start_coor, end_coor, **kargs):
        super(Line2D, self).__init__(Line2D.LINE_DEFAULT_PLOTTING_KARGS, kargs)
        self.start_coor = start_coor
        self.end_coor = end_coor

        self.coor_array = np.vstack((self.start_coor, self.end_coor))

    def draw(self, ax):
        plotting_kwargs = self.get_plotting_kargs()
        ax.plot(self.coor_array[:, 0], -self.coor_array[:, 1], **plotting_kwargs)
