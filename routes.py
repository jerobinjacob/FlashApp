from flask import Blueprint, render_template, abort, request, make_response

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
    # Request
    custom_header = request.headers.get('Client-ID', 'zephony')
    print(f'Custom Header: {custom_header}')
    if username in data:
        html = render_template("users.html", info=data[username])
        #response
        response = make_response(html)
        response.headers['Developer'] = 'Jerobin'
        response.headers['Client-ID'] = custom_header
        return response
    else:
        abort(404)
