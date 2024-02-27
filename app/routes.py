
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

@app.route('/speel')
def speel():
    testspelers =[   
        {
            'naam':'jantje',
            'score':0
        },
        
        {
            'naam':'pietje',
            'score':0
        }
    ]
    return render_template('speel.html', spelers = testspelers)

@app.route('/winnaar')
def winnaar():
    return render_template('winnaar.html')