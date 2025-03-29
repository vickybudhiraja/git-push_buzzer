from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>This is the middleware service for my Git Push Buzzer Pico-W project.</h1>"

@app.route('/fetchpush')
def fetch_push():
    response = requests.get('https://github.com/vickybudhiraja/pico_git-push-buzzer', stream=True)

    if response.status_code == 200:
        for chunk in response.iter_content(chunk_size=None):
            if chunk:
                print(chunk)
    else:
        print(f"Error: {response.status_code}")

if __name__ == '__main__':
    app.run(debug=True)
