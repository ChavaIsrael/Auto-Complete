from os import getcwd,walk,chdir,sep,pardir,listdir
# import sys
# sys.path.insert(0, '..')
from DB.archiveDB import ArchiveDB


def initializeDB():
    path = getcwd()
    global_path = path + '/2021-archive'
    small_path = global_path + '/temp_files'
    # print(walk(small_path))
    initializeFromDirectories(small_path)
        
def initializeFromDirectories(path):
    for subdir, dirs, files in walk(path):
        print(subdir)
        if subdir:
            for dir in dirs:
                initializeFromDirectories(path + '/' + dir)
        print(dirs)
        print(files)
        for file in files:
            initializeFromFile(path + '/' + file)



def initializeFromFile(file_path):
    archiveDB = ArchiveDB()
    try:
        with open(file_path, encoding='utf-8') as f:
        # Read the entire file, where each line will be an item in a the returned list
            lines = f.readlines()
            for line in lines:
                print(line)
                archiveDB.addLine(line, file_path)

        
    except IOError as e:
        print("Error:", e)
    

