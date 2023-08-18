"""empty message

Revision ID: 53971aac9f4b
Revises: 
Create Date: 2023-04-05 01:57:23.997822

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53971aac9f4b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_file', sa.String(length=50), nullable=True))

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_file', sa.String(length=50), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('image_file')

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('image_file')

    # ### end Alembic commands ###