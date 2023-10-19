"""add phone number

Revision ID: 0739176f7973
Revises: 7e8461ef67fc
Create Date: 2023-10-19 23:27:40.010756

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '0739176f7973'
down_revision: Union[str, None] = '7e8461ef67fc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_num', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    
    op.drop_column('users', 'phone_num')
   
    # ### end Alembic commands ###
