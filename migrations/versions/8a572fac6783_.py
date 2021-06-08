"""empty message

Revision ID: 8a572fac6783
Revises: 6b4fa3463442
Create Date: 2020-07-09 21:49:35.549555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a572fac6783'
down_revision = '6b4fa3463442'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('User', sa.Column('code', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('User', 'code')
    # ### end Alembic commands ###
