import psycopg2

def get_connection():
    return psycopg2.connect(
        host='localhost',
        database='karunya',
        user='jerobinjacob',
        password='8072749895',
        port='5432'
    )


