from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped

from app.setup.database import Base


class User(Base):
    id: Mapped[int] = Column(Integer, primary_key=True)
    username: Mapped[str] = Column(String, unique=True, index=True)


class Employee(Base):
    id: Mapped[int] = Column(Integer, primary_key=True)
    firstName: Mapped[str] = Column(String(100), nullable=False)
    lastName: Mapped[str] = Column(String(100), nullable=False)
    email: Mapped[str] = Column(String(100), nullable=False)
    phone: Mapped[str] = Column(String(100), nullable=False)
    department: Mapped[str] = Column(String(100), nullable=False)
    position: Mapped[str] = Column(String(100), nullable=False)
    location: Mapped[str] = Column(String(100), nullable=False)
    isActive: Mapped[bool] = Column(Integer, nullable=False, default=True)
    isStarted: Mapped[bool] = Column(Integer, nullable=False, default=False)
    isTerminated: Mapped[bool] = Column(Integer, nullable=False, default=False)
