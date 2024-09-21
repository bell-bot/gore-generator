#!/usr/bin/env python3

import os.path
import sys
from flask_cors import CORS


from flask import Flask, make_response, request, send_file

from constants import IMAGE_PATH
from generate import generate
app = Flask(__name__)
CORS(app)

@app.get('/generate')
def generate_gore():
    print("Working dir: " + os.getcwd())
    radius = request.args.get('radius', type=float)
    n_gores = request.args.get('n_gores', type=int)
    precision = request.args.get('precision', type=float)
    
    if (radius == None or n_gores == None or precision == None):
        return make_response("Missing attributes: all attributes must be given", 400)
    
    generate(radius, n_gores, precision)
    
    response = make_response(send_file(IMAGE_PATH))
    response.headers.add('Content-Type', 'image/png')

    return response
