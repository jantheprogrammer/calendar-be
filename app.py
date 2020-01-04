from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/bok')
def bok():
    return 'bok'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'posted'
    else:
        return 'get'


if __name__ == '__main__':
    app.run(debug=True)
