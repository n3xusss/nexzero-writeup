from flask import Flask, request, jsonify
import js2py

app = Flask(__name__)

@app.route('/execute-js', methods=['POST'])
def execute_js():
    try:
        js_code = request.json['code']
        js_result = js2py.eval_js(js_code)
        return jsonify({'result': str(js_result)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)
