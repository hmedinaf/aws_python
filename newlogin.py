import os
import pymysql

from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error=None
    if request.method=="POST":
        if valid_login(request.form['username'], request.form['password']):
            return redirect(url_for('welcome', username=request.form.get('username')))
        else:
            error = "Incorrect username/password"

    return render_template('login.html', error=error)

def valid_login(username, password):
    #mysql
    MYSQL_DATABASE_HOST = os.getenv('IP', '0.0.0.0')
    MYSQL_DATABASE_USER = 'hector'
    MYSQL_DATABASE_PASSWORD = 'stargat3'
    MYSQL_DATABASE_DB = 'my_flask_app'
    conn = pymysql.connect(
        host=MYSQL_DATABASE_HOST,
        user=MYSQL_DATABASE_USER,
        passwd=MYSQL_DATABASE_PASSWORD,
        db=MYSQL_DATABASE_DB
        )
    cursor=conn.cursor()
    cursor.execute("select * from user where username='%s' and password='%s'" % (username, password))
    data=cursor.fetchone()
    if data:
        return True
    else:
        return False

@app.route('/welcome/<username>')
def welcome(username):
    return render_template('welcome.html', username=username)

if __name__ == '__main__':
    host=os.getenv('IP', '0.0.0.0')
    port=int(os.getenv('PORT', 5000))
    app.debug=True
    app.run(host=host, port=port)
    
