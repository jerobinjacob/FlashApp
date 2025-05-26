from flask import Blueprint, render_template, abort

main = Blueprint('main', __name__)

@main.route('/user/<username>')
def userspage(username):
    data = {
        'jerobin': {
            'name': 'Jerobin Jacob',
            'address': 'South Authoor, Thoothukudi',
            'phone': '+91 8072749895',
            'email': 'jerobinjacob@gmail.com',
            'age': 22,
            'gender' : 'Male',
        },
        'jeleena': {
            'name': 'Jeleena',
            'address': 'South Authoor, Thoothukudi',
            'phone': '+91 9344647676',
            'email': 'jeleena@gmail.com',
            'age': 17,
            'gender' : 'Female',
        }
    }
    if username in data:
        return render_template("users.html", info = data[username])
    else:
        abort(404)
