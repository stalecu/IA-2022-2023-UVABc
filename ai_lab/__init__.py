import sys, importlib, pkgutil

__all__ = []


def pkg_submodules(package, recursive=True):
    """Return a list of all submodules in a given package, recursively by default"""

    # If the package is a string, we try to import it like that, otherwise
    # return nothing in case there's an error.
    if isinstance(package, str):
        try:
            package = importlib.import_module(package)
        except ImportError:
            return []

    # Once we imported the main package, we walk through all of the packages
    # (optionally recursively) and import them.
    submodules = []
    for _, name, is_pkg in pkgutil.walk_packages(package.__path__):
        full_name = package.__name__ + "." + name

        try:
            submodules.append(importlib.import_module(full_name))
        except ImportError:
            continue

        if recursive and is_pkg:
            submodules += pkg_submodules(full_name)

    __all__.append(submodules)

    return submodules


pkg_submodules(sys.modules[__name__], recursive=True)
