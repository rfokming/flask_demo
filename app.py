from flask import Flask,session
from flask_session import Session

app = Flask(__name__)
from app_blueprint import app_blueprint


app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
app.register_blueprint(app_blueprint)

