from flask import Response, request
from application import app
import requests

@app.route('/outcome', methods=['GET'])
def outcome():
    timeframe = request.data1.decode("utf-8")
    fortune = request.data2.decode("utf-8")

    response = timeframe + ", " + fortune

    return Response(response, mimetype='text/plain')