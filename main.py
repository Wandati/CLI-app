from models import session,Bank,Account,Customer
import click
import random
import click
from models import session,Customer,Bank,Account

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
        if initial_deposit > 500:
                new_account = Account(number= random.randint(1000000,6000000),amount=initial_deposit)
                # session.add(new_account)
                customer.accounts.append(new_account)
                session.commit()
                click.echo(f"Account opened for {customer.name} with an initial deposit of: {initial_deposit} Kshs.")
                
                
                # session.add(new_account)
                # session.commit()
        else:
            
            click.echo("deposit cannot be less than 500!!")
    else:
        click.echo("Customer not Found!!!")

@click.command()
@click.argument('acc_number',type=int)
@click.argument('amount', type=float)
def make_deposit(acc_number,amount):
    account = session.query(Account).filter_by(number=acc_number).first()
    if account:
        if amount > 1:
            account.amount += amount
            session.commit()
            click.echo(f"Deposited {amount} Kshs into account No: {acc_number}. New Account Balance is : {account.amount} Kshs")
        else:
            click.echo("Deposit Cannot be less than 0")
    else:
        click.echo("Invalid Account!!")

@click.command()
@click.argument('acc_number',type =int)
@click.argument('amount', type=float)
def make_withdrawal(acc_number,amount):
    account = session.query(Account).filter_by(number=acc_number).first()
    if account:
        if amount > 0 and  amount < account.amount:
            account.amount -= amount
            session.commit()
            click.echo(f"Successful Withdrawal of {amount} Kshs from account No: {acc_number}. New Account Balance is: {account.amount} Kshs.")
        else:
            click.echo("Withdrawal cannot be less than 0 or more than the remaining balance!")
    else:
        click.echo("Invalid Account!!")

cli.add_command(create_customer)
cli.add_command(open_account)
cli.add_command(make_deposit)
cli.add_command(make_withdrawal)

if __name__ == '__main__':
    cli()
