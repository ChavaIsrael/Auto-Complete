from classes.trie import Trie
from os import getcwd,walk
# ,chdir,sep,pardir,listdirs
from DB.archiveDB import ArchiveDB


def initializeDB():
    path = getcwd()
    global_path = path + '/2021-archive'
    small_path = global_path + '/temp_files'
    initialize_from_directories(small_path)
    return insert_archiveDB_to_trie()
        
def initialize_from_directories(path):
    for subdir, dirs, files in walk(path):
        # print(subdir)
        if subdir:
            for dir in dirs:
                initialize_from_directories(path + '/' + dir)
        # print(dirs)
        # print(files)
        for file in files:
            initialize_from_file(path + '/' + file)



def initialize_from_file(file_path):
    archiveDB = ArchiveDB()
    try:
        with open(file_path, encoding='utf-8') as f:
        # Read the entire file, where each line will be an item in a the returned list
            lines = f.readlines()
            for line in lines:
                # print(line)
                archiveDB.add_line(line, file_path)
    except IOError as e:
        print("Error:", e)
    

def insert_archiveDB_to_trie():
    archiveDB = ArchiveDB()
    trie = Trie()
    pos = 0
    for id, textAndSource in archiveDB.get_db().items():
        text = textAndSource.get_text()
        words = text.split()
        for word in words:
            trie.insert(word, pos, id)
            pos += len(word)
    return trie        
