from sqlalchemy import Column, Integer, String
from app.Database.session import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable= False)
    description = Column(String, nullable=True)
    status = Column(String, default="new", nullable=False)