"""add cf user

Revision ID: 3f657ead958d
Revises: 26c438e9c293
Create Date: 2021-08-12 17:01:39.443588

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f657ead958d'
down_revision = '26c438e9c293'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('codeforces_userinfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('handle', sa.String(length=64), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('maxRating', sa.Integer(), nullable=True),
    sa.Column('titlePhoto', sa.String(length=512), nullable=True),
    sa.Column('avatar', sa.String(length=512), nullable=True),
    sa.Column('password', sa.String(length=256), nullable=True),
    sa.Column('api_key', sa.String(length=64), nullable=True),
    sa.Column('secret', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_codeforces_userinfo_handle'), 'codeforces_userinfo', ['handle'], unique=True)
    op.create_index(op.f('ix_codeforces_userinfo_id'), 'codeforces_userinfo', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_codeforces_userinfo_id'), table_name='codeforces_userinfo')
    op.drop_index(op.f('ix_codeforces_userinfo_handle'), table_name='codeforces_userinfo')
    op.drop_table('codeforces_userinfo')
    # ### end Alembic commands ###
