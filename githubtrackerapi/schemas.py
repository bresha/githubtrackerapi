from pydantic import BaseModel
from datetime import datetime


class GithubMember(BaseModel):
    id: int
    handler: str
    date_added: datetime | None
