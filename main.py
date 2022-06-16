import requests
from flask import Flask, render_template, request

app = Flask(__name__)
api_key = '423997f7-8635-4a53-9387-67ff2fd9fa7f'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def image():
    if request.method == "POST":
        response = requests.get("https://randomfox.ca/floof")
        cat = response.json()
        content = cat['image']
        return render_template('index.html', image=content, data=cat)
    else:
        return index()


if __name__ == "__main__":
    app.run(debug=True)
