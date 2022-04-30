from functools import wraps
from typing import Callable
"""
The code is a decorator factory.
The in the factory decorator receives an argument type, and validates in the func call, that the received
argument is from the defined type.
If it is, the factory returns the decorated function.
Else, it raise a TypeError exception.
"""


def decorator_factory(correct_type: type) -> Callable:
    """
    The decorator factory receives a variable type.
    If the decorated function receives an argument which not from the received type, a TypeError exception raised.
    Else, it returns the decorated function.
    :param correct_type: The wanted decorated argument type.
    :return: The decorated function.
    :raise: TypeError: if the received argument's type is not as correct_type's value.
    """
    def decorator(func: Callable) -> Callable:
        """
        The decorator returns a func wrapped in an argument's type validation.
        :param func: The function wants to be wrapped.
        :return: func function wrapped in type validation.
        :raise: TypeError: If the argument is not from the defined correct_type.
        """
        @wraps(func)
        def wrapper(arg: object) -> object:
            """
            The wrapper returns the received func return value if its argument's type is the defined correct_type.
            :param arg: The func's argument.
            :return: func's return value.
            :raise TypeError: if the received argument's type is not as the defined correct_type.
            """
            if type(arg) != correct_type:
                raise TypeError
            return func(arg)
        return wrapper
    return decorator


@decorator_factory(int)
def print_value(val: int) -> None:
    """
    The function prints the received value.
    It decorated so if the argument's type is not int, it raises TypeError exception.
    :param val: The value wants to be printed.
    :return: None
    :raise: TypeError: if the argument's type is not int.
    """
    print("The value is: ", val)


if __name__ == "__main__":
    try:
        print_value("7")
    except TypeError:
        print("Type error exception raised.")
    print_value(80)
