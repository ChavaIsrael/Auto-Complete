

from trie import Trie

def insert_to_trie(trie, text,id):
    # Construct trie
    for i in range(len(text)):
        word = text[i]
        trie.insert(word, len(word)+i+ 1, id)


def main():

    # Input keys (use only 'a' through 'z' and lower case)
    keys =["the","a","there","anaswe","any",
            "by","their", "the"]
    keyss =["the","a","there","anaswe","any",
    "by","their", "the"]
    # keys = ["th"]
    output = ["Not present in trie",
              "Present in trie"]
 
    # Trie object
    t = Trie()
 
    insertToTrie(t,keys,0)
    insertToTrie(t,keyss,1)

    # list_words(t)
    # Search for different keys

   
    print("{} ---- {}".format("the",t.search("the")))
    # print("{} ---- {}".format("these",output[t.search("these")]))
    print("{} ---- {}".format("their",output[t.search("their")]))
    # print("{} ---- {}".format("thaw",output[t.search("thaw")]))
 
if __name__ == '__main__':
    main()