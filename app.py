from flask import Flask, jsonify

app = Flask(__name__)

@app.get('/')
def home():
    return jsonify(message='Hello from my DevOps CI/CD project!', status='running')

@app.get('/health')
def health():
    return jsonify(status='healthy'), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
