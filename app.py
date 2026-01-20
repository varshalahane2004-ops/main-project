from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "CI/CD Pipeline Working Successfully!"

if __name__ == "_main_":
    app.run(host="0.0.0.0", port=5000)