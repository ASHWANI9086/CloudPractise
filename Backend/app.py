from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app, origins="*")  # ✅ IMPORTANT FIX

@app.route('/')
def home():
    return "Backend is Running 🚀"

@app.route('/api/test', methods=['POST'])
def test_api():
    data = request.get_json()
    name = data.get('name', 'Guest')

    return jsonify({
        "message": f"Hello {name}, Backend Connected Successfully 🚀"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)