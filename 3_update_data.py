from create_database import example_db

con = example_db()

sql = "UPDATE users SET nickname = 'NEW_NICKNAME' WHERE nickname = 'Alisa'"

con.execute(sql)
con.commit()
con.close()
