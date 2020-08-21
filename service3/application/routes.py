from flask import Response, request
from application import app
import random

@app.route('/fortune', methods=['GET'])
def fortune():

    number = random.randint(1, 2)
    if number == 1:
        goodfortune = ["an acquaintance of the past will positively affect you", "a lifetime friend shall soon be made", "a golden egg of opportunity will fall into your lap", "an important person will step into your life", "you will meet your soul-mate", "you will receive good news"]
        randgoodfortune = random.choice(goodfortune)
        return Response(randgoodfortune, mimetype='text/plain')
    elif number == 2:
        badfortune = ["you will face great uncertainty", "you will receive bad news", "you will face some hard times", "you will have a bad argument with a friend", "an acquaintance of the past will negatively affect you"]
        randbadfortune =  random.choice(badfortune)
        return Response(randbadfortune, mimetype='text/plain')