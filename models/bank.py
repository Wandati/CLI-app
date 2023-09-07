from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
from .base import Base
from .associations import customer_bank_association
class Bank(Base):
    __tablename__ = 'banks'
    id = Column(Integer,primary_key=True)
    name = Column(String)
    location = Column(String,nullable=True)
    users = relationship('Customer',secondary=customer_bank_association,back_populates='banks')
    account = relationship('Account',back_populates='banks')
    def __repr__(self):
        return f"{self.name} located at {self.adress}"