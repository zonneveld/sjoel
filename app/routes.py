
from flask import render_template, Response,request

from app import app

from app.machine import Machine

import time


@app.route('/')
@app.route('/index')
@app.route('/start')
def index():
    return render_template('start.html')

@app.route('/aanmelden')
def aanmelden():
    return render_template('aanmelden.html')

@app.route('/speel',methods = ['GET'])
def speel():
    # print(request.args.get("speler1"))
    # print(request.args.)
    huidgespelers = []
    id = 0    
    for data in request.args:

        if request.args.get(data) != "":
            huidgespelers.append(
                {
                    'naam':request.args.get(data),
                    'id':id
                }
            )
            id += 1
    # testspelers =[   
    #     {
    #         'naam':'jantje',
    #         'score':0
    #     },
        
    #     {
    #         'naam':'pietje',
    #         'score':0
    #     }
    # ]
    return render_template('speel.html', spelers = huidgespelers)

@app.route('/winnaar')
def winnaar():
    return render_template('winnaar.html')

@app.route('/listen')
def stream_data():
    def generator():
        machine = Machine()
        machine.start()
        while True:
            while not machine.check():
                pass
            r_data = machine.get_payload()
            machine.flush()
            data = f'data: {r_data}\n\n'
            print(f"yielding {r_data}")
            yield data
            
    return Response(generator(),mimetype='text/event-stream')