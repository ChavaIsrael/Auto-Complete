class TrieNode:

    def __init__(self):
        self.__children = {}
        self.__sources = {}
        self.__EOW = False

    def get_children(self):
        return self.__children      

    def get_child_by_letter(self, letter):
        return self.__children.get(letter)

    def add_child_by_letter(self, letter, child):
        self.__children[letter] = child

    def get_sources(self):
        return self.__sources  

    def get_offsets_by_source(self, source):
        return self.__sources.get(source)

    def add_source(self, source, offset):
        self.__sources[source] = offset

    def set_EOW(self, boolean):
        self.__EOW = boolean
    
    def get_EOW(self):
        return self.__EOW