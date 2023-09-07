from models.account import Account
from models.customer import Customer
from models.bank import Bank
from models.base import Base
import click
import random
from models.base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# import random
engine = create_engine('sqlite:///Bank_management.db')
Session = sessionmaker(bind=engine)
session = Session()
# Base.metadata.create_all(engine)
# from cli import session

@click.group()
def cli():
    pass

@click.command()
# @click.argument('first_name')
# @click.argument('last_name')
@click.argument('name')
# creating a customer
def create_customer(name):
    new_customer = session.query(Customer).filter_by(name=name).first()
    if not new_customer:
        new_customer = Customer(name=name)
        session.add(new_customer)
        session.commit()
        click.echo(f"Customer: {name} has been created.")
    else:
        click.echo(f"Customer {new_customer.name} already exists")


@click.command() 
@click.argument('customer_id', type=int)
@click.argument('initial_deposit', type=float)
def open_account(customer_id,initial_deposit):
    
    customer = session.query(Customer).filter_by(id=customer_id).first()
    
    if customer:
        if initial_deposit >= 500:
                new_account = Account(number= random.randint(1000000,6000000),amount=initial_deposit)
                # session.add(new_account)
                customer.accounts.append(new_account)
                session.commit()
                click.echo(f"Account opened for {customer.name} with an initial deposit of: {initial_deposit} Kshs.")
                
                
                # session.add(new_account)
                # session.commit()
        else:
            
            click.echo("deposit cannot be less than 500!")
    else:
        click.echo("Customer not Found!")

@click.command()
@click.argument('user_id',type=int)
@click.argument('amount', type=float)

def make_deposit(user_id,amount):
    user = session.query(Customer).filter_by(id=user_id).first()
    account = session.query(Account).filter_by(customer_id =user_id).first()
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
    

@click.command()
@click.argument('user_id',type =int)
@click.argument('amount', type=float)
def make_withdrawal(user_id,amount):
    user = session.query(Customer).filter_by(id=user_id).first()
    account = session.query(Account).filter_by(customer_id=user_id).first()
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
@click.command()
@click.argument('user_id',type=int)
def check_personal_accounts(user_id):
    # accounts = session.query(Account).all()
    
    customer = session.query(Customer).filter_by(id=user_id).first()
    if customer and not customer.accounts:
        click.echo(f'Customer: {customer.name}\n' + 'No Accounts Found!')
    elif customer and customer.accounts:
        click.echo(f'Customer: {customer.name}')
        for account in customer.accounts:
            click.echo(f'Accounts: {account}')

    else:
        return click.echo('User not found!')
            
            
        

@click.command()
# click.arg
def display_user_accounts():
    Users = session.query(Customer).all()
    for user in Users:
        if user.accounts:
            
            click.echo(f'Username: {user.name} \n'+ f'Accounts: {user.accounts}')
        else:
            click.echo(f'Username: {user.name} \n'+ 'Accounts: None ')
            
@click.command()
@click.argument('user_id',type=int)
def delete_customer(user_id):
    customer = session.query(Customer).filter_by(id=user_id).first()
    if customer:
        session.delete(customer)
        session.commit()
        click.echo(f'Customer {customer.name} has been deleted successfully.')
    else:
        click.echo("No customers found.")         
cli.add_command(create_customer)
cli.add_command(open_account)
cli.add_command(make_deposit)
cli.add_command(make_withdrawal)
cli.add_command(check_personal_accounts)
cli.add_command(display_user_accounts)
cli.add_command(delete_customer)

if __name__ == '__main__':
    cli()
