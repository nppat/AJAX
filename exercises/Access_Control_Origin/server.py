from flask import Flask, render_template, request, redirect
import requests
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movie', methods=['POST'])
def get_movie():
    artist = request.form['user_input']
    url = "https://itunes.apple.com/search?term=" + artist + "&entity=musicVideo"
    # notice this is 'requests' not 'request'
    # we are using the request modules, 'get' function to send a request from our controller
    # then we use ".content" to get the content we are looking for
    response = requests.get(url).content
    # we then send the response back to our client which sent the initial post request
    return response

app.run(debug=True)