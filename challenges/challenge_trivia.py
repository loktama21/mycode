#!/usr/bin/python3

from flask import Flask
from flask import redirect
from flask import session
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def start():
    user = session.get("user")
    return render_template("index.html", user = user)

@app.route("/correct")
def correct():
    return render_template("correct.html")

@app.route("/game", methods = ["POST"])
def gameon():
        if request.form.get("nm") == "Alaska":
                return redirect("/correct")
        else:
            return redirect("/")

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)

