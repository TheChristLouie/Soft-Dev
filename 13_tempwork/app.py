# Christopher Louie
# SoftDev
# Sep 2024

import random
from flask import Flask, render_template
app = Flask(__name__)        

@app.route("/")
def readfile():
    occupations = {}
    with open('data/occupations.csv') as text:
        reader = text.read()
        reader = reader.split('\n')
        for row in range(len(reader)-2):
            if '"' in reader[row+1]:
                reader[row+1] = reader[row+1].split('",')
                reader[row+1][0] = reader[row+1][0]
            else:
                reader[row+1] = reader[row+1].split(',')
            occupations[reader[row+1][0]]=float(reader[row+1][1])
    return occupations

@app.route("/")
def generateRandom(occupations):
    generated = random.random()*99.8
    for key in occupations.keys():
        generated-=occupations[key]
        if (generated<0):
            return(str(key)+', ' +str(occupations[key]))
    return("error")

@app.route("/wdywtbwygp")
def page():         
    return render_template( 'tablified.html', title = "Job Helper", occupation = generateRandom(readfile()), Header = "Table", collection = readfile())

if __name__ == "__main__":
    app.debug = True
    app.run()