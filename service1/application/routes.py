from application import app, db
from flask import render_template, request, jsonify, Response
from application.models import ToldFortunes
import requests

@app.route('/')
@app.route('/home', methods=['GET'])
def home():
    fortunes = ToldFortunes.query.all()
    return render_template('home.html', title='Home', fortunes=fortunes)

@app.route('/fortuneteller', methods=['GET', 'POST'])
def fortuneteller():
    tf = requests.get('http://service2:5001/timeframe')
    fort = requests.get('http://service3:5002/fortune')
    
    percent = requests.post("http://service4:5003/outcome", data=tf.text)

    timeframe = tf.text
    fortune = fort.text
    percentage = percent.text

    fortuneData = ToldFortunes(
        timeframe = timeframe,
        fortune = fortune,
        percentage = percentage
    )
    db.session.add(fortuneData)
    db.session.commit()
    
    return render_template('fortune.html', title='Fortune', timeframe=timeframe, fortune=fortune, percentage=percentage)