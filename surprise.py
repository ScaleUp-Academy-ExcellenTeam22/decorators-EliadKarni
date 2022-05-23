from functools import wraps
from typing import Callable


def surprise_decorator(func: Callable) -> Callable:
    """
    The decorator returns a function which prints "Surprise!".
    :param func: The ignored function.
    :return: A function which prints "Surprise!".
    """
    @wraps(func)
    def wrapper() -> None:
        """
        The Wrapper prints "Surprise!" and not execute the wrapped function.
        :return:None.
        """
        print("Surprise!")
    return wrapper


@surprise_decorator
def no_surprise() -> None:
    """
    The function prints I know it!.
    :return: None.
    """
    print("I know it!")


if __name__ == "__main__":
    no_surprise()
    print(no_surprise.__name__)
    print(no_surprise.__doc__)