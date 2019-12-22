from create_database import example_db

con = example_db()

result = con.execute("SELECT * FROM users")
print(result.fetchall())
print(result.fetchall())

print(100 * "-") # Разделитель

for row in con.execute("SELECT * FROM users WHERE nickname = ?", ("MegaVasya",)):
    print(row)

con.close()
