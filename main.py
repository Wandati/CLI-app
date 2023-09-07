from models.account import Account
from models.customer import Customer
from models.bank import Bank
from models.base import Base
import click
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///Bank_management.db')
Session = sessionmaker(bind=engine)
session = Session()
banks = { 'names':['Equity','Cooperative','Ncba','Absa'],
         'location':['Nairobi','Kisumu','Mombasa']
         }

session.query(Bank).delete()
bank1 = Bank(name = banks['names'][2],location =banks['location'][0] )
bank2 = Bank(name = banks['names'][1],location =banks['location'][2] )
bank3 = Bank(name = banks['names'][0],location =banks['location'][1] )
session.add_all([bank1,bank2,bank3])
session.commit()
list_banks = [bank1,bank2,bank3]

    
@click.group()
def cli():
    pass
@cli.command()

@click.option('--name', prompt='Customer name', help='Name of the Customer')
# creating a customer
def create_customer(name):
    new_customer = session.query(Customer).filter_by(name=name).first()
    if not new_customer:
        new_customer = Customer(name=name)
        session.add(new_customer)
        # bank1.users.append(new_customer)
        random.choice(list_banks).users.append(new_customer)
        session.commit()
        click.echo(f"Customer: {name} has been created.")
    else:
        click.echo(f"Customer {new_customer.name} already exists")
    
@cli.command() 
@click.option('--id', prompt='Customer id', help='id of the Customer',type=int)
@click.option('--amount', prompt='Amount', help='deposit Amount',type = float)
def open_account(id,amount):
    banks = session.query(Bank).all()
    customer = session.query(Customer).filter_by(id=id).first()
    
    if customer:
        if amount >= 500:
                new_account = Account(number= random.randint(1000000,6000000),amount=amount)
                # session.add(new_account)
                customer.accounts.append(new_account)
                for bank in banks:
                    if customer in bank.users:
                        bank.account.append(new_account)
                # customer.banks.append(new_account)
                # customer.banks.
                # random.choice(list_banks).account.append(new_account)
                session.commit()
                click.echo(f"Account opened for {customer.name} with an initial deposit of: {amount} Kshs.")
                
        else:
            
            click.echo("deposit cannot be less than 500!")
    else:
        click.echo("Customer not Found!")


@cli.command
@click.option('--id', prompt='Customer id', help='id of the Customer',type =int)
@click.option('--amount', prompt='Deposit Amount', help='deposit Amount',type=float)


def make_deposit(id,amount):
    user = session.query(Customer).filter_by(id=id).first()
    account = session.query(Account).filter_by(customer_id =id).first()
    if user and account:
        if amount >= 1:
            account.amount += amount
            session.commit()
            click.echo(f"You Have Deposited {amount} Kshs into account No: {account.number}. New Account Balance is : {account.amount} Kshs")
        else:
            click.echo("Deposit Cannot be less than or equal to 0!")
    elif user and not account:
        click.echo('Account does not exist!')
    else:
        click.echo(" User does not exist!")
    
@cli.command() 
@click.option('--id', prompt='Customer id', help='id of the Customer',type=int)
@click.option('--amount', prompt='Withdrwal Amount', help='Withdrawal Amount',type = int)
def make_withdrawal(id,amount):
    user = session.query(Customer).filter_by(id=id).first()
    account = session.query(Account).filter_by(customer_id=id).first()
    if user and account :
        if amount > 0 and  amount < account.amount:
            account.amount -= amount
            session.commit()
            click.echo(f"Successful Withdrawal of {amount} Kshs from account No: {account.number}. New Account Balance is: {account.amount} Kshs.")
        else:
            click.echo("Withdrawal cannot be less than or equal to 0 or more than the remaining balance!")
    elif user and not account:
        click.echo(" Account Does not exist!")
    else:
        click.echo("User does not exist!")

@cli.command() 
@click.option('--id', prompt='Customer id', help='id of the Customer',type=int)

def check_personal_accounts(id):
    # accounts = session.query(Account).all()
    
    customer = session.query(Customer).filter_by(id=id).first()
    if customer and not customer.accounts:
        click.echo(f'Customer: {customer.name}\n' + 'No Accounts Found!')
    elif customer and customer.accounts:
        click.echo(f'Customer: {customer.name}')
        for account in customer.accounts:
            click.echo(f'Accounts: {account}')

    else:
        return click.echo('User not found!')
                  
        
@cli.command
@click.option('--id',prompt="Bank Id",help="Displaying Bank details")
def display_bank_users(id):
    bank = session.query(Bank).filter_by(id=id).first()
    
    if bank and not bank.users:
        click.echo(f'Bank: {bank.name}\n' + 'No Users Registered!')
    elif bank and bank.users:
        click.echo(f'Bank: {bank.name}')
        for user in bank.users:
            click.echo(f'Users: {user.name}')

    else:
        return click.echo('Bank not found!')
        
        
@cli.command() 
@click.option('--id', prompt='Customer id', help='id of the Customer to delete',type=int)
def delete_customer(id):
    customer = session.query(Customer).filter_by(id=id).first()
    if customer:
        session.delete(customer)
        session.commit()
        click.echo(f'Customer {customer.name} has been deleted successfully.')
    else:
        click.echo("No customers found.") 
   

if __name__ == '__main__':
    cli()
