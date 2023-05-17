"""Add option_id column to questions table

Revision ID: 99a2b9ce523e
Revises: b1e37fef5c25
Create Date: 2023-04-11 23:41:22.363726

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99a2b9ce523e'
down_revision = 'b1e37fef5c25'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chats', sa.Column('option_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'chats', 'options', ['option_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'chats', type_='foreignkey')
    op.drop_column('chats', 'option_id')
    # ### end Alembic commands ###
