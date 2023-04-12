import os
import sqlite3
import hashlib
import time
from flask import Flask, request, render_template,url_for


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/prebuilt')
def prebuilt():
    return render_template('prebuilt.html')

@app.route('/3dprint')
def print():
    return render_template('3dprinting.html')


if __name__ == '__main__':
    app.run(debug=True)