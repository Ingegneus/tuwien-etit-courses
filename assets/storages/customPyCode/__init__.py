import os
import glob

# Automatically import all .py files in the current folder
modules = glob.glob(os.path.join(os.path.dirname(__file__), "*.py"))
__all__ = [os.path.basename(f)[:-3] for f in modules if f.endswith(".py") and not f.endswith("__init__.py")]

# Import all files
for module in __all__:
    exec(f"from .{module} import *")