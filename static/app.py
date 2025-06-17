from flask import Flask, render_template, request, redirect, session, flash
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
app.secret_key = 'vulnerable-secret-key'
limiter = Limiter(app, key_func=get_remote_address)

users = {'admin': 'password123'}
reset_tokens = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/module1', methods=['GET', 'POST'])
def module1():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['user'] = username
            flash('Login successful!', 'success')
        else:
            flash('Invalid credentials.', 'error')
    return render_template('module1.html')

@app.route('/module2', methods=['GET', 'POST'])
def module2():
    if request.method == 'POST':
        username = request.form['username']
        token = 'reset123'  # weak predictable token
        reset_tokens[username] = token
        flash(f'Token generated: {token}', 'info')
    return render_template('module2.html')

@app.route('/module3', methods=['GET', 'POST'])
@limiter.limit("5 per minute")
def module3():
    if request.method == 'POST':
        flash('Request received.', 'info')
    return render_template('module3.html')

@app.route('/module4')
def module4():
    return render_template('module4.html')

@app.route('/module5')
def module5():
    return render_template('module5.html')

if __name__ == '__main__':
    app.run(debug=True)
