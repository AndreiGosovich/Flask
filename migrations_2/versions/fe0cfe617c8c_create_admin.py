"""Create Admin

Revision ID: fe0cfe617c8c
Revises: 9597c1d6438f
Create Date: 2023-03-01 21:17:28.065211

"""
from alembic import op
from sqlalchemy.sql import table, column
from sqlalchemy import String, Boolean
from werkzeug.security import generate_password_hash

# revision identifiers, used by Alembic.
revision = 'fe0cfe617c8c'
down_revision = '9597c1d6438f'
branch_labels = None
depends_on = None


def upgrade():
    users_table = table('users',
                        column('username', String),
                        column('email', String),
                        column('password', String),
                        column('is_staff', Boolean),
                        column('full_name', String),
                        column('address', String),
                        )

    op.bulk_insert(users_table, [
        {
            'username': 'admin1',
            'email': 'admin1@one.tu',
            'password': generate_password_hash('admin1'),
            'is_staff': True,
            'full_name': 'admin1',
            'address': 'no address',
        }
    ])


def downgrade():
    from blog.models import User
    from blog.models.database import db
    user = User.query.filter_by(username='admin1').one_or_none()
    db.session.delete(user)
    db.session.commit()
