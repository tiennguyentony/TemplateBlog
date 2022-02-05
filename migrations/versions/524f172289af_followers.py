"""followers

Revision ID: 524f172289af
Revises: 18fbacd48271
Create Date: 2022-02-04 23:05:07.186360

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '524f172289af'
down_revision = '18fbacd48271'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
