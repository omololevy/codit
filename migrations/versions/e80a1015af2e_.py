"""empty message

Revision ID: e80a1015af2e
Revises: 1c017d1db85d
Create Date: 2021-11-17 15:38:50.407122

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e80a1015af2e'
down_revision = '1c017d1db85d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('language', sa.String(), nullable=True))
    op.drop_column('posts', 'cohort')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('cohort', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('posts', 'language')
    # ### end Alembic commands ###
