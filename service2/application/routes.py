from flask import Response, request
from application import app
import random

@app.route('/timeframe', methods=['GET'])
def timeframe():
    neartime = ["Today", "Tomorrow", "In a few days", "Next week", "On this coming Friday", "On this coming Tuesday", "This month"]
    fartime = ["This year", "Next year", "In a few years", "In a few months", "Next spring", "Next summer", "Next winter"]

    number = random.randint(1,2)
    if number == 1:
        randneartime = random.choice(neartime)
        return Response(randneartime, mimetype='text/plain')
    elif number == 2:
        randfartime = random.choice(fartime)
        return Response(randfartime, mimetype='text/plain')