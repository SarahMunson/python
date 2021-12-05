from flask import Flask, render_template 
app = Flask(__name__)

@app('/')
def index():
    return render_template('index.html')

@app('/play/<num>')
def num(num):
    return render_template('index.html', num = int(num))

if __name__ == '__main__':
    app.run(debug=True)