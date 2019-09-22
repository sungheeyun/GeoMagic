import numpy as np

from atoms.geo_object_2d import GeoObject2D


class Box(GeoObject2D):

    BOX_DEFAULT_PLOTTING_KARGS = dict(facecolor="w", edgecolor="k", linewidth=0.5, zorder=5)

    def __init__(self, lt_coor, wh_pair, text=None, **kargs):
        super(Box, self).__init__(Box.BOX_DEFAULT_PLOTTING_KARGS, kargs)
        self.lt_coor = lt_coor
        self.wh_pair = wh_pair
        self.text = text

        left, top = self.lt_coor
        width, height = self.wh_pair

        self.x_coor_array = left + np.array([0, 0, 1, 1, 0]) * width
        self.y_coor_array = top + np.array([0, 1, 1, 0, 0]) * height

        self.mid_x_coor = left + width / 2.0
        self.mid_y_coor = top + height / 2.0

        self.text_x_coor = self.mid_x_coor
        self.text_y_coor = self.mid_y_coor

    def get_mid_x_coor(self):
        return self.mid_x_coor

    def draw(self, ax):
        plotting_kwargs = self.get_plotting_kargs()
        ax.fill(self.x_coor_array, -self.y_coor_array, **plotting_kwargs)

        if self.text:
            ax.text(self.text_x_coor, -self.text_y_coor, self.text, ha="center", va="center", zorder=6)
