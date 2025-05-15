from .database import Base
from sqlalchemy import Column, Integer, String, UniqueConstraint

class DbUser(Base):
    __tablename__ = 'user_info'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String, unique=True)
    phonenumber = Column(String, unique=True)
    password = Column(String)