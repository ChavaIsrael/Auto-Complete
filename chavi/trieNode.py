class TrieNode:

    def __init__(self):
        self.__letter = None
        self.__children = {}
        self.__sources = {}
        self.__EOW = False

    def get_letter(self):
        return self.__letter

    def set_letter(self, letter):
        self.__letter = letter

    def get_children(self):
        return self.__children      

    def get_children_by_index(self, letter):
        # print(self.__children)
        # print(self.__children.get(letter))
        return self.__children.get(letter)

    def set_children_by_index(self, letter, children):
        self.__children[letter] = children

    def get_sources(self):
        return self.__sources  

    def get_locatin_by_key(self, key):
        return self.__sources.get(key)

    def set_source(self, source, location):
        self.__sources[source] = [location]

    def set_location(self, source, location):
        self.__sources[source].append(location)

    def set_EOW(self, boolean):
        self.__EOW = boolean
    
    def get_EOW(self):
        return self.__EOW