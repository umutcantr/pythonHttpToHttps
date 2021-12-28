

from flask import Flask, request  # import flask and incoming request.
import requests  # import outgoing request

url = "YOUR_URL"

app = Flask(__name__)


@app.get("/")  #http get
def get_countries():
    return "Hello, you requested."


@app.post("/")  #http post
def https_post_to_firebase():
    if request.is_json:
       data = request.get_json()   # Get requested http post data.
       
       print(data)
       
       response = requests.post(url, json=data)  # Post requested data to https server.

       if response.status_code == 404:
          print('Not Found.')
 
    return  data, 201    # return http 201(created) response.



