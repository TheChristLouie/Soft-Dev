#Death Row Coders: Kevin Lin, Raymond Lin, Christopher Louie
#SoftDev
#Sep 2024

import random
from flask import Flask, render_template
import csv

app = Flask(__name__)        

def readfile():
    occupations = []
    with open('data/occupations.csv') as text:
        reader = csv.reader(text)
        next(reader)
        for row in reader:
            if len(row) == 3:
                occupation = row[0]
                percentage = float(row[1])
                link = row[2]
                occupations.append((occupation, percentage, link))
    return occupations

def generateRandom(occupations):
    generated = random.random() * 99.8
    for occupation, percentage, link in occupations:
        generated -= percentage
        if generated < 0:
            return occupation, percentage, link
    return "error", 0, ""

@app.route("/wdywtbwygp")
def page():
    occupations = readfile()
    random_occupation, percentage, link = generateRandom(occupations)
    return render_template('tablified.html', title="Job Helper", occupation=f"{random_occupation}, {percentage}%", link=link, Header="Table", collection=occupations)

if __name__ == "__main__":
    app.debug = True
    app.run()
