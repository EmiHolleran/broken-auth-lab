from flask import Flask, render_template, request, redirect, session
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
app.secret_key = 'vulnerable-secret-key'
limiter = Limiter(app, key_func=get_remote_address)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/module1')
def module1():
    return render_template('module1.html')

@app.route('/module2')
def module2():
    return render_template('module2.html')

@app.route('/module3')
def module3():
    return render_template('module3.html')

@app.route('/module4')
def module4():
    return render_template('module4.html')

@app.route('/module5')
def module5():
    return render_template('module5.html')

if __name__ == '__main__':
    app.run(debug=True)
