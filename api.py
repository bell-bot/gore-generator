#!/usr/bin/env python3
from flask_cors import CORS


from flask import Flask, make_response, request, send_file

from constants import PDF_PATH, ZIP_PATH
from generate import generate
from util import zip_response
app = Flask(__name__)
CORS(app)

@app.get('/generate')
def generate_gore():
    print(request.args.get('n_gores'))
    radius = float(request.args.get('radius', type=str))
    n_gores = int(float(request.args.get('n_gores', type=str)))
    precision = request.args.get('precision', type=float)
    
    if (radius == None or n_gores == None or precision == None):
        return make_response("Missing attributes: all attributes must be given", 400)
    
    generate(radius, n_gores, precision)
    
    zip_response()

    response = send_file("../" + ZIP_PATH, 'zip')

    return response
