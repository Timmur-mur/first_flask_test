"""empty message

Revision ID: e5f0ffb56b0c
Revises: 63e810b865d8
Create Date: 2020-06-23 21:32:02.210431

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5f0ffb56b0c'
down_revision = '63e810b865d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('basket_eat')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('basket_eat',
    sa.Column('basket_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('eat_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['basket_id'], ['Basket.id'], name='basket_eat_basket_id_fkey'),
    sa.ForeignKeyConstraint(['eat_id'], ['Eat.id'], name='basket_eat_eat_id_fkey')
    )
    # ### end Alembic commands ###
