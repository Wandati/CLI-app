from sqlalchemy import Column,Integer,ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer,primary_key=True)
    number = Column(Integer)
    amount = Column(Integer)
    customer_id = Column(Integer,ForeignKey('customers.id'))
    bank_id = Column(Integer,ForeignKey('banks.id'))
    users = relationship('Customer',back_populates='accounts')
    banks = relationship('Bank',back_populates='account')
    
    def __repr__(self):
        return f"Account Number:{self.number} ,Available Balance: {self.amount}"