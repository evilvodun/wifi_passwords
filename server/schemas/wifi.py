from sqlmodel import SQLModel


class WifiInput(SQLModel):
    computer_name: str
    ssid: str
    password: str
