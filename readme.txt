This is my readme.txt file

Crear ambiente virtual en AWS Cloud o en Cloud9

//En ambiente limpio
sudo yum install python3
sudo yum install flask

mkdir flask_init --directorio donde se va a crear el ambiente virtual
cd flask_init
python -V  //ver versión de Python
virtualenv -p python3 venv  //crear ambiente virtual
source venv/bin/activate //activar ambiente
deactivate //salir

pip //para instalar herramientas de python/ side packages

pip install flask //instalar flask


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
    

Install  MySQL (ya viene en Cloud9)
sudo yum install -y mysql-server (linux)
sudo apt install -y mysql-server (ubuntu)

Iniciar MySQL service:
sudo service mariadb start && sudo service mariadb status
Firmarse en MySql:
sudo mysql -uroot -p

pip install -r requirements.txt