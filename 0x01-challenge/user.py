#!/usr/bin/python3
"""
User class
"""


class User():
    """ User class definitions """

    def __init__(self):
        """ Constructor method """
        self.__email = None

    @property
    def email(self):
        """ Gets the value of the email """
        return self.__email

    @email.setter
    def email(self, value):
        """ Sets email to a new value """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":
    """User object """
    u = User()
    u.email = "john@snow.com"
    print(u.email)
