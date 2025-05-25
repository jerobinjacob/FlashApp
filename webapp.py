from flask import Flask
from routes import main

app = Flask("JerobinApp")

def sep_app():
    app.register_blueprint(main)
    return app