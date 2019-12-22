from create_database import example_db

con = example_db()

sql = "DELETE FROM users WHERE nickname = 'Fedor'"

con.execute(sql)
con.commit()
con.close()
