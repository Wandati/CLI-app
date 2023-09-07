from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import relationship
from .base import Base
from .associations import customer_bank_association
class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer,primary_key=True)
    # first_name = Column(String)
    # last_name = Column(String)
    name = Column(String)
    accounts = relationship('Account',back_populates='users',cascade='all, delete')
    banks = relationship('Bank',secondary=customer_bank_association,back_populates='users')

    def __repr__(self):
        return f" Customer Name: {self.name}"      