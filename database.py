import psycopg2

con = psycopg2.connect(
        host = 'localhost',
        database = 'karunya',
        user = 'jerobinjacob',
        password = '8072749895',
        port = '5432')

cur = con.cursor()

cur.execute(
    "INSERT INTO students (name, age, course, professor_id, favorite_professors) VALUES (%s, %s, %s, %s, %s)",
    ('Nitin', 22, 'MBBS', 2, 'Ancy'))
con.commit()

cur.execute("SELECT * FROM students")
rows = cur.fetchall()
print (rows)

cur.close()
con.close()
