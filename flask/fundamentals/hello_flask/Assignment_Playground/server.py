from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def index():
    return render_template('index.html')

@app.route('/play/<number>')
def boxNum(number):
    trueNumber = int(number)
    return render_template("./templates/index.html", trueNumber)


@app.route('/play/<number>/<newColor>')
def boxNumColor(number, newColor):
    trueNumber = int(number)
    return render_template("./templates/index.html", trueNumber, newColor)

if __name__=="__main__":
    app.run(debug=True)