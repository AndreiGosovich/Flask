"""Create Admin

Revision ID: fe0cfe617c8c
Revises: c38eecdfe86b
Create Date: 2023-03-01 21:17:28.065211

"""
from alembic import op
from sqlalchemy.sql import table, column
from sqlalchemy import String, Boolean
# from werkzeug.security import generate_password_hash
from blog.security import flask_bcrypt

# revision identifiers, used by Alembic.
revision = 'fe0cfe617c8c'
# down_revision = '9597c1d6438f'
down_revision = 'c38eecdfe86b'
branch_labels = None
depends_on = None


def upgrade():
    users_table = table('users',
                        column('username', String),
                        column('email', String),
                        column('_password', String),
                        column('is_staff', Boolean),
                        column('first_name', String),
                        column('last_name', String),
                        column('address', String),
                        )

    op.bulk_insert(users_table, [
        {
            'username': 'admin1',
            'email': 'admin1@one.tu',
            '_password': flask_bcrypt.generate_password_hash('admin1'),
            'is_staff': True,
            'first_name': 'admin1',
            'last_name': 'admin1',
            'address': 'no address',
        }
    ])


def downgrade():
    from blog.models import User
    from blog.models.database import db
    user = User.query.filter_by(username='admin').one_or_none()
    db.session.delete(user)
    db.session.commit()
