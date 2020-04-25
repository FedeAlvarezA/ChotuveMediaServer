import os
from flask import Flask, escape, request, jsonify
from marshmallow import ValidationError
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
	return '<h1>Hello World!!</h1>'


app.run()
