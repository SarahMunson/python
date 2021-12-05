from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = 'keep it safe'

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/return_session', methods = ['POST'])
def return_session():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['fave_language'] = request.form['fave_language']
    session['comment'] = request.form['comment']
    return redirect('/post')

@app.route('/post')
def post():
    return render_template('post.html')


if __name__ == "__main__":
    app.run(debug = True)