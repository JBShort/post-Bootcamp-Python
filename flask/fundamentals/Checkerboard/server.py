from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<number>')
def yBoard(number):
    intNumber = int(number)
    return render_template('index.html', number = intNumber)


@app.route('/x/y')
def xbyYBoard(x,y):
    intx = int(x)
    inty = int(y)
    return render_template('./templates/index.html', x = intx, y = inty)


if __name__=="__main__":
    app.run(debug=True)