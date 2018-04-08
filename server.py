from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "secretKey"


@app.route("/")
def index():
    returnStr = ""
    session["guess"] = "";
    if "randomNum" not in session:
        session["randomNum"] = random.randint(1, 100)
    return render_template('index.html', returnStr = returnStr)

@app.route("/getGuess", methods = ["POST"])
def getGuess():

    if "randomNum" not in session:
        session["randomNum"] = random.randint(1, 100)
        returnStr = ""
        return render_template("index.html", returnStr = returnStr)

    print(session["randomNum"])
    returnStr = ""
    
    session["guess"] = request.form["guess"]

    if int(session["guess"]) > session["randomNum"]:
        print("Too high!")
        returnStr = "Too high!"
        return render_template("index.html", returnStr = returnStr)

    elif int(session["guess"]) < session["randomNum"]:
        returnStr = "Too low!"
        print("Guess was too low")
        return render_template("index.html", returnStr = returnStr)

    else:
        returnStr = str(session["randomNum"]) + " was the number!"
        session.pop("randomNum")
        session.pop("guess")
        return render_template("index.html", returnStr = returnStr)
    

app.run(debug=True)