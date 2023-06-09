"""Add task column to occupations table

Revision ID: b1e37fef5c25
Revises: 009bcc43d7e6
Create Date: 2023-04-09 23:21:00.346978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1e37fef5c25'
down_revision = '009bcc43d7e6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('occupations', sa.Column('task', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('occupations', 'task')
    # ### end Alembic commands ###
