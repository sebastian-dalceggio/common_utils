def check_none_variables(*args) -> None:
    """Check if any of the variables passed into the function is None.

    Raises
    ------
    Exception
       If any of the variables is None, a custom Exception is raised.
    """
    if any(var == None for var in args):
        raise Exception("At least one variable is None")