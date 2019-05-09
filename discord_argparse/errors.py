"""
MIT License

Copyright (c) 2019 lukeciel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from discord.ext import commands

__all__ = ["InvalidArgumentValueError", "UnknownArgumentError"]


class InvalidArgumentValueError(commands.BadArgument):
    """ Exception raised when an argument cannot be converted with a
    converter. """

    def __init__(self, name, value):
        super().__init__(
            "Invalid argument value passed for {0}: {1}".format(name, value)
        )
        self.name = name
        self.value = value


class UnknownArgumentError(commands.BadArgument):
    """ Exception raised when an unknown argument is passed. """

    def __init__(self, name):
        super().__init__("Unknown named argument {0}".format(name))
        self.name = name