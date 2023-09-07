"""Adding bank_cusotomer_association

Revision ID: 56af52a00a4e
Revises: 54ca5f879e54
Create Date: 2023-09-07 16:37:26.979236

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56af52a00a4e'
down_revision = '54ca5f879e54'
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
