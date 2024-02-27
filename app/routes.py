
from flask import render_template

from app import app

@app.route('/')
@app.route('/index')
@app.route('/start')
def index():
    return render_template('start.html')

@app.route('/aanmelden')
def aanmelden():
    return render_template('aanmelden.html')