
from classes.trieNode import TrieNode


class Trie:

    def __init__(self):
        self.__root = self.getNode()
 
    # def getNode(self):
    #     return TrieNode()
 
    def insert(self, word, position, source):
        # print(word)
        root = self.__root
        # print(word)
        length = len(word)
        for level in range(length):
            index = word[level]
            # if current character is not present
            # if word == "the":
            # print(index, root.get_children_by_index(index), "juh")
            if root.get_children_by_index(index) is None:
                root.add_children_by_letter(index, TrieNode())
            root = root.get_children_by_index(index)
            # print(root.get_children())
        if root.get_locatin_by_key(source) is None:
            root.set_source(source, position)
        else:
            root.set_location(source, position)    
        root.set_EOW(True)
 
    def search(self, word):
        root = self.__root
        length = len(word)
        for level in range(length):
            letter = word[level]
            print(letter)
            print(root.get_children_by_index(letter))
            if root == {}:
                return False
            # if root.get_children_by_index(letter) == {}:
            if level != len(word) - 1:
                root = root.get_children_by_index(letter)
        print(root.get_sources())    
        return root.get_EOW()
 