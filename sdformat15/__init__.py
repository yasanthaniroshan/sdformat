import os
import sys
import ctypes

# Get the directory of the package
_package_dir = os.path.dirname(__file__)
_so_path = os.path.join(_package_dir, "libsdformat15.so")

# Load shared library explicitly
try:
    ctypes.CDLL(_so_path, mode=ctypes.RTLD_GLOBAL)
except OSError as e:
    raise ImportError(f"Could not load shared library: {_so_path}\nError: {e}")
    sys.exit(1)

# Now, import actual package contents
try:
    import sdformat15
except ImportError as e:
    raise ImportError(f"Failed to import sdformat15 after loading shared library: {e}")
    sys.exit(1)
