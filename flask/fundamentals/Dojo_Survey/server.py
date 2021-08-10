from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    print(request.form)
    formName = request.form['name']
    formLocation = request.form['location']
    formLanguage = request.form['language']
    text = request.form['comment']
    return render_template('show.html', formName = formName, formLocation = formLocation, formLanguage = formLanguage, text = text)


if __name__=="__main__":
    app.run(debug=True)