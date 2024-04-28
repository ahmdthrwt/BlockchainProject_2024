from flask import Flask, render_template, session, redirect, logging
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL


app = Flask(__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'crypto'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor' #  how we access the data from the database ,dictionary cursor

mysql = MySQL(app) # pass the app to the mysql object
@app.route('/') # route to the home page 

def index():
    """
    This function renders the home page of the application.
    """
    return "Hello World!"
if __name__ == '__main__':
    app.secret_key = 'secret123' # secret key for the session 
    app.run(debug=True)
