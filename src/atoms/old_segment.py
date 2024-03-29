import numpy as np

from atoms.old_geo_object_2d import OldGeoObject2D


class OldSegment(OldGeoObject2D):
    LINE_DEFAULT_PLOTTING_KARGS = dict(color="k", linewidth=0.5)

    def __init__(self, start_coor, end_coor, **kwargs):
        super(OldSegment, self).__init__(OldSegment.LINE_DEFAULT_PLOTTING_KARGS, kwargs)
        self.start_coor = start_coor
        self.end_coor = end_coor

        self.coor_array = np.vstack((self.start_coor, self.end_coor))

    def get_name(self) -> str:
        return f"OldSegment(({self.start_coor[0]}, {self.start_coor[1]}), ({self.end_coor[0]}, {self.end_coor[1]}))"

    def draw(self, ax):
        plotting_kwargs = self.get_plotting_kwargs()
        ax.plot(self.coor_array[:, 0], -self.coor_array[:, 1], **plotting_kwargs)
