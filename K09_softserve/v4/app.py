# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024
# Comments: prints "The __name of this module is... " to terminal, prints "__main__" to terminal, puts "No hablo queso!" on site, and turns debug on.

from flask import Flask
app = Flask(__name__)           #create instance of class Flask

@app.route("/")                 #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":      # true if this file NOT imported
    app.debug = True            # enable auto-reload upon code change
    app.run()
