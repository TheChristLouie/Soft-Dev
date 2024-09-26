# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024
# Comments: Doesn't print anything to terminal.

from flask import Flask
app = Flask(__name__)            #create instance of class Flask

@app.route("/")                  #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

