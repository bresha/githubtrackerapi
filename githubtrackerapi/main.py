from datetime import datetime
from fastapi import FastAPI

app = FastAPI()


db = [
    {"id": 1, "handler": "bresha", "date_added": "2023-12-22"},
    {"id": 2, "handler": "mmaljak"},
    {"id": 3, "handler": "valentin994"},
    {"id": 4, "handler": "amotl"},
    {"id": 5, "handler": "adhithiravi"},
    {"id": 6, "handler": "mnajdova"},
    {"id": 7, "handler": "siriwatknp"},
    {"id": 8, "handler": "renovate-bot"},
    {"id": 9, "handler": "michaldudak"},
    {"id": 10, "handler": "mbrookes"},    
]

@app.get("/")
async def welcome():
    """Returns a friendly welcome message"""
    return {'message': "Welkom to Github tracking service"}

@app.get("/date")
async def current_date():
    "Returns current date "
    return {'current_date': datetime.now()}

@app.get("/api/handlers")
def get_handlers():
    return db

@app.get("/api/handlers/{handler}")
def get_handler(handler: str) -> list:
    return [item for item in db if item['handler'] == handler]
