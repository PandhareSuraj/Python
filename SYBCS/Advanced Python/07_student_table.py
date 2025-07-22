'''Q.2 Write a program to create a student table with attributes, roll_no and name. Insert the records in table and display it.
update the records with roll_no = 10 from above table. 	'''
import psycopg2
conn = psycopg2.connect(database = "mydata",
                        user = "postgres",
                        port = 5432,
                        password = "12345678",
                        host = "localhost")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        roll_no INTEGER PRIMARY KEY,
        name varchar
    );
''')

cursor.execute("""insert into students(roll_no,name) values(1,'om'),(2,'rahul'),(10,'raj');""")
cursor.execute("""update students set name = 's' where roll_no = 10;""")
cursor.execute("select * from students;")
cursor.close()
conn.close()
