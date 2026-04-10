from flask import Flask, request, jsonify

app = Flask(__name__)

# Test API route
@app.route('/api/test', methods=['POST'])
def test_api():
    data = request.get_json()
    
    name = data.get('name', 'Guest')
    
    return jsonify({
        "message": f"Hello {name}, Backend Connected Successfully 🚀"
    })

if __name__ == '__main__':
    app.run(debug=True)