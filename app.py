from flask import Flask
from redis import Redis
import os

app = Flask(__name__)

# Environment variable with correct name (case-sensitive)
redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_password = os.getenv('REDIS_PASSWORD', None)

# Connect to Redis using environment variables or defaults
try:
    redis = Redis(host=redis_host, port=6379, password=redis_password)
except ConnectionError as e:
    print(f"Error connecting to Redis: {e}")
    redis = None  # Handle the error appropriately

@app.route('/')
def hello():
    """Increments a counter in Redis and displays the hit count."""

    if redis:  # Check if Redis connection is successful
        count = redis.incr('hits')
        return f'Hello! This page has been visited {count} times.'
    else:
        return 'Error: Could not connect to Redis cache.'

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
