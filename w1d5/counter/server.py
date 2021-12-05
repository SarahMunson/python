from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it safe'

@app.route('/')
def main():
    if 'counter' not in session:
        session['counter'] = 0
    else:
        session['counter'] += 1
    return render_template('index.html')

@app.route('/tracker')
def tracker():
    session['counter'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

@app.route('/choose', methods=['POST'])
def choose():
    session['choose'] = int(request.form['choose'])
    session['counter'] += session['choose'] - 1
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)