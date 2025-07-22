'''Q.2 Write a program to create a employee table with attributes, no and name. Insert the 5 records in table and display it.
update the records with no = 103 from above table.
'''
import psycopg2
conn = psycopg2.connect(database = 'mydata',
                        user = 'postgres',
                        host = 'localhost',
                        port = 5432,
                        password = 'omsai@2024#')
cur = conn.cursor()
cur.execute("""create table employee(no int,name varchar);""")
print("Table created successful")
cur.execute("""insert into employee values(1,'om'),(2,'ratan'),(3,'ram'),(4,'jay'),(103,'raj');""")
print("5 values is inserted")
cur.execute("""update employee set name = 's' where no = 103;""")
print("Update")
#cur.commit()
cur.close()
conn.close()