"""empty message

Revision ID: 44af135eb41b
Revises: 9f78f55cf7f3
Create Date: 2018-07-25 15:35:42.573268

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '44af135eb41b'
down_revision = '9f78f55cf7f3'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('User', sa.Column('last_login_date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('User', 'last_login_date')
    # ### end Alembic commands ###