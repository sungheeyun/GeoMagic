from atoms.old_geo_object_2d import OldGeoObject2D


class OldArrow(OldGeoObject2D):

    ARROW_DEFAULT_PLOTTING_KARGS = dict(
        color="k", linewidth=0.5, head_width=6.0, head_length=10.0, length_includes_head=True
    )

    def __init__(self, start_coor, delta_pair, text=None, **kwargs):
        super(OldArrow, self).__init__(OldArrow.ARROW_DEFAULT_PLOTTING_KARGS, kwargs)
        self.start_coor = start_coor
        self.delta_pair = delta_pair

    def draw(self, ax):
        plotting_kwargs = self.get_plotting_kwargs()
        ax.arrow(self.start_coor[0], -self.start_coor[1], *self.delta_pair, **plotting_kwargs)
