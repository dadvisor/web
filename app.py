import os

from flask import Flask, request

from loadThread import LoadThread

app = Flask(__name__)

ITERATIONS = int(os.environ.get('ITERATIONS', 10 ** 7))
print('Iterations: {}'.format(ITERATIONS))


@app.route('/')
def home():
    if ITERATIONS > 0:
        LoadThread(ITERATIONS).start()
    return 'Ok'


@app.route('/with_load')
def with_load():
    try:
        load = int(request.args.get('load', default='1'))
    except Exception as e:
        print(e)
        load = 1
    return '*' * load


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=6000)
