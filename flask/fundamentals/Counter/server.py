from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
# remember to use redirect instead of return for POST



@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] = session['counter'] + 1
    return render_template('index.html')

@app.route('/destroy_session')
def destry_session():
    session.clear()		# clears all keys
    return redirect('/')



if __name__=="__main__":
    app.run(debug=True)