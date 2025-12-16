from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Hello, Flask in Docker!"

# Health check (very useful for Docker & Kubernetes)
@app.route('/health')
def health():
    return jsonify(status="ok"), 200

# Simple API route
@app.route('/api/hello')
def hello():
    name = request.args.get('name', 'World')
    return jsonify(
        message=f"Hello {name}!",
        time=datetime.utcnow().isoformat()
    )

# Math route
@app.route('/api/add')
def add():
    try:
        a = int(request.args.get('a', 0))
        b = int(request.args.get('b', 0))
        return jsonify(
            a=a,
            b=b,
            result=a + b
        )
    except ValueError:
        return jsonify(error="a and b must be numbers"), 400

# Echo JSON (POST)
@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json()
    if not data:
        return jsonify(error="JSON body required"), 400
    return jsonify(received=data)

# List example items
@app.route('/api/items')
def items():
    items = ["apple", "banana", "orange"]
    return jsonify(items=items, count=len(items))

# 404 handler
@app.errorhandler(404)
def not_found(e):
    return jsonify(error="Route not found"), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
