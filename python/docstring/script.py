"""This is module docstring."""


def cool_function(cool_param1: int, cool_param2: str = "", cool_param3 = False) -> int:
    """This is function docstring.

    Parameters
    ----------
    cool_param1 : int
        Description of param1.
    cool_param2 : str
        Description of param2. (Default value = "")
    cool_param3 :
        Description of param3. (Default value = False)

    Returns
    -------
    int
    
    """
    cool_value = 1
    return cool_value


class CoolClass:
    """This is class doctring."""
    def __init__(self, cool_param):
        self.cool_param = cool_param

    def cool_method(self, cool_param) -> bool:
        """This is method docstring.

        Parameters
        ----------
        cool_param :
            Description of cool_param.

        Returns
        -------
        bool
        
        """
        return self.cool_param == cool_param
