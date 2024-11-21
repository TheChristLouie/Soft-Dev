#Double Ls - Kevin Lin, Christopher Louie
#SoftDev
#K23 - NASA API
#2024-11-20
#time spent: 0.75
from flask import Flask, render_template
#import requests
import urllib.request
import json

app = Flask(__name__)
with open('key_nasa.txt',"r") as key:
    api = key.read()

@app.route("/")
def nasa():
    #request = requests.get(api).json()
    #print(request['explanation'])
    with urllib.request.urlopen(api) as response:
        html = response.read()
        data = json.loads(html)
        #print(data['explanation'])
    return render_template("main.html",text=data['explanation'],img1 = data['url'], img2 = data['hdurl'])
    
if __name__ == "__main__":
    app.debug = True
    app.run()