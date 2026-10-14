
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello from Flask! My DevOps project is running."


@app.route("/health")
def health():
    return {"status": "healthy"}