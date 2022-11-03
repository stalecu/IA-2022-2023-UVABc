import inspect

from .lab_03 import *

# Add all of the packages inside the modules that don't begin with __
# (those are by convention private functions)
__all__ = [
    o.__name__
    for _, o in inspect.getmembers(inspect.getmodule(__name__ + ".lab_03"))
    if inspect.isfunction(o)
    and o.__module__ == inspect.getmodule(__name__ + ".lab_03")
    and not o.__name__.startswith("__")
]
