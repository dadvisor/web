import os

from flask import Flask

from loadThread import LoadThread

app = Flask(__name__)


@app.route('/')
def home():
    LoadThread(os.environ.get('ITERATIONS', 10**8)).start()
    return 'Ok'


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=6000)
