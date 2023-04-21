from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")  #decorator
def index():
    return "Hello World"
#app.add_url_rule("/", "index", index)

@app.route("/ws")
def ws():
    return "Welcome to CAD  Session"

@app.route("/sw/<number>")
def sw(number):
    return "Welcome to CAD Batch {} Session" .format(number)

@app.route("/welcome_students/<int:dnumber>")
def wel_stud(dnumber):
    if dnumber == 1 or dnumber == 5:
        return redirect(url_for("sw", number = dnumber))
    else:
        return redirect(url_for("ws"))

if __name__ == "__main__":
    app.run(debug=True)


#ip address = 127.0.0.1:  / localhost === 0.0.0.0
#port = 5000
#debug = True/False ---- False

# variables - string - int float
#<string>
#<int : number>
#<float: number>