from flask import Flask, render_template
import requests
import re

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>This is the middleware service for my Git Push Buzzer Pico-W project.</h1>"

@app.route('/fetchpush')
def fetch_push():
    response = requests.get('https://github.com/vickybudhiraja/pico_git-push-buzzer', stream=True)

    if response.status_code == 200:
        search_str = "commit"
        match_found = False
        found_number = None

        for chunk in response.iter_content(chunk_size=1024):
            # if chunk:
            #     print(chunk)
            if chunk:
                decoded = chunk.decode("utf-8", errors="ignore")
                if search_str in decoded:
                    print(search_str)
                    match = re.search(rf"\D*(\d+){search_str}", decoded)
                    if match:
                        found_number = match.group(1)
                        print(found_number)
                        match_found = True
                        break

        if match_found and found_number:
            return found_number
    else:
        print(f"Error: {response.status_code}")

if __name__ == '__main__':
    app.run(debug=True, port=8080)
