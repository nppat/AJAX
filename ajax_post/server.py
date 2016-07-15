from flask import Flask, request, render_template, session, flash, jsonify, redirect
from mysqlconnection import MySQLConnector # import connection to DB
app = Flask(__name__)
app.secret_key = "DivisionBell" # Pink Floyd reference
mysql = MySQLConnector(app,"notesdb") # connect to the DB

# root route
@app.route('/')
def index():
	query = "SELECT note FROM notes ORDER BY created_at DESC"
	notes = mysql.fetch(query) # get notes from DB
	return render_template('index.html', notes=notes) #render page w/ notes, if any.

# index_json route
@app.route('/index_json')
def index_json():
	query = "SELECT CONCAT(note,' - ', DATE_FORMAT(notes.created_at, '%M %D %Y %r')) as note FROM notes ORDER BY created_at DESC"
	notes = mysql.fetch(query)
	return jsonify(notes)

# index_html route
@app.route('/index')
def index_html():
	query = "SELECT CONCAT(note,' - ', DATE_FORMAT(notes.created_at, '%M %D %Y %r')) as note FROM notes ORDER BY created_at DESC"
	notes = mysql.fetch(query)
	return render_template('partials/_note_partial.html', notes=notes)

#CREATE note route and input validation
@app.route('/posts/create',methods=['POST'])
def create():
	#set session data from form
	session['note'] = request.form['get_note']
	# # check to see if session is empty, flash error if empty
	# if(len(session['note']) < 1):
	# 	flash("Note cannot be empty.", 'error')
	# 	return redirect('/index')
	# else:
	query = "INSERT INTO notes (note, created_at, updated_at) VALUES ('{0}', NOW(), NOW())".format(session['note'])
	print "in first query"
	mysql.run_mysql_query(query)
	# flash("Note posted!", 'success')
	rquery = "SELECT CONCAT(note,' - ', DATE_FORMAT(notes.created_at, '%M %D %Y %r')) as note FROM notes ORDER BY created_at DESC"
	print "in rquery"
	notes = mysql.fetch(rquery)
	print "redirect"
	return render_template('partials/_note_partial.html', notes=notes)

app.run(debug=True) # run the server