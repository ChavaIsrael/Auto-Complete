from DB.archiveDB import ArchiveDB
from DB.trieNode import TrieNode
import sys, time

class Trie:

    def __init__(self):
        self.__root = self.getNode()
 
    def getNode(self):
        return TrieNode()
 
    def insert(self, text, source, offset):
        root = self.__root
        length = len(text)
        for level in range(length):
            letter = text[level]
            if letter == " " and level < length - 1 and text[level + 1] == " ":
                continue
            if letter in [",", ".", " "]:
                letter = '#'
            if root.get_child_by_letter(letter) is None:
                root.add_child_by_letter(letter, self.getNode())
            if level != len(text) - 1:  
                root = root.get_child_by_letter(letter)
        root.add_source(source, offset)   
        root.set_EOW(True)

    def insert_text(self, text, source):
        for i in range(len(text) - 1):
            self.insert(text[i:], source, i)
            
    def result(self, sources):
        archiveDB = ArchiveDB()
        sum = 0
        texts = []
        sources = sources[::-1]
        for source in sources:
            for key in source.keys():
                if sum >= 5:
                    break
                texts += [archiveDB.get_db()[key].get_text()]
                sum += 1
        return texts    

    def search(self, text):
        text = text.lower()
        root = self.__root
        length = len(text)
        for level in range(length):
            letter = text[level]
            if root.get_child_by_letter(letter) is None: 
                return []       
            root = root.get_child_by_letter(letter)    
        if root.get_sources() == {}:
            children = self.all_children(root)
            return self.result(children)
        children = self.all_children(root)
        children = children + [root.get_sources()]
        return self.result(children)


    def all_children(self, root):
        children = [root]
        source_arr = []
        while children != [] and len(source_arr) < 5:
            cld = children.pop(0)
            if cld == {}:
                continue
            for child in cld.get_children().values():
                if child.get_sources() != {}:
                    source_arr.append(child.get_sources())
                children.append(child)                                    
        return source_arr


 