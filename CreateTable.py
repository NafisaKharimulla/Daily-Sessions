import pyodbc

# connect to AWS RDS
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=ecommerce-sql.c3i6myqiiehv.ap-south-1.rds.amazonaws.com;"
    "DATABASE=ecommerce;"
    "UID=admin;"
    "PWD=nafisashaik"
)

cursor = conn.cursor()

# CREATE TABLE
cursor.execute("CREATE TABLE students (id INT, name VARCHAR(50), course VARCHAR(50))")

# INSERT DATA
cursor.execute("INSERT INTO students VALUES (1,'Ram','Python')")
cursor.execute("INSERT INTO students VALUES (2,'Sam','AWS')")

# READ DATA
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("Students Table Data:")
for row in rows:
    print(row)

# UPDATE DATA
cursor.execute("UPDATE students SET course='Data Science' WHERE id=2")

# DELETE DATA
cursor.execute("DELETE FROM students WHERE id=1")

# save changes
conn.commit()

print("CRUD operations completed")

conn.close()
