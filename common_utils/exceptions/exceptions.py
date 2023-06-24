"""
This module provides a serie of custom Exceptions used in this package.

"""


class NoneValuesException(Exception):
    """
    Custom Exception used when one or more values is None.

    """

    def __init__(self, message: str) -> None:
        """
        NoneValuesException constructor

        Parameters
        ----------
        message : str
            Message to be displayed after the exception is raised
        """
        super().__init__(message)
