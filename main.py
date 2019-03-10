from flask import Flask, request, jsonify
import random

app = Flask(__name__)


@app.route('/')
def hello_world():
  return 'Hola Mundo'

@app.route('/hello/<string:name>')
def hello(name):
  return "Hola %s" % name

@app.route('/sum')
def sum():
  n1 = request.args.get('n1', default = 0, type = int)
  n2 = request.args.get('n2', default = 0, type = int)
  return jsonify(
    response = n1 + n2
  )

@app.route('/random')
def random_numbers():
  return jsonify(
    response = random.randint(1, 100)
  )

if __name__ == '__main__':
  app.run()