from datetime import datetime
from fastapi import FastAPI

from .schemas import load_db, save_db, GithubMember


app = FastAPI()


db = load_db()


@app.get("/")
async def welcome():
    """Returns a friendly welcome message"""
    return {'message': "Welkom to Github tracking service"}

@app.get("/date")
async def current_date():
    "Returns current date "
    return {'current_date': datetime.now()}

@app.get("/api/githubmembers")
def get_githubmembers():
    return db


@app.get("/api/githubmembers/{handler}")
def get_githubmember(handler: str) -> list:
    return [item for item in db if item.handler == handler]

@app.post("/api/githubmembers")
def add_githubmember(gm: GithubMember) -> None:
    db.append(gm)
    save_db(db)

