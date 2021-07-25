# from trie import Trie
from DB.trie import Trie
from os import getcwd,walk
from DB.archiveDB import ArchiveDB


def initializeDB():
    path = getcwd()
    global_path = path + '/2021-archive'
    small_path = global_path + '/RFC'
    initialize_from_directories(small_path)
    return insert_archiveDB_to_trie()
        
def initialize_from_directories(path):
    for subdir, dirs, files in walk(path):
        if subdir:
            for dir in dirs:
                initialize_from_directories(path + '/' + dir)

        for file in files:
            initialize_from_file(path + '/' + file)



def initialize_from_file(file_path):
    archiveDB = ArchiveDB()
    try:
        with open(file_path, encoding='utf-8') as f:
        # Read the entire file, where each line will be an item in a the returned list
            lines = f.readlines()
            for line in lines:
                archiveDB.add_line(line, file_path)
    except IOError as e:
        print("Error:", e)
    


def insert_archiveDB_to_trie():
    archiveDB = ArchiveDB()
    trie = Trie()
    for id, text_and_source in archiveDB.get_db().items():
        text = text_and_source.get_text()
        trie.insert_text(text, id)
    return trie        
