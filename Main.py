
from GetPath import ReturnPath
from flask import Flask,Response, request, url_for,jsonify
from flask_cors import CORS, cross_origin
import json
from flask import request
import os
import speech_recognition as sr
import logging
from StringProcess import ConnectProcess

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['DEBUG'] = True

logging.getLogger('flask_cors').level = logging.DEBUG

@app.route('/', methods=['GET'])
def home():
    return "<h1>Flask API</h1>"

@app.route('/api/', methods= ["POST"])
@cross_origin()
def text():
    request_data = request.get_json()
    print(request_data)
    startVertex, endVertext, error_code = ConnectProcess(request_data['text'], request_data['language'])
    if error_code!=0:
        return jsonify( startVertex)
    respons = ReturnPath(int(startVertex), int(endVertext), language=request_data['language'])
    return jsonify(respons)

@app.route('/api/auth/', methods = ['POST'])
@cross_origin()
def auth():
    request_data = request.get_json()
    print(request_data)
    return jsonify({'auth': 'true'})

@app.route('/api/blob/request/', methods = ['POST']) 
def convertBlob2Text():
    files = request.files['file']
    files.save(os.path.join('C:/Users/.../Desktop/.../blob.mp3'))
    r = sr.Recognizer()
    with sr.AudioFile('blob.mp3') as source:
        audio = r.record(source)
        text = r.recognize_google(audio)
    return text

if __name__ == "__main__":
    app.run()