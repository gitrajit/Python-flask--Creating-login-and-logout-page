import sqlite3

def get_connecttion():
   # Connect to SQLite database (creates the file if it doesn't exist)
    return sqlite3.connect('my_database.db',detect_types=sqlite3.PARSE_DECLTYPES |
                             sqlite3.PARSE_COLNAMES)

if __name__ == "__main__":
    get_connecttion()