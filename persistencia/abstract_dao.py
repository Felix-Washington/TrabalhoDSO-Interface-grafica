import pickle
from abc import ABC

class AbstractDAO(ABC):
    def __init__(self, datasource=""):
        self.__datasource = datasource
        self.__object_cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__object_cache, open(self.__datasource,'wb'))

    def __load(self):
        self.__object_cache = pickle.load(open(self.__datasource,'rb'))

    def add(self, key, obj):
        self.__object_cache[key] = obj
        self.__dump()

    def get(self, key):
        try:
            return self.__object_cache[key]
        except KeyError:
            pass

    def get_all(self):
        return self.__object_cache.values()

    def remove(self, key):
        try:
            self.__object_cache.pop(key)
        except KeyError:
            pass