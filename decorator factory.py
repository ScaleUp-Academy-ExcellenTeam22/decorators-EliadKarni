from functools import wraps
from typing import Callable


def type_validator(correct_type: type) -> Callable:
    """
    The decorator factory receives a variable type.
    If the decorated function receives an argument which is not from the received type, a TypeError exception is raised.
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


@type_validator(int)
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
    print_value("7")
    print_value(80)
