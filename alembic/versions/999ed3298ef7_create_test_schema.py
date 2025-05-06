"""create test schema

Revision ID: 999ed3298ef7
Revises: 4ef1e97ea906
Create Date: 2025-05-06 12:07:28.979819

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '999ed3298ef7'
down_revision: Union[str, None] = '4ef1e97ea906'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "test",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(100), nullable=False)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("test")
