import sys
sys.path.insert(0, '..')
from classes.textAndSource import TextAndSource

# Singleton class
class ArchiveDB:
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            self = cls.__instance
            self.__textDict = {}
            self.__idIndicator = 0
        return cls.__instance


    def add_line(self, lineText, Source):
        self.__textDict[self.__idIndicator] = TextAndSource(lineText, Source)
        # print(self.__textDict[self.__idIndicator])
        self.__idIndicator += 1

    def get_db(self):
        return self.__textDict