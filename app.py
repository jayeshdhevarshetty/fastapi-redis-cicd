from fastapi import FastAPI
import redis
import os

app = FastAPI()

REDIS_HOST = os.getenv("REDIS_HOST", "redis")

r = redis.Redis(host=REDIS_HOST, port=6379, decode_responses=True)


@app.get("/")
def home():
    visits = r.incr("visits")

    return {
        "message": "Hello",
        "visits": visits
    }


@app.get("/health")
def health():
    return {
        "status": "UP"
    }