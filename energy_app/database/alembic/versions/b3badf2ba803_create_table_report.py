"""Create table report

Revision ID: b3badf2ba803
Revises: 133eb81a53a2
Create Date: 2023-07-19 15:17:26.101368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3badf2ba803'
down_revision = '133eb81a53a2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('report',
    sa.Column('country_code', sa.String(length=4), nullable=False),
    sa.Column('table_entsoe', sa.String(), nullable=False),
    sa.Column('day', sa.Date(), nullable=False),
    sa.Column('max_created_at', sa.DateTime(), nullable=False),
    sa.Column('row_count', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['country_code'], ['country.code'], ),
    sa.UniqueConstraint('country_code', 'table_entsoe', 'day')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('report')
    # ### end Alembic commands ###
