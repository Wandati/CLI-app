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

    # def open_account(self,initial_balance):
    #     customer = session.query(Customer).filter_by(id=self.id).first()
    #     if customer:
    #         if initial_balance > 500:
    #             new_account = Account(number= random.randint(1000000,6000000),amount=initial_balance)
    #             customer.accounts.append(new_account)
    #             session.commit()
                
    #             # session.add(new_account)
    #             # session.commit()
    #         else:
    #             print("deposit cannot be less than 500!!")
    #     else:
    #         print("Customer not Found!!!")
    #     # session.add(new_account)
    #     # session.commit()
    #     # return new_account
    # def make_deposit(self,ac_number,amount):
    #     account = session.query(Account).filter_by(number=ac_number).first()
    #     if account in self.accounts:
    #         account.amount += amount
    #     else:
    #         print("Invalid Account!!")
       
            
    #     # if ac_number == Account.number:
    #     #     Account.amount += amount
    #     # else:
    #     #     print("Invalid Account!!!")
    #     # if ac_number :
    #     #     self.accounts.amount += amount
    #     # else:
    #     #     print("invalid Account!!")
    #     # for account in self.accounts:
    #     #     if account.number == ac_number:
    #     #         account.amount += amount
    #     #         new_balance = account.amount
    #     #     else:
    #     #         print("Invalid Account Number!!")
    #     # return new_balance
    # def make_withdrawal(self,ac_number,amount):
    #     account = session.query(Account).filter_by(number=ac_number).first()
    #     if account in self.accounts:
    #         if amount > 0 and  amount < account.amount:
    #             account.amount -= amount
    #         else:
    #             print("Withdrawal cannot be less than 0 or  more than the remaining balance")
    #     else:
    #         print("Invalid Account!!!")
        
    def __repr__(self):
        return f" Customer Name: {self.name}"      
    # def __repr__(self):
    #     return f'Full Names: {self.first_name}, {self.last_name}'