from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "llo2ay"
password = "123"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina","Sobhe"]


@app.route('/', methods = ['POST', 'GET'])  # '/' for the default page
def login():
	if request.method == 'POST':
	 if username == request.form['username'] and password == request.form['password']:
	    return render_template('home.html')
	redirect(url_for('home'))
  
@app.route('/')
def home():
	 return render_template("home.html", friends = facebook_friends)


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)