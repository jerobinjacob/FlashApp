from flask import Flask, request, redirect, render_template
from db import get_connection

app = Flask(__name__)

@app.route('/')
def home():
    con = get_connection()
    cur = con.cursor()
    cur.execute('select s.student_id, s.name as student_name, s.age as student_age, s.course, p1.name as professor_name, p2.name as favourite_professors from students s join professors p1 on s.professor_id = p1.professor_id join professors p2 on s.favourite_professors = p2.professor_id order by s.student_id;')
    students = cur.fetchall()
    cur.close()
    con.close()

    return render_template('home.html', students=students)

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

@app.route('/delete', methods = ['GET', 'POST'])
def delete():
    if request.method == 'POST':
        student_id = request.form['student_id']
        con = get_connection()
        cur = con.cursor()
        cur.execute('delete from project_details where student_id = %s', (student_id, ))
        cur.execute('delete from students where student_id = %s', (student_id, ))
        con.commit()
        cur.close()
        con.close()
        return redirect('/')
    return render_template('delete.html')

@app.route('/update/<int:student_id>', methods = ['GET', 'POST'])
def update(student_id):
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        course = request.form.get('course')
        professor_id = request.form.get('professor_id')
        favourite_professors = request.form.get('favourite_professors')        
        con = get_connection()
        cur = con.cursor()
        cur.execute('update students set name = %s, age = %s, course = %s, professor_id = %s, favourite_professors = %s where student_id = %s', (name, age, course, professor_id, favourite_professors, student_id))
        con.commit()
        cur.close()
        con.close()
        return redirect('/')
    else:
        con = get_connection()
        cur = con.cursor()
        cur.execute('select * from students where student_id = %s', (student_id,))
        student = cur.fetchone()
        cur.close()
        con.close()
        return render_template('update.html', s=student)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5001, debug = True)
