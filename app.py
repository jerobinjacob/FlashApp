from flask import Flask, render_template, request, redirect
from db import get_connection

app = Flask(__name__)

@app.route('/')
def home():
    con = get_connection()
    cur = con.cursor()
    cur.execute('select * from students')
    students = cur.fetchall()
    cur.close()
    con.close()
    return render_template('home.html', students = students)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        course = request.form['course']
        professor_id = request.form['professor_id']
        favourite_professors = request.form['favourite_professors']

        con = get_connection()
        cur = con.cursor()
        cur.execute(
            'insert into students (name, age, course, professor_id, favourite_professors) values (%s, %s, %s, %s, %s)', (name, age, course, professor_id, favourite_professors))

        con.commit()
        cur.close()
        con.close()
        return redirect('/')
    return render_template('add.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5001, debug = True)
