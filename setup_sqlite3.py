import sqlite3
from sqlite3 import Error

db_file = 'hsfl_lnn.db'

sql_setup = [['CREATE TABLE "latestGrades" ( `id` INTEGER PRIMARY KEY AUTOINCREMENT, `courseid` INTEGER UNIQUE, `course` TEXT NOT NULL, `study_course` TEXT, `study_course_id` TEXT, `file` BLOB, `timestamp` TEXT )'],
        ['CREATE TABLE "latestNews" ( `id` INTEGER PRIMARY KEY AUTOINCREMENT, `title` TEXT NOT NULL UNIQUE, `date` TEXT NOT NULL, `preview` TEXT NOT NULL, `image` BLOB, `timestamp` INTEGER NOT NULL )'],
        ['CREATE TABLE `studyCourse` ( `id` INTEGER PRIMARY KEY AUTOINCREMENT,`name` INTEGER, `chat_id` STRING)'],
]

def database_setup(db_file='hsfl_lnn.db'):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        create_tables()
    except Error as e:
        print(e)
    finally:
        conn.close()

def create_tables():
    """ Setup Tables"""
    try:
        conn = sqlite3.connect(db_file)
        
        for sql_command in sql_setup:
            conn.execute(str(sql_command)[2:-2])

    except Error as e:
        print(e)
    finally:
        conn.close()

if __name__ == '__main__':
    database_setup()