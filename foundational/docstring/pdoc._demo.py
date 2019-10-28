import datetime as s
def my_method(self, a: str = None, b: str = None) -> typing.Set[str]:
    """
    Do something

    Args:
        a (str): The first parameter.
        b (str): The second parameter.

    Returns:
         Set: The return value. If result has values then Set of string, otherwise empty set

    """
    s._parse_hh_mm_ss_ff()
    return {a, b}

def module_level_function(param1, param2=None, *args, **kwargs):
    """This is an example of a module level function.
    Args:
        param1 (int): The first parameter.
        param2 (:obj:`str`, optional): The second parameter. Defaults to None.
            Second line of description should be indented.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        bool: True if successful, False otherwise.

        The return type is optional and may be specified at the beginning of
        the ``Returns`` section followed by a colon.

        The ``Returns`` section may span multiple lines and paragraphs.
        Following lines should be indented to match the first line.

        The ``Returns`` section supports any reStructuredText formatting,
        including literal blocks::

            {
                'param1': param1,
                'param2': param2
            }

    Raises:
        AttributeError: The ``Raises`` section is a list of all exceptions
            that are relevant to the interface.
        ValueError: If `param2` is equal to `param1`.

    """
    if param1 == param2:
        raise ValueError('param1 may not be equal to param2')
    return True

    my_method()