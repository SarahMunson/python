from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it safe'

@app.route('/')
def root ():
    if "your_gold" not in session:
        session["your_gold"] = 0
    return render_template('index.html')

app.route('/redirect', methods=['POST'])
def re_direct():
    session['farm'] = request.form['farm']
    session['cave'] = request.form['cave']
    session['house'] = request.form['house']
    session['casino'] = request.form['casino']
    return redirect('/')
    

if __name__ == "__main__":
    app.run(debug = True)