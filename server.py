#!/usr/bin/env python3

from flask import Flask, render_template
import json
from random import randint

with open('totalAsiaGeolocatedSorted.json') as json_file:
    data = json.load(json_file)


app = Flask(__name__)
@app.route('/')
def index():
        postId = randint(1,len(data))
        caller = 'Post '+str(postId)
        print("length data: ",len(data))
        print("printing at post: ",postId)
        title = data[caller]['Title']
        url = data[caller]['URL']
        lat = data[caller]['lat']
        lon = data[caller]['lon']
        stat = 0
        return render_template('index.html', url=url, title=title, lat=lat, lon=lon)

if __name__ == '__main__':
    app.run(port="80",debug=True, host='0.0.0.0')
