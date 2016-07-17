from flask import Flask, request, render_template
import requests # new import, had to install with pip
app = Flask(__name__)

# root route
@app.route('/')
def index():
	return render_template('index.html')

# Get some videos route
@app.route('/search', methods=['POST'])
def search():
	artist = request.form['user_input'].replace(' ', '')
	url = "https://itunes.apple.com/search?term=" + artist + "&entity=musicVideo"
	response = requests.get(url).content
	return response

app.run(debug=True) # run the app