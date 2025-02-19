"""Add description to Post model

Revision ID: ddaab94a98ee
Revises: ae98495a3bb0
Create Date: 2025-02-17 19:02:55.618731

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ddaab94a98ee'
down_revision = 'ae98495a3bb0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.String(length=255), nullable=True))
    op.drop_constraint('users_lastname_key', 'users', type_='unique')
    op.drop_constraint('users_name_key', 'users', type_='unique')
    op.create_unique_constraint(None, 'users', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.create_unique_constraint('users_name_key', 'users', ['name'])
    op.create_unique_constraint('users_lastname_key', 'users', ['lastname'])
    op.drop_column('users', 'username')
    # ### end Alembic commands ###
