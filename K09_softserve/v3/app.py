# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024
# Comments: prints to terminal some words, and debug is true in this case, saying debugger is active, and it gives a debugger pin in the terminal.

from flask import Flask
app = Flask(__name__)                 #create instance of class Flask

@app.route("/")                       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)                   #where will this go? Goes to terminal
    return "No hablo queso!"

app.debug = True
app.run()
