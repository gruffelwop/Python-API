"""add foreign key to posts table

Revision ID: a01f6ce53bef
Revises: 260da4d80946
Create Date: 2023-08-04 18:21:44.479860

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a01f6ce53bef'
down_revision = '260da4d80946'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("posts_users_fk", source_table="posts", referent_table="users", local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint("posts_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
