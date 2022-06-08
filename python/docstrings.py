# pyment -w -o numpydoc script.py  # generate NumPy style docstring template
# pyment -w -o google script.py  # generate Google style docstring template

import python.docstring
import python.docstring.script

help(python.docstring)
print(python.docstring.__doc__)  # print package docstring

help(python.docstring.script)
print(python.docstring.script.__doc__)  # print module docstring

help(python.docstring.script.cool_function)
print(python.docstring.script.cool_function.__doc__)  # print function docstring

help(python.docstring.script.CoolClass)
print(python.docstring.script.CoolClass.__doc__)  # print class docstring

help(python.docstring.script.CoolClass.cool_method)  # not working
print(python.docstring.script.CoolClass.cool_method.__doc__)  # print method docstring
