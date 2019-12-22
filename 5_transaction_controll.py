from create_database import example_db

sql_1 = "INSERT INTO users (nickname, email) VALUES (?, ?)"
sql_2 = "UPDATE users SET nickname = ? WHERE email = ?"
sql_3 = "DELETE FROM users WHERE nickname = ?"

NICKNAME = 'SuperUser'
EMAIL = 'superemail@email.ru'
NEw_NICKNAME = 'UPDATED_NICKNAME'

con = example_db()

con.execute(sql_1, (NICKNAME, EMAIL))
con.execute(sql_2, (NEw_NICKNAME, EMAIL))
con.commit()
con.rollback()
con.execute(sql_3, (NEw_NICKNAME,))
con.rollback()
con.commit()
