"""Add Content Column to Posts Table

Revision ID: 7b88059c4efc
Revises: b7b445075de0
Create Date: 2023-07-30 08:51:57.029614

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b88059c4efc'
down_revision = 'b7b445075de0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False, primary_key=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
