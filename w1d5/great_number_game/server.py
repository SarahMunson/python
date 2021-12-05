from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it safe'

@app.route('/')
def root():
    session['random_number'] = 55
    if int(session['guess']) < session['random_number']:
        print("Too Low")
    elif int(session['guess']) > session['random_number']:
        print("Too high")
    else:
        print("You guessed it!")
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    session['random_number'] = 55
    if int(session['guess']) < session['random_number']:
        print("Too Low")
    elif int(session['guess']) > session['random_number']:
        print("Too high")
    else:
        print("You guessed it!")
    return redirect('/')



if __name__ == "__main__":
    app.run(debug = True)