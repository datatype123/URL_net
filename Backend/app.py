import redis
from flask import Flask, request, jsonify
import json
import redis
import requests
import feature_extraction
app = Flask(__name__)
@app.route('/', methods = ['POST'])
def get_method():
    data = request.data
    url = json.loads(data).get("url")
    prediction = feature_extraction.main(url)
    data_response = {"prediction": prediction}
    return jsonify(data_response)  
if(__name__ == "__main__"):
    app.run(host = '127.0.0.1', port = 5000, debug = True)
