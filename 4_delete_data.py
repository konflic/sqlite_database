from create_database import example_db

con = example_db()

sql = "DELETE FROM users WHERE nickname = ?"

con.execute(sql, ('Fedor',))
con.commit()
con.close()


def drop_table(table_name):
    con = example_db()
    con.execute("DROP table %s" % table_name)
    con.commit()
    con.close()

# drop_table("users")
