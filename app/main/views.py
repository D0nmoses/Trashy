from .. import main
from ..request import getLocation
from flask import render_template,request,redirect,url_for,abort,flash

@main.route
def map():
    location = getLocation()
    latitude = location[1]
    longitude =location[2]

    return render_template('map.html', latitude=latitude, longitude = longitude)

