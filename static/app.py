from flask import Flask, render_template, request, redirect, session, flash
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import time

app = Flask(__name__)
app.secret_key = 'vulnerable-secret-key'
limiter = Limiter(app, key_func=get_remote_address)

users = {'admin': 'password123'}
reset_tokens = {}
secure_mode = False

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/module6', methods=['GET', 'POST'])
def module6():
    if request.method == 'POST':
        username = request.form['username']
        start = time.time()
        if username in users:
            time.sleep(0.8)
        else:
            time.sleep(0.2)
        end = time.time()
        flash(f"Response time: {end - start:.2f}s", 'info')
    return render_template('module6.html')

@app.route('/module7', methods=['GET', 'POST'])
def module7():
    if request.method == 'POST':
        token = request.form['token']
        if token == 'valid123':
            flash('Token accepted. Replay attack succeeded.', 'danger')
        else:
            flash('Invalid token.', 'error')
    return render_template('module7.html')

@app.route('/module8')
def module8():
    attacks = [
        {'time': '12:01', 'action': 'Brute force login attempt'},
        {'time': '12:02', 'action': 'MFA bypass simulation'},
        {'time': '12:04', 'action': 'CAPTCHA flaw used'}
    ]
    return render_template('module8.html', attacks=attacks)

@app.route('/secure_toggle')
def secure_toggle():
    global secure_mode
    secure_mode = not secure_mode
    state = 'ON' if secure_mode else 'OFF'
    flash(f"Secure mode is now {state}", 'info')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
