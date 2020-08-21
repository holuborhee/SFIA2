from flask import Response, request
from application import app
import requests

@app.route('/outcome', methods=['GET', 'POST'])
def outcome():
    time = request.data.decode("utf-8")

    if time == "Today" or time == "Tomorrow" or time == "In a few days":
        percentage = "15%"
    elif time  == "On this coming Friday" or time == "On this coming Tuesday" or time == "Next week":
        percentage = "20%"
    elif time == "This month":
        percentage = "25%"
    elif time == "This year" or time == "Next year" or time == "In a few years":
        percentage = "75%"
    elif time == "In a few months":
        percentage = "40%"
    elif time == "Next spring" or time == "Next summer" or time == "Next winter":
        percentage = "55%"
    else:
        percentage = "Unable to calculate"

    return Response(percentage, mimetype='text/plain')