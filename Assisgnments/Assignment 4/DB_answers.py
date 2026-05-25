import sqlite3

conn=sqlite3.connect("college.db")



conn.execute("""
CREATE TABLE IF NOT EXISTS STUDENT(
ID INT,
NAME TEXT
)
""")

conn.execute("""
CREATE TABLE IF NOT EXISTS EMPLOYEE(
ID INT,
NAME TEXT
)
""")

conn.execute("""
CREATE TABLE IF NOT EXISTS COURSE(
ID INT,
COURSE_NAME TEXT
)
""")

print("Tables created")



conn.execute("INSERT INTO STUDENT VALUES(1,'Nikhil')")
conn.execute("INSERT INTO STUDENT VALUES(2,'Rahul')")

conn.execute("INSERT INTO EMPLOYEE VALUES(101,'Vikas')")
conn.execute("INSERT INTO COURSE VALUES(1,'Python')")




cursor=conn.execute("SELECT * FROM STUDENT")

print("\nStudent Table")

for row in cursor:
    print(row)




conn.execute("""
UPDATE STUDENT
SET NAME='Tanish Pinjani'
WHERE ID=1
""")



conn.execute("""
DELETE FROM STUDENT
WHERE ID=2
""")


conn.commit()

print("\nDatabase operations completed")

conn.close()