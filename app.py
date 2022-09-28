from flask import Flask
app = Flask(__name__)
from app_blueprint import app_blueprint

app = Flask(__name__)
app.register_blueprint(app_blueprint)

