"""empty message

Revision ID: 3707d4b229ff
Revises: 71c0b14b79e8
Create Date: 2021-11-21 06:22:56.602579

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3707d4b229ff'
down_revision = '71c0b14b79e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('vote', sa.Integer(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['comments.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('users', sa.Column('profile', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile')
    op.drop_table('votes')
    # ### end Alembic commands ###