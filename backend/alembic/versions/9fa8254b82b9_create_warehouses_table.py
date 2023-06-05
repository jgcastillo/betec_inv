"""create warehouses table

Revision ID: 9fa8254b82b9
Revises: e07cabed29cb
Create Date: 2023-06-04 19:36:34.947146

"""
import uuid

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = '9fa8254b82b9'
down_revision = 'e07cabed29cb'
branch_labels = None
depends_on = None

def create_warehouses_table():
    op.create_table(
        'warehouses',
        sa.Column('id', sa.String(36), primary_key=True, default=str(uuid.uuid4())),
        sa.Column('name', sa.VARCHAR(length=50), nullable=False, unique=True),
        sa.Column('location', sa.VARCHAR(length=80), nullable= False),
        sa.Column('is_active', sa.Boolean),
        sa.Column('created_date', sa.DateTime)
    )

def upgrade() -> None:
    create_warehouses_table()


def downgrade() -> None:
    op.drop_table('warehouses')
