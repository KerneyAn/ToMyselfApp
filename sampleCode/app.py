from flask import Flask

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def say_hello():
    res = 'Hello World'
    return str(res)

if __name__ == '__main__':
        app.run()
