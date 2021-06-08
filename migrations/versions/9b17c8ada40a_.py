"""empty message

Revision ID: 9b17c8ada40a
Revises: c52ef46485a0
Create Date: 2020-05-27 16:22:13.282308

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b17c8ada40a'
down_revision = 'c52ef46485a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('User', sa.Column('active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('User', 'active')
    # ### end Alembic commands ###
