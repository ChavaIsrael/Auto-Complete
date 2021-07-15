
from classes.trieNode import TrieNode


class Trie:

    def __init__(self):
        self.__root = self.getNode()
 
    def getNode(self):
        return TrieNode()
 
    def insert(self, word, source):
        # print(word)
        root = self.__root
        # print(word)
        length = len(word)
        for level in range(length):
            
            letter = word[level]
            if letter in [",", ","] or letter.isspace():
                letter = '#'
            if root.get_child_by_letter(letter) is None:
                root.add_child_by_letter(letter, TrieNode())
            root = root.get_child_by_letter(letter)
            # print(root.get_children())
        if root.get_positions_by_source(source) is None:
            root.add_source(source, level)
            if word == "understand":
                print("pppp")
        else:
            if word == "understand":
                print("rrr")
            root.add_position_to_source(source, position)    
        root.set_EOW(True)
 
    def search(self, word):
        root = self.__root
        length = len(word)
        for level in range(length):
            letter = word[level]
            print(letter)
            if root == None :
                print("root", root)
                return False
            # if root.get_children_by_index(letter) == {}:
            if level != len(word) - 1:
                print("let", letter)
                root = root.get_child_by_letter(letter)  
        return root.get_sources()
 