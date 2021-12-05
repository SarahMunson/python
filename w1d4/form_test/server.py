from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes


@app.route('/')
def root():
    return render_template('index.html')


# adding this method
@app.route('/show')
def show_user():
    return render_template('show.html')


@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')



if __name__ == "__main__":
    app.run(debug = True)