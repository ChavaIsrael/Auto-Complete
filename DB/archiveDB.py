import sys
from DB.textAndSource import TextAndSource

sys.path.insert(0, '..')


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
        self.__idIndicator += 1

    def get_db(self):
        return self.__textDict