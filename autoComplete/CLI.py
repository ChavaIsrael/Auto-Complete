from DB.initializationDB import initializeDB
from autoComplete.search import search_all_options
from autoComplete.autoCompleteData import AutoCompleteData
import sys
import time


class CLI():
    def __init__(self):
        self.__sentence = ""
        self.__trie = None

    def get_sentence(self):
        return self.__sentence

    def set_word(self, sentence):
        self.__sentence = sentence

    def search_sentence(self):
        res = self.__trie.search(self.__sentence)
        return res


    def print_5_completes(self, res):
        min_score = [AutoCompleteData("", "", "2", sys.maxsize), AutoCompleteData("", "", "2", sys.maxsize), AutoCompleteData("", "", "2", sys.maxsize),AutoCompleteData("", "", "2", sys.maxsize), AutoCompleteData("", "", "2", sys.maxsize)]
        
        #If there are 5 sentences to complete                      
        if len(res) >= 5:
            for r in res:
                print(r)
        #If not
        else:
            suggestions = search_all_options(self.__trie, self.__sentence)
            for sug in suggestions:
                for max in range(5): 
                    flag = True
                    if sug.get_score() < min_score[max].get_score():
                        for m in range(5):
                            if min_score[m] == sug:
                                if min_score[m].get_score() > sug.get_score():
                                    min_score[m] = sug
                                else:
                                    flag = False   
                                break  
                        if flag:    
                            min_score[max] = sug
                        break
            for sug in min_score:
                if sug.get_score() != sys.maxsize:
                    print(sug.get_completed_sentence())  

    def run(self):
        print("Loading...")
        self.__trie = initializeDB()
        while self.__sentence != "q!":
            self.__sentence = input("enter a sentence to search- to quite enter q!:")
            res = self.search_sentence()
            self.print_5_completes(res)
        print("Please wait some seconds")    

