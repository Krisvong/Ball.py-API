"""empty message

Revision ID: 66066cfa3a9c
Revises: 
Create Date: 2023-06-12 12:59:28.226399

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66066cfa3a9c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reptiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('common_name', sa.String(length=250), nullable=True),
    sa.Column('scientific_name', sa.String(length=250), nullable=True),
    sa.Column('fun_fact', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reptiles')
    # ### end Alembic commands ###