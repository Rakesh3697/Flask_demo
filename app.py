from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Flask app deployed successfully on Render 🚀"
    })

@app.route("/about")
def about():
    return jsonify({
        "project": "Render Deployment Test",
        "status": "Working fine"
    })

if __name__ == "__main__":
    app.run(debug=True)