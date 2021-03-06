"""empty message

Revision ID: 7926bc314355
Revises: 872dc9a139d3
Create Date: 2020-06-27 22:00:47.316815

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7926bc314355'
down_revision = '872dc9a139d3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('List_order')
    op.drop_constraint('Eat_list_or_fkey', 'Eat', type_='foreignkey')
    op.drop_column('Eat', 'list_or')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Eat', sa.Column('list_or', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('Eat_list_or_fkey', 'Eat', 'List_order', ['list_or'], ['id'])
    op.create_table('List_order',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"List_order_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], name='List_order_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='List_order_pkey')
    )
    # ### end Alembic commands ###
