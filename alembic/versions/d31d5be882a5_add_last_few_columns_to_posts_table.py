"""add last few columns to posts table

Revision ID: d31d5be882a5
Revises: a01f6ce53bef
Create Date: 2023-08-04 18:37:13.406914

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd31d5be882a5'
down_revision = 'a01f6ce53bef'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"))
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("NOW()")))
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
