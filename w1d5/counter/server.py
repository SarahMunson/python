from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it safe'

@app.route('/')
def main():
    return render_template('index.html')

# @app.route('/', method=['POST'])
# def main():
#     return redirect('/tracker')

@app.route('/tracker')
def tracker():
#     if 'key_name' in session:
#       print('key exists!')
# else:
#     print("key 'key_name' does NOT exist")

    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return render_template('counter.html')


if __name__ == "__main__":
    app.run(debug=True)