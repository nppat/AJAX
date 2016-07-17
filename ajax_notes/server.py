from flask import Flask, request, redirect, render_template, session, jsonify
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "Monster"
mysql =  MySQLConnector(app,"notes") # connect to the DB

# root route
@app.route('/')
def index():
	query = "SELECT * FROM notes ORDER BY created_at DESC"
	notes = mysql.fetch(query)
	return render_template("index.html", notes=notes)

# index_json route
@app.route('/index_json')
def index_json():
	query = "SELECT * FROM notes"
	notes = mysql.fetch(query)
	return jsonify(notes)

# index_html route
@app.route('/index_html')
def index_html():
	query = "SELECT * FROM notes"
	notes = mysql.fetch(query)
	return render_template('/partials/_notes.html', notes=notes)

# Create route
@app.route('/notes/create', methods=['POST'])
def create():
	title = request.form['title']
	description = request.form.get('add_description')
	print title
	print description
	query = "INSERT INTO notes(title, description, created_at, updated_at) VALUES('{0}','{1}', NOW(), NOW())".format(title, description)
	mysql.run_mysql_query(query)
	rquery = "SELECT * FROM notes ORDER BY created_at DESC"
	notes = mysql.fetch(rquery)

	return render_template('partials/_notes.html', notes=notes)

# Update route
@app.route('/notes/update/<id>', methods=['POST']) #update by id
def update(id):
	title = request.form['title_update']
	description = request.form.get("description_update")
	query = "UPDATE notes SET title = '{0}', description = '{1}' WHERE id = '{2}'".format(title,description,id)
	mysql.run_mysql_query(query)
	return redirect('/')

# Delete route
@app.route('/notes/delete/<id>', methods=['POST']) # delete note by id
def delete(id):
	query = "DELETE FROM notes WHERE id = '{0}'".format(id)
	mysql.run_mysql_query(query)
	print query
	return redirect('/')

app.run(debug=True)