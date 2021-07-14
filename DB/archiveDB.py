import sys
sys.path.insert(0, '..')
from classes.TextAndSource import TextAndSource

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


    def addLine(self, lineText, Source):
        self.__textDict[self.__idIndicator] = TextAndSource(lineText, Source)
        print(self.__textDict[self.__idIndicator])
        self.__idIndicator += 1





# archiveDB = {
#     1:"fbhdjvk rbfkregbrjhg rfbrjkgrbgjr bri briugbrg",
#     2:"hgifkhfgiuhgiuer fghuir huirtuigh. 4 98 br98g "
# }


# wordsDB = {"u":[
#         {"uir":[(2,[13])]},
#         {"uer":[(2,[20,25])]}
#     ]
# }

# print(archiveDB[2][13:])