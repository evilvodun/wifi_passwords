from datetime import datetime
from sqlmodel import SQLModel, Field


class Wifi(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    computer_name: str
    ssid: str
    password: str
    created_at: datetime | None = None
