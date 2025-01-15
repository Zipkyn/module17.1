from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.backend.db import Base

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)
    slug = Column(String, unique=True, index=True)

    user = relationship('User', back_populates='tasks')
    __table_args__ = {'extend_existing': True}

from sqlalchemy import create_engine
from sqlalchemy.schema import CreateTable
from app.models.user import User
from app.models.task import Task

engine = create_engine("sqlite:///taskmanager.db", echo=True)

print(CreateTable(User.__table__))
print(CreateTable(Task.__table__))




