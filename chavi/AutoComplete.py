
archiveDB = {
    1:"This is a cat ,this",
    2:"This is a coffee",
    3:"Thia is the beautiful cat "
}
# This is a c

wordsDB = [
    {"This":[(1, [4, ])]

    }
]

from DB.archiveDB import *
import sys

def AutoComlete(sen):
    found_words = [sys.minint, sys.minint, sys.minint, sys.minint, sys.minint]
    score = 2 * len(sen)
    for word in sen:
        w_resoures = wordsDB[word.lower()]
        for resource in w_resoures:#arr
            for r in resource:
                archiveDB_key = r[0]
                archiveDB_value = r[1]
                for value in archiveDB_value:
                    string_to_equal = archiveDB_key[value]
                    for i in range(string_to_equal):
                        if string_to_equal != score[len(w_resoures) + i]:
                            score =- 1


            # place = archiveDB[resource]

       

