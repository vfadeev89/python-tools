"""
Singleton class decorator.

Usage:

from singleton import singleton

@singleton
class SimpleSingleton:
    def __init__(self, number):
        self.number = number

one = SimpleSingleton(10)
"""

class singleton:
    def __init__(self, a_class):
        self.a_class = a_class
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.a_class(*args, **kwargs)
        return self.instance
