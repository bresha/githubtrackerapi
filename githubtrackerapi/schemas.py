from pydantic import BaseModel
from datetime import datetime
import json

class GithubMember(BaseModel):
    id: int
    handler: str
    date_added: datetime | None


def load_db() -> list[GithubMember]:
    with open("githubmembers.json") as f:
        return [GithubMember.parse_obj(obj) for obj in json.load(f)]
