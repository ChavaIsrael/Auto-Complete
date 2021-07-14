from initialization.DBinitialization import initializeDB
from DB.archiveDB import ArchiveDB
from test import main

if __name__ == "__main__":
    archiveDB = ArchiveDB()
    t = initializeDB()
    print("{} ---- {}".format("the",t.search("understand")))
    # main()
    