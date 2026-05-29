# import sqlite3
# conn = sqlite3.connect('example.db')
# sql ="""CREATE TABLE IF NOT EXISTS employees (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     age INTEGER,
#     mob varchar(10),
#     email varchar(255)
# )"""
# conn.execute(sql)
# print("Table created successfully")
# conn.close()


# import sqlite3
# conn = sqlite3.connect('example.db')
# sql ='''
#         insert into employees (name, age, mob, email) values ('pINJANI', 22, '1234567890', 'abhaykumaryadav@example.com')
# '''
# conn.execute(sql)
# conn.commit()
# conn.close()


import sqlite3
conn = sqlite3.connect('mydatabase.db')
sql ='''
        select * from employees
'''
res = conn.execute(sql)
for row in res:
    print(row)
conn.commit()
conn.close()