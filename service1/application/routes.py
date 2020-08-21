from application import app
from flask import render_template, request, jsonify, Response
import requests

@app.route('/')
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', title='Home')

@app.route('/fortuneteller', methods=['GET', 'POST'])
def fortuneteller():
    timeframe = requests.get('http://service2:5001/timeframe')
    fortune = requests.get('http://service3:5002/fortune')
    
    outcome = requests.post("http://service4:5003/outcome", data1=timeframe.text, data2=fortune.text)
    
    return render_template('fortune.html', title='Fortune', outcome=outcome)