import sqlite3
import datetime
from create_database import example_db, simple_db

"""
Python -> SQLite
----------------
None   -> NULL
int    -> INTEGER
float  -> REAL
str    -> TEXT
bytes  -> BLOB
"""

EXAMPLE = "example.db"
SIMPLE = "simple.sqlite"

example_con = example_db()
simple_db()

def insert_row(db, sql, params):
    con = sqlite3.connect(db)
    con.execute(sql, params)
    con.commit()
    con.close()

# Единичное добавление и уникальность ряда
# insert_row(EXAMPLE, "INSERT INTO users (nickname) VALUES (?)", ("DOMINATOR666",))
# insert_row(SIMPLE, "INSERT INTO simple (nickname) VALUES (?)", ("NAGIBATOR888",))

users = [
    ("MegaVasya", "super@mail.ru", datetime.datetime.now()),
    ("Alisa", "alisa@ya.ru", datetime.datetime.now()),
    ("Fedor", "nikita@yahoo.ru", datetime.datetime.now()),
    ("DEADMOROZ", "iks_@hotmail.ru", datetime.datetime.now()),
    ("___ZIP____", "z@gmail.com", datetime.datetime.now()),
    ("MegaVasya", "super@mail.ru", datetime.datetime.now()),
]

# Множественное добавление
sql = "INSERT INTO users (nickname, email, reg_date) VALUES (?, ?, ?)"
example_con.executemany(sql, users)
example_con.commit()
example_con.close()
