from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! from Python Program..............This is version V0.1'

if __name__ == '__main__':
    app.run(debug=True)
