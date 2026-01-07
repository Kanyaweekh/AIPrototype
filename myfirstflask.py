from flask import Flask,  flash, redirect, request, render_template, make_response, url_for
import json
import sys 
#import pandas as pd

app = Flask(__name__)

#web service
##api post
@app.route('/') #บอกว่าเรียกใช้ web ไหน
def helloworld():
    return "Hello, World!"

@app.route('/name') 
def name():
    return "Kanyawee Khamudom"

@app.route('/request_POSTGET',methods=['POST','GET']) 
def web_service_API_GET():
    if request.method == 'GET':
        msg = request.args.get('msg')
        name = request.args.get('name')
        print(f'the input message from GET is {msg} from {name}.')
        return f'GET {msg} from {name} receive!'
    elif request.method == 'POST':
            payload = request.data.decode("utf-8")
            inmessage = json.loads(payload)

            print(inmessage)

            json_data = json.dumps({'y': 'POST received!'})
            return json_data

    else:
         return "Only GET and POST methods are supported."
if __name__ == "__main__":   # run code 
    app.run(host='localhost',debug=True,port=5001)#host='0.0.0.0' = run on internet ,port=5001