from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db.db_setup import Base

class MnistDigit(Base):
    __tablename__ = "mnist_digits"
    
    id = Column(Integer, primary_key=True)
    true_value = Column(Integer, nullable=True)
    predicted_value = Column(Integer)
    # array of numbers
    
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="mnist_digits")
    