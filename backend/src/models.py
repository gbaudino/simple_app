from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session


class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    surname = Column(String, index=True)
    email = Column(String, unique=True, index=True)


class LeadsDAO:
    def __init__(self, db: Session):
        self.__db = db

    def create_lead(self, name: str, surname: str, email: str):
        db_lead = Lead(name=name, surname=surname, email=email)
        self.__db.add(db_lead)
        self.__db.commit()
        self.__db.refresh(db_lead)
        return db_lead

    def get_lead_by_id(self, id: int):
        return self.__db.query(Lead).filter(Lead.id == id).first()

    def update_lead_email(self, id: int, new_email: str):
        lead = self.__db.query(Lead).filter(Lead.id == id).first()
        if lead:
            lead.email = new_email
            self.__db.commit()
            self.__db.refresh(lead)
        return lead

    def delete_lead(self, id: int) -> None:
        lead = self.__db.query(Lead).filter(Lead.id == id).first()
        if lead:
            self.__db.delete(lead)
            self.__db.commit()
