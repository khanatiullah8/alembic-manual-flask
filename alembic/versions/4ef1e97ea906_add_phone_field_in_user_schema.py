"""add phone field in user schema

Revision ID: 4ef1e97ea906
Revises: 2dd6124864d1
Create Date: 2025-05-06 11:43:38.219683

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4ef1e97ea906'
down_revision: Union[str, None] = '2dd6124864d1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "user",
        sa.Column("phone", sa.String(10), nullable=False, unique=True)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("user","phone")
