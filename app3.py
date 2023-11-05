from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the home page'

@app.route('/greet/<name>')
def greet(name):
    greeting = f'Hello, {name}!'
    return render_template('dynamic.html', greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)
