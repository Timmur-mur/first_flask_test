"""empty message

Revision ID: 6b4fa3463442
Revises: e209eeb3a8cb
Create Date: 2020-07-09 17:18:07.499787

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b4fa3463442'
down_revision = 'e209eeb3a8cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Eat', sa.Column('body', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Eat', 'body')
    # ### end Alembic commands ###
