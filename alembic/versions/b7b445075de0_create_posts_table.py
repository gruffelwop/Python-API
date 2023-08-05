"""Create Posts Table

Revision ID: b7b445075de0
Revises: 
Create Date: 2023-07-30 08:41:47.400694

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7b445075de0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts",
                    sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
                    sa.Column("title", sa.String(), nullable=False, primary_key=False),
                )
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
