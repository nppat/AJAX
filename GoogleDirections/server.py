from flask import Flask, request, render_template
import requests
import urllib # found this is the Docs
app = Flask(__name__)

# root route
@app.route('/')
def index():
	return render_template('index.html')

# get directions route
@app.route('/get_directions', methods=['POST'])
def get_directions():
	origin = request.form['origin'] # get origin info from form
	destination = request.form ['destination'] # get destination info from form
	data = {'origin':origin, 'destination':destination} # package up into a dictionary
	# put data into urlencode to pass to a query string to Google w/ our API key
	url = "https://maps.googleapis.com/maps/api/directions/json?"+urllib.urlencode(data)+"&key=AIzaSyCnGpbunYYumP3ATcHHTG1gSZfjQiN0fDs"
	response = requests.get(url).content # requests.get to send in the request
	return response # return response to client that sent initial post request

app.run(debug=True) # run the server