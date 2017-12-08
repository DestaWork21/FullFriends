from flask import Flask, render_template, request, redirect
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'friendsdydb')

@app.route("/")
def index():
    
	return render_template("index.html", friendsdy=mysql.query_db("SELECT * FROM friendsdy"))

@app.route("/create_friends", methods=["POST"])
def create():
    query = "INSERT INTO friendsdy (name, age, friendSince, year, created_at, updated_at) VALUES(:Name, :Age, :FriendSince, :Year, NOW(), NOW())"
    data = {
	    "Name": request.form["name"],
		"Age": request.form["age"],
        "FriendSince": request.form["friendSince"],
		"Year": request.form["year"] 
	}

    mysql.query_db(query, data)
    return redirect("/")

@app.route("/edit/<id>")
def edit(id):
	query = "SELECT * FROM friendsdy WHERE id={}".format(id)
	book = mysql.query_db(query)
	return render_template("edit.html", friendsdy=friend[0])

@app.route("/update_friend/<id>", methods=["POST"])
def update(id):
	query = "UPDATE friendsdy SET Name=:Name, Age=:Age, Friend Since=:Friend Since, Year=:Year, updated_at=NOW() WHERE id=:id;"
	data = {
		"Name": request.form["name"],
		"Age": request.form["age"],
        "Friends Since": request.form["friendSince"],
		"Year": request.form["year"],
		"id": id
	}
	mysql.query_db(query, data)
	return redirect("/")

@app.route("/delete/<id>")
def delete(id):
	query = "DELETE FROM friendsdy WHERE id={}".format(id)
	mysql.query_db(query)
	return redirect("/")

app.run(debug=True)