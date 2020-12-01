import pickle
from abc import ABC

class AbstractDAO(ABC):
    def __init__(self, datasource=""):
        self.__datasource = datasource
        self.__object_cache = {}
        try:
            self.load()
        except FileNotFoundError:
            self.dump()
    def dump(self):
        pass
    def load(self):
        pass
    def add(self):
        pass
    def get(self, key):
        pass