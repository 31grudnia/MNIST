from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.db_setup import Base


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(100))
    test  = Column(String(100))

    mnist_digits = relationship("MnistDigit", back_populates="user")