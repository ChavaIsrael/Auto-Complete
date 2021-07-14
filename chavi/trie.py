from trieNode import TrieNode

class Trie:

    def __init__(self):
        self.__root = self.getNode()
 
    def getNode(self):
        return TrieNode()
 
    def insert(self, word, location, source):
        root = self.__root
        length = len(word)
        for level in range(length):
            index = word[level]
            # if current character is not present
            if root.get_children_by_index(index) is None:
                root.set_children_by_index(index, self.getNode())
            root = root.get_children_by_index(index)
        if root.get_locatin_by_key(source) is None:
            root.set_source(source, location)
        else:
            root.set_location(source, location)
        root.set_EOW(True)
 
    def search(self, word):
        root = self.__root
        length = len(word)
        for level in range(length):
            letter = word[level]
            if root.get_children_by_index(letter) is {}:
                return False
            root = root.get_children_by_index(letter)
        print(root.get_sources())    
        return root.get_EOW()
 