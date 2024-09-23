#Christopher Louie
#Death Row Coders
#SoftDev
#File Reading
#2024/9/18
#Time Spent: 30

'''
DISCO:
<note any discoveries you made here... no matter how small!>

QCC:
0. In c the @ is a suppressor
1. The / seems to be some sort of route like in the terminal.
2. An erorr appears when it runs - prints to external server http://127.0.0.1:5000
3. "No hablo queso!"
4. It will appear on the external server at the link http://127.0.0.1:5000 that can be put in the browser. Also when the site is accessed stuff prints in the terminal.
5. html website
 ...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?

app.run()                                # Q5: Where have you seen similar constructs in other languages?



