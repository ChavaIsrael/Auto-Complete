class TrieNode:

    def __init__(self):
        # self.__letter = None
        self.__children = {}
        self.__sources = {}
        self.__EOW = False

    # def get_letter(self):
    #     return self.__letter

    # def set_letter(self, letter):
    #     self.__letter = letter

    def get_children(self):
        return self.__children      

    def get_child_by_letter(self, letter):
        # print(self.__children)
        # print(self.__children.get(letter))
        return self.__children.get(letter)

    def add_child_by_letter(self, letter, child):
        self.__children[letter] = child
        # print(self.__children[letter])

    def get_sources(self):
        return self.__sources  

    def get_positions_by_source(self, source):
        return self.__sources.get(source)

    def add_source(self, source, position):
        self.__sources.append(position)

    def add_position_to_source(self, source, position):
        self.__sources[source].append(position)

    def set_EOW(self, boolean):
        self.__EOW = boolean
    
    def get_EOW(self):
        return self.__EOW