from flask import Flask, url_for, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
import requests
from base64 import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self, username, password):
        self.username = username
        self.password = password


@app.route('/', methods=['GET'])
def index():
    if session.get('logged_in'):
        return render_template('home.html')
    else:
        return render_template('index.html', message="Hello!")


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            db.session.add(User(username=request.form['username'], password=request.form['password']))
            db.session.commit()
            return redirect(url_for('login'))
        except:
            return render_template('index.html', message="User Already Exists")
    else:
        return render_template('register.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        u = request.form['username']
        p = request.form['password']
        data = User.query.filter_by(username=u, password=p).first()
        if data is not None:
            session['logged_in'] = True
            u=b64encode(bytes(u.encode('utf-8'))).decode('ascii')
            print(f"TTTTHHHHHHIIIIIISSSS ======>> {u}")
            #requests.post("http://php_app/index.php",data=f"user={u}&status=Successful")
            requests.get(f"http://php_app_new/index.php?user={u}&status=Successful")
            return redirect(url_for('index'))
        u=b64encode(bytes(u.encode('utf-8'))).decode('ascii')
        print(f"TTTTHHHHHHIIIIIISSSS ======>> {u}")
        #requests.post("http://php_app/index.php",data=f"user={u}&status=Unsuccessful")
        requests.get(f"http://php_app_new/index.php?user={u}&status=Successful")
        return render_template('index.html', message="Incorrect Details")


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))

def init_db():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    app.secret_key = "ThisIsNotASecret:p"
    init_db()
    app.run(host='0.0.0.0')
