#step 1 - import flask
from flask import Flask, request

# step -2 - Create an object

app = Flask(__name__)

# step - 3 - create an endpoint
@app.route('/')
def home_page():
    return "<h1 style='background-color:red;'>Hello Innomatics Interns</h1><h3 style='color:blue;'>My Name is </h3>"

@app.route('/about')
def about_page():
    return "<h3 style='background-color:yellow;'>We can connect on Linkedin</h3><a href='https://www.linkedin.com/in/jagadeeshmerugu/' target='_blank'>Linkedin</a>"

@app.route('/uppercase')
def upperCase():
    name = request.args.get('name')
    if name:
        name = name.upper()

        return f'<div><h1>Flask Backend Assignment</h1></br><h3>Your Username in uppercase is {name}</h3><body>Hello {name}, how can Innomatics Research lab help you? </body></div>'
    else:
        return '<div><h1>Flask Backend Assignment</h1></br><h3>Kindly input your username </h3></div>'
        


@app.route('/factorial')
def Factorial():
    a = int(request.args.get('a'))
    factorial = 1
    for i in range(1,a):
        factorial = factorial*i

    return str(factorial)


@app.route('/innomatics')
def quiz():
    if 3*0.1 == 0.3 and 4*0.1 == 0.4:
        return "INNOMATICS"
    elif 3*0.1 == 0.3 and 4*0.1 != 0.4:
        return "INNOMATICS RESEARCH"

    elif 3*0.1 != 0.3 and 4*0.1 == 0.4:
        return "INNOMATICS RESEARCH LAB"



# step - 4 - Run the flask application
if __name__ == "__main__":
    app.run(debug=True)
