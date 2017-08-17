from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world!3333333333333333333333'
@app.route('/keyboard')
def keboard_input():
    return "안녕하세요~~~~~~~"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

