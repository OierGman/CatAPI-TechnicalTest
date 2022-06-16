import requests
from flask import Flask, render_template, request
import random

app = Flask(__name__)
api_key = '423997f7-8635-4a53-9387-67ff2fd9fa7f'


@app.route('/')
def index():
    if request.method == "GET":
        response = requests.get("https://api.thecatapi.com/v1/images/search", headers={'x-api-key': api_key})
        cat = response.json()
        content = cat[0]['url']
        return render_template('index.html', image=content)


@app.route('/types', methods=['GET'])
def service():
    response = requests.get("https://api.thecatapi.com/v1/breeds?limit=30", headers={'x-api-key': api_key})
    breeds = response.json()
    if request.method == "GET":
        random_number = random.randint(0, 29)
        breed = [i['name'] for i in breeds]
        indexOf = [breeds[j] for j in range(30)]
        info = indexOf[0]
        name = breed[random_number]
        nReq = requests.get("https://api.thecatapi.com/v1/images/search?breed_ids="+indexOf[random_number]['id'],
                            headers={'x-api-key': api_key})
        img = nReq.json()[0]['url']
        desc = indexOf[random_number]['description']
        orig = indexOf[random_number]['origin']
        temp = indexOf[random_number]['temperament']
        return render_template('types.html', info=info, image=img, name=name, desc=desc, orig=orig, temp=temp)


@app.route('/bad-day', methods=['POST', 'GET'])
def gif():
    if request.method == "POST" or "GET":
        response = requests.get("https://api.thecatapi.com/v1/images/search?mime_types=gif", headers={'x-api-key': api_key})
        cat = response.json()
        content = cat[0]['url']
        return render_template('bad-day.html', image=content)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
