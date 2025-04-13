from flask import Flask
from ddtrace import patch_all, tracer
import time
import os


# Set environment variables (you can also set these in your shell environment)
os.environ['DD_AGENT_HOST'] = 'localhost'  # Hostname of the Datadog Agent
os.environ['DD_TRACE_AGENT_PORT'] = '8126'  # Default trace port for Datadog
os.environ['DD_ENV'] = 'local'  # Environment name
os.environ['DD_SERVICE'] = 'datadog-python-flask'  # Service name
os.environ['DD_VERSION'] = '1.0.0'  # Version of your service

# Automatically patch all supported libraries (Flask, requests, etc.)
patch_all()

app = Flask(__name__)

@app.route("/")
def index():
    with tracer.trace("custom.index.handler", service="datadog-python-flask") as span:
        span.set_tag("custom-tag", "homepage")
        time.sleep(0.2)  # simulate some work
        return "Hello from Flask with Datadog tracing!"

@app.route("/compute")
def compute():
    with tracer.trace("custom.compute.operation", service="datadog-python-flask") as span:
        span.set_tag("task", "fibonacci")
        result = fibonacci(10)
        span.set_tag("result", result)
        return f"Fibonacci(10): {result}"

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

@app.route("/health")
def health():
    return "Health Check OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
