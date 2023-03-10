"""empty message

Revision ID: 00ead9f307f6
Revises: 65ff197943f6
Create Date: 2023-02-22 11:10:08.800031

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00ead9f307f6'
down_revision = '65ff197943f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('language', sa.String(length=5), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('language')

    # ### end Alembic commands ###
