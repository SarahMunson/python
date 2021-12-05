from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def root():
    result = helper(8, 8)
    return render_template('index.html', result = result)
#8 by 8 checkerboard

@app.route('/<int:y>')
def routes(y):
    result = helper(8, y)
    return render_template('index.html', result = result)

@app.route('/<int:x>/<int:y>')
def dynamic(x, y):
    result = helper(x, y)
    return render_template('index.html', result = result)

def helper(x, y):
    result = []
    for i in range(0, x):
        list = []
        for j in range(0, y):
            list.append((j + i) % 2)
        result.append(list)
    return result
print(helper(8,8))


if __name__ == "__main__":
    app.run(debug=True)