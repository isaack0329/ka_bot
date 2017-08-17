from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world!'
@app.route('/keyboard')
def keboard_input():
    return "안녕하세요~~~~~~~"

if __name__ == '__main__':
    app.debug = True
    app.run()

