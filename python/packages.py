# with subpackage import in __init__.py you can import main package
import mypackage

# and get access to subpackages
help(mypackage.myfolder)

# with module function import in __init__.py you can get access to function from package level
help(mypackage.myfolder.myfunc)

# relative import cheat sheet
# from . import module  # import module from current directory
# from .. import module  # import module from one directory up
# from .module import function  # import function from module in current directory
# from ..subpackage.module import function  # import function from module in subpackage from one directory up
