from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']

    return f'Welcome, {username}!'

if __name__ == '__main__':
    app.run(debug=True)
