import os

from flask import Flask

from loadThread import LoadThread

app = Flask(__name__)

ITERATIONS = int(os.environ.get('ITERATIONS', 10**7))
print('Iterations: {}'.format(ITERATIONS))


@app.route('/')
def home():
    if ITERATIONS > 0:
        LoadThread(ITERATIONS).start()
    return 'Ok'


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=6000)
