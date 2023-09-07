from sqlalchemy import Table,Column,ForeignKey,Integer
from .base import Base
customer_bank_association = Table(
    'customer_bank_association',
    Base.metadata,
    Column('customer_id',Integer,ForeignKey('customers.id')),
    Column('bank_id',Integer,ForeignKey('banks.id'))
)