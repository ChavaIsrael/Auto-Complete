from AutoCompleteData import AutoCompleteData
from trieNode import TrieNode

class Trie:

    def __init__(self):
        self.__root = self.getNode()
 
    def getNode(self):
        return TrieNode()
 
    def insert(self, sen, location, source):
        root = self.__root
        length = len(sen)
        for level in range(length):
            index = sen[level]
            # if current character is not present
            if root.get_child_by_letter(index) is None:
                root.add_child_by_letter(index, self.getNode())
            root = root.get_child_by_letter(index)
        # if root.get_sou(source) is None:
        #     root.set_source(source, location)
        # else:
        root.add_position_to_source(source, AutoCompleteData())
        root.set_EOW(True)
 
    def search(self, word):
        root = self.__root
        length = len(word)
        for level in range(length):
            letter = word[level]
            if root is None or root.get_child_by_letter(letter) is {}:
                return False
            root = root.get_child_by_letter(letter)  
        return root.get_sources()
 