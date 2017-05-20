"""empty message

Revision ID: 21d7cebe03e5
Revises: ca4d20580c47
Create Date: 2017-05-20 18:32:49.648604

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '21d7cebe03e5'
down_revision = 'ca4d20580c47'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Engineers', 'full_name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('Photos', 'link',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('Reports', 'comment',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('Reports', 'end_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('Reports', 'gps_latitude',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=False)
    op.alter_column('Reports', 'gps_longitude',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=False)
    op.alter_column('Tasks', 'start_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('Tasks', 'task_description',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('Tasks', 'task_name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Tasks', 'task_name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('Tasks', 'task_description',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('Tasks', 'start_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('Reports', 'gps_longitude',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=True)
    op.alter_column('Reports', 'gps_latitude',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=True)
    op.alter_column('Reports', 'end_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('Reports', 'comment',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('Photos', 'link',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('Engineers', 'full_name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
