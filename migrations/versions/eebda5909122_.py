"""empty message

Revision ID: eebda5909122
Revises: 534a82bbfd38
Create Date: 2020-06-28 22:26:08.845164

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eebda5909122'
down_revision = '534a82bbfd38'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Orders', sa.Column('user', sa.PickleType(), nullable=True))
    op.drop_column('Orders', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Orders', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('Orders', 'user')
    # ### end Alembic commands ###