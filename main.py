from flask import Flask, jsonify, request,make_response

app = Flask(__name__)
def _corsify(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    resp.headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
    return resp

@app.route('/access_with_javascript', methods=['GET'])
def access_with_javascript():
    result = {"message": "Hello from Flask GET!"}
    response = jsonify(result)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/post_something', methods=['POST', 'OPTIONS'])
def post_something():
    if request.method == 'OPTIONS':
        return _corsify(make_response('', 204))   # preflight OK

    data = request.get_json() or {}
    print("Received from JS:", data)
    input_var = data.get('inputVar')
    result_value = input_var * 10 if input_var is not None else None
    return _corsify(jsonify(status="success",
                            received_input=input_var,
                            computed_result=result_value))

if __name__ == '__main__':
    app.run(host='localhost', port=8989)
