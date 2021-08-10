from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    compNum = random.randint(1,100)
    if 'compGuess' not in session:
        session['compGuess'] = compNum
    # if user guess in session
    userNum = int(session['userGuess'])
    compNum = int(session['compGuess'])
    if userNum == compNum:
        gameResult = str(userNum) + "was the number!"
    elif userNum < compNum:
        gameResult = "too low!"
    elif userNum > compNum:
        gameResult = "too high!"

    return render_template('index.html', computerNum = session['compGuess'], userNum = "1")


@app.route('/formintake', methods=['POST'])
def form():
    session['userGuess'] = request.form['userinput']
    # userNum = int(session['userGuess'])
    # compNum = int(session['compGuess'])
    # if userNum == compNum:
    #     gameResult = str(userNum) + "was the number!"
    # elif userNum < compNum:
    #     gameResult = "too low!"
    # elif userNum > compNum:
    #     gameResult = "too high!"

    return redirect('index.html')


@app.route('/reset', methods=['GET'])
def reset():
    session.clear()

    return redirect('/')


if __name__==("__main__"):
    app.run(debug=True)