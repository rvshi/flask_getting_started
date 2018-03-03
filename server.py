from flask import Flask, jsonify, request
from jsonschema import validate, ValidationError
import math

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return 'Welcome to the server'


@app.route('/<name>', methods=['GET'])
def name(name):
    data = {
        'name': name
    }
    return jsonify(data)


@app.route('/hello/<name>', methods=['GET'])
def hello_name(name):
    data = {
        'message': 'Hello there,  {}'.format(name)
    }
    return jsonify(data)


def pythagorean(l1, l2):
    return math.sqrt(l1 ** (2) + l2 ** (2))


@app.route('/distance', methods=['POST'])
def distance():
    array_type = {
        'type': 'array',
        'items': {
            'type': 'number'
        },
        'minItems': 2,
        'maxItems': 2
    }
    schema = {
        'type': 'object',
        'properties': {
            'a': array_type,
            'b': array_type
        },
	"required": ["a", "b"],
	'additionalProperties': False
    }

    r = request.get_json()
    try:
        validate(r, schema)
    except ValidationError:
        res = {
            'message': 'ERROR: data was incorrectly formatted.',
            'input': r
        }
        return jsonify(res), 400

    a = [int(i) for i in r['a']]
    b = [int(i) for i in r['b']]

    dist = pythagorean(b[0] - a[0],
                       b[1] - a[1])
    res = {
        'input': r,
        'distance': round(dist, 5)
    }
    return jsonify(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)

