"""add content table

Revision ID: e4971c53ffd0
Revises: befc8adf62a5
Create Date: 2024-09-27 17:24:00.245322

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e4971c53ffd0'
down_revision: Union[str, None] = 'befc8adf62a5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
