from functools import wraps
from typing import Callable


def twice_decorator(func: Callable) -> Callable:
    """
    The decorator execute the decorated function twice.
    :param func: The function wanted to be execute twice.
    :return: A function which execute func twice.
    """
    @wraps(func)
    def wrapper(*args: list, **kwargs: dict) -> None:
        """
        The wrapper execute func twice.
        :param args: The function's arguments.
        :param kwargs: The function's arguments.
        :return: None.
        """
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper


@twice_decorator
def function() -> None:
    """
    The function prints "Hello!!"
    :return:
    """
    print("Hello!!")


if __name__ == "__main__":
    function()
