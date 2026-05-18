from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)   # allow frontend requests

@app.route("/")
def home():
    return jsonify({
        "message": "Backend connected successfully from Render 🚀"
    })

@app.route("/about")
def about():
    return jsonify({
        "project": "Render Deployment Test",
        "status": "Working fine"
    })

if __name__ == "__main__":
    app.run(debug=True)
