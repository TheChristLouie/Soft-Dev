# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024
# Comments: Prints "about to print __name__..." to terminal, and prints "__main__" to terminal afterwards

from flask import Flask
app = Flask(__name__)             #create instance of class Flask

@app.route("/")                   #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)               #where will this go? clouie50: terminal
    return "No hablo queso!"

app.run()

