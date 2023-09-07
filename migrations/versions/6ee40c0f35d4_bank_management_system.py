"""Bank_management_system

Revision ID: 6ee40c0f35d4
Revises: be654132376c
Create Date: 2023-09-07 20:42:19.124760

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ee40c0f35d4'
down_revision = 'be654132376c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
     op.create_table('customers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
     op.create_table('banks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('location', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
     op.create_table('accounts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('bank_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['bank_id'], ['banks.id'], ),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
     op.drop_table('banks')
     op.drop_table('customers')
     op.drop_table('accounts')
    # ### end Alembic commands ###
