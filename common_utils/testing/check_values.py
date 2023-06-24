"""
This module provides a serie of functions that can be used to check the correct value of a variable or a serie of variables.

"""

from common_utils.exceptions.exceptions import NoneValuesException


def check_none_variables(*args) -> None:
    """Check if any of the variables passed into the function is None.

    Raises
    ------
    Exception
       If any of the variables is None, a custom Exception is raised.
    """
    if any(var is None for var in args):
        raise NoneValuesException
