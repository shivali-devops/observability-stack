from flask import Flask
from prometheus_client import Counter, generate_latest , CONTENT_TYPE_LATEST

app = Flask(__name__)

request_counter = Counter("app_requests_total", "Total requests to the app")

@app.route("/")
def home():
    request_counter.inc()
    return "Hello! This is a monitored app."

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
