from datetime import datetime
from sqlmodel import Session, desc
from fastapi import Depends
from models.wifi import Wifi
from configuration.database import get_session
from typing import List


class Repository:
    db: Session

    def __init__(self, db: Session = Depends(get_session)) -> None:
        self.db = db

    def create(self, wifi: Wifi) -> Wifi:
        wifi.created_at = datetime.utcnow()

        self.db.add(wifi)
        self.db.commit()
        self.db.refresh(wifi)
        return wifi

    def list(self) -> List[Wifi]:
        return self.db.query(Wifi).order_by(desc(Wifi.id)).all()

    def delete_by_id(self, wifi_id: int) -> bool:
        wifi = self.db.get(Wifi, wifi_id)

        if wifi:
            self.db.delete(wifi)
            self.db.commit()
            return True
        return False

    def delete_all(self):
        wifis = self.db.query(Wifi).all()

        for wifi in wifis:
            print(wifi)
            self.db.delete(wifi)
            self.db.commit()
