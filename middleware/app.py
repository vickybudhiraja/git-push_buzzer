from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>This is the middleware service for my Git Push Buzzer Pico-W project.</h1>"

@app.route('/fetchpush')
def fetch_push():
    return ""

if __name__ == '__main__':
    app.run(debug=True)
