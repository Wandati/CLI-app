# # from faker import Faker
# session.query(Customer).delete()
# session.query(Account).delete()
# session.query(Bank).delete()
# # session.query(customer_bank_association).delete()
# session.commit()

# customer1 =Customer(first_name ="brian",last_name = "paul")
# customer2 =Customer(first_name ="paul",last_name = "Bamford")
# customer3 =Customer(first_name ="henry",last_name = "clarkson")
# session.add_all([customer1,customer2,customer3])
# session.commit()
# Banks = ['equity','Kcb','Cooperative','national','absa']
# bank1 = Bank(name =random.choice(Banks),adress= 'Nairobi')
# bank2 = Bank(name = random.choice(Banks),adress= 'Mombasa')
# session.add_all([bank1,bank2])
# session.commit()
# account1=Account(number=1234555,amount=505500)
# account2=Account(number=23443245,amount=600440)
# account3=Account(number=34242425,amount=600004)
# account4=Account(number=49324092,amount=670770)
# account5=Account(number=43242325,amount=234423)
# session.add_all([account1,account2,account3,account4,account5])
# session.commit()

# Accounts = session.query(Account).all()
# Banks = session.query(Bank).all()
# Customers = session.query(Customer).all()

# # for account in Accounts:
# #     print(account)
# # for customer in Customers:
# #     print(customer)
# # for bank in Banks:
# #     print(bank)
    
    
# customer1.accounts.append(account1)
# customer1.accounts.append(account2)
# customer1.accounts.append(account3)
# session.commit()

# # for accounts in customer1.accounts:
# #     print(accounts.amount)
# bank1.account.append(account1)
# session.commit()
# bank2.account.append(account2)
# bank2.account.append(account3)
# bank2.account.append(account4)
# bank2.account.append(account5)
# session.commit()

# # for accounts in bank1.account:
# #     print(accounts)
# # for accounts in bank2.account:
# #     print(accounts)
    
# bank1.users.append(customer1)
# bank2.users.append(customer2)
# bank2.users.append(customer3)
# session.commit()

# customer1.make_deposit(ac_number=1234555,amount=50000)
# session.commit()
# for account in customer1.accounts:
#     print(account)
    
# # account = session.query(Account).filter_by(account_number=account_number).first()
# # customer1.
# # bank1 = session.query(Bank).first()
# # session.delete(customer3)
# # session.delete(bank1)
# # session.commit()
# account5 = customer1.open_account(405660)
# # session.add(account5)
# # session.commit()


# # for account in customer1.accounts:
# #     print(account)
    
# customer1.make_withdrawal(ac_number=1234555,amount=1300000)
# session.commit()

# for account in customer1.accounts:
#     print(account)