from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Home route (GET)
@app.route('/')
def home():
    return "Backend is Running 🚀"


# API route (POST)
@app.route('/api/test', methods=['POST'])
def test_api():
    data = request.get_json()

    name = data.get('name', 'Guest')

    return jsonify({
        "message": f"Hello {name}, Backend Connected Successfully 🚀"
    })


if __name__ == '__main__':
    app.run(debug=True)