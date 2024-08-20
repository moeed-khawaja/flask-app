from flask import Flask
from redis import Redis
import os

app = Flask(__name__)

redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_password = os.getenv('REDIS_PASSWORD', None)

redis = Redis(host=redis_host, port=6379, password=redis_password)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return f'Hello! This page has been visited {count} times.'

if __name__ == "__main__":
    port = int(os.getenv('PORT', 8000))
    app.run(host="0.0.0.0", port=port)
