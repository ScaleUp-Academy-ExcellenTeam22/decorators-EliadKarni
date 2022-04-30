import atexit
"""
The code does:
1. Demonstrate static method usage.
2. Demonstrate property method usage.
3. Prints good bye message at the end of the code's run.
"""


class Example:
    """
    The class used to demonstrate usage of static method and property method.
    """
    def __init__(self, value: int = 1):
        """
        The ctor sets the Example's object's member value to the received one.
        :param value: The wanted member value.
        """
        self.__member = value

    @staticmethod
    def static_method() -> None:
        """
        The static method prints the message: "static method used"
        :return: None
        """
        print("static method used")

    @property
    def member(self):
        """
        The method is a get method to the class': __member.
        It prints "get method used!" message and returns its value.
        :return: The class' __member value.
        """
        print("get method used!")
        return self.__member

    @member.setter
    def member(self, value: int) -> None:
        """
        The method is __member's set method.
        It prints: "set method used!", and set the __member value to the received one.
        :param value: The wanted __member new value.
        :return: None
        """
        print("set method used!")
        self.__member = value


@atexit.register
def print_good_bye():
    """
    The function prints good bye message at the end of the code's run.
    :return:
    """
    print("Good bye!")


if __name__ == "__main__":
    Example.static_method()

    example_obj = Example()
    print(example_obj.member)
    example_obj.member = 100
    print(example_obj.member)
