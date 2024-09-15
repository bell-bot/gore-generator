#!/usr/bin/env python3

import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from flask import Flask, make_response, request, send_file

from server.constants import IMAGE_PATH
from server.generate import generate
app = Flask(__name__)

@app.get('/generate')
def generate_gore():
    radius = request.args.get('radius', type=float)
    n_gores = request.args.get('n_gores', type=int)
    precision = request.args.get('precision', type=float)
    
    if (radius == None or n_gores == None or precision == None):
        return make_response("Missing attributes: all attributes must be given", 400)
    
    generate(radius, n_gores, precision)
    
    return send_file(IMAGE_PATH)