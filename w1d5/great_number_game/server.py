from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'keep it safe'

@app.route('/')
def root():
    if "num" not in session:
        session['num'] = random.randint(1, 100)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/playagain')
def play_again():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)