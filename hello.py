import os

from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def index():
    # return "Index page"
    return url_for('show_user_profile', username='Hector')

@app.route('/user/<username>')
def show_user_profile(username):
    # show user profile
    return "User: " + username

@app.route('/hello')
def hello_world():
    return 'Hello World!'
    
if __name__ == '__main__':
    host=os.getenv('IP', '0.0.0.0')
    port=int(os.getenv('PORT', 5000))
    app.debug=True
    app.run(host=host, port=port)
    
