"""empty message

Revision ID: ca4d20580c47
Revises: 3a8976117c26
Create Date: 2017-05-20 16:40:32.663985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca4d20580c47'
down_revision = '3a8976117c26'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Tasks', sa.Column('photo_required', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Tasks', 'photo_required')
    # ### end Alembic commands ###
