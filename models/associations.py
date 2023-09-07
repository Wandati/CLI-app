from sqlalchemy import Table,Column,ForeignKey,Integer
# from sqlalchemy.orm import declarative_base
from .base import Base
# Base = declarative_base()
customer_bank_association = Table(
    'customer_bank_association',
    Base.metadata,
    Column('customer_id',Integer,ForeignKey('customers.id')),
    Column('bank_id',Integer,ForeignKey('banks.id'))
)