# TODO - (5) Take a look at below todo list written a long ago.
# TODO - (5) remove idx: int in front of for-loop since it's not needed
# TODO - (5) move all plt.show() in tearDown static methods to below if __name__ == "__main__"
# TODO - (3) change return type of draw to None
# TODO - (3) think of whether or not we should put '2d' to some class names (hence file names).
#  Regardless of the results, make the naming consistent.
# TODO - (1) change the part that does something like "a: A = None" to declare the variable type to "a: A"
#  everywhere it happens
# TODO - (3) take care of the parts marked by XXX
# TODO - (1) test rotation on 2d object, too.
# TODO - (??) store objects with rec. boxes
# TODO - (1) properly implement get_name for object_2d
# TODO - (2) get A and b for symmetric_around_line transformation and subclass it from affine transformation
# TODO - (4) change assert to exceptions

# TODO - DONE - check coordinate direction for 3d rotation. something seems odd
# TODO - DONE change kargs to kwargs and pargs to args
# TODO - DONE/CC attach plotting kargs to each object
#  -> decided not to do this.. instead, moved those old classes under OldGeoObject2D,
#  -> i.e., made them subclasses of OldGeoObject2D,
# TODO - DONE - make prism net generic (e.g., by implementing mirror symmetry transformation, etc.)
# TODO - DONE - figure out draw2d and draw3d return types and make changes to code
#  -> decided to return None
