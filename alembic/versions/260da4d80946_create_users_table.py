"""Create Users Table

Revision ID: 260da4d80946
Revises: 7b88059c4efc
Create Date: 2023-07-30 09:01:29.542994

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '260da4d80946'
down_revision = '7b88059c4efc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users",
                    sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("email", sa.String(), nullable=False),
                    sa.Column("password", sa.String(), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()"), nullable=False),
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("email")
                    )
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
