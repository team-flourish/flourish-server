from flask import Flask, render_template, request
from flask_cors import CORS
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)
