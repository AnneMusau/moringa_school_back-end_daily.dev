"""Added an activated attribute to the User model.

Revision ID: bcd43f24184f
Revises: 65891fe623dd
Create Date: 2024-11-13 18:09:59.566660

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bcd43f24184f'
down_revision = '65891fe623dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.alter_column('approved',
               existing_type=sa.BOOLEAN(),
               nullable=False)
        batch_op.alter_column('flagged',
               existing_type=sa.BOOLEAN(),
               nullable=False)

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('activated', sa.Boolean(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('activated')

    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.alter_column('flagged',
               existing_type=sa.BOOLEAN(),
               nullable=True)
        batch_op.alter_column('approved',
               existing_type=sa.BOOLEAN(),
               nullable=True)

    # ### end Alembic commands ###
