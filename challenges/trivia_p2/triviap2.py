#!/usr/bin/python3
from flask import Flask
from flask import request
from flask import session
from flask import redirect
from flask import render_template
import triviaapi

app = Flask(__name__)
app.secret_key = "viaanRaj"

user_name = "Lok"
question_answer_dict = triviaapi.question_and_answer()
question= question_answer_dict["question"]
answer= question_answer_dict["answer"]

@app.route("/")
def home():
    return render_template('home.html',name=user_name, question_answer_dict = question_answer_dict, answer=answer,)

@app.route("/incorrect")
def incorrect():
    return render_template('incorrect.html')

@app.route("/correct")
def correct():
    trivia_answer_option = session['user_input']
    print(trivia_answer_option)
    return render_template('correct.html',name=user_name, question_answer_dict = question_answer_dict, answer=answer,trivia_answer_option=trivia_answer_option)

@app.route("/home", methods=["POST"])
def correct_answer():
    trivia_answer_option = request.form['answer']
    session['user_input'] = trivia_answer_option
    if(question_answer_dict[trivia_answer_option].upper() == answer.upper()):
        return redirect("/correct")
    else:
        return redirect("/incorrect")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
