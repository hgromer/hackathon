from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():
    payload = request.json
    print("Payload received {}".format(payload))

    message_type = payload['type']

    if message_type == 'url_verification':
        return jsonify({
            'challenge': payload['challenge']
        })
    elif message_type == 'message':
        pass

    return jsonify(success=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
