"""Customer_bank_association

Revision ID: 1d51842e0f3c
Revises: 6ee40c0f35d4
Create Date: 2023-09-07 20:44:58.120164

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d51842e0f3c'
down_revision = '6ee40c0f35d4'
branch_labels = None
depends_on = None



def upgrade():
     op.create_table('customer_bank_association',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('bank_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['bank_id'], ['banks.id'], ),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    pass
