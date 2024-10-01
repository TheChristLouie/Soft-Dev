#Christopher Louie, Sasha Murokh
#SoftDev
#File Reading
#2024/9/18
#Time Spent: 30

import random
from flask import Flask
app = Flask(__name__)                 

def readfile():
    occupations = {}
    with open('occupations.csv') as text:
        reader = text.read()
        reader = reader.split('\n')
        for row in range(len(reader)-2):
            if '"' in reader[row+1]:
                reader[row+1] = reader[row+1].split('",')
                reader[row+1][0] = reader[row+1][0][1:]
            else:
                reader[row+1] = reader[row+1].split(',')
            occupations[reader[row+1][0]]=float(reader[row+1][1])
    return occupations

def generateRandom(occupations):
    generated = random.random()*99.8
    for key in occupations.keys():
        generated-=occupations[key]
        if (generated<0):
            return(str(key)+', ' +str(occupations[key]))
    return("error")

@app.route("/")
def page():         
    occ = generateRandom(readfile())
    code = """
    <!DOCTYPE html>
    <html>
      <body>
            <p>Death Row Coders: Raymond, Christopher, Kevin)</p>
            <p>SoftDev</p>
            <p>File Reading + HTML coding</p>
            <p>2024/9/18</p>
            <p>Time Spent: 180</p>
            <h2>Randomly selected occupation: """ + occ + """
            <h1>Occupations Table</h2>
            <table>
    """
    for a, b in readfile().items():
        code += "<tr><td>" + a + "</td><td>" + str(b) + "</td></tr>"

    code += "</table></body></html>"
    return code

app.debug = True
app.run()