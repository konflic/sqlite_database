import sqlite3

con3 = sqlite3.connect(":memory:")
con3.close()

def example_db():
    sql = """
        CREATE TABLE
        IF NOT EXISTS users
        (
            id INTEGER PRIMARY KEY,
            nickname TEXT,
            email TEXT,
            reg_date DATETIME
        );
    """
    con = sqlite3.connect("example.db")
    con.execute(sql)
    return con

def simple_db():
    con = sqlite3.connect("simple.sqlite")
    with open("sql/create_simple_table.sql", "r") as script:
        con.execute(script.read())
    con.close()
