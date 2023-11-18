from pydantic import BaseModel
from datetime import datetime
import json

class GithubMember(BaseModel):
    id: int
    handler: str
    #date_added: datetime | None


def load_db() -> list[GithubMember]:
    with open("githubtrackerapi/githubmembers.json") as f:
        return [GithubMember.parse_obj(obj) for obj in json.load(f)]

def save_db(gms: list[GithubMember]):
    with open("githubtrackerapi/githubmembers.json", "w") as f:
        json.dump([gm.dict() for gm in gms], f, indent=4)