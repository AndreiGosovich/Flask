"""Create Authors

Revision ID: 5df6f74a27be
Revises: dfef82a66bfd
Create Date: 2023-03-08 17:05:20.702697

"""
from alembic import op
from sqlalchemy import Integer
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = '5df6f74a27be'
down_revision = 'dfef82a66bfd'
branch_labels = None
depends_on = None


def upgrade():
    authors_table = table('author',
                          column('id', Integer),
                          column('user_id', Integer),
                          )

    op.bulk_insert(authors_table, [
        {
            'user_id': '8',
            'id': '8',
        },
        {
            'user_id': '9',
            'id': '9',
        },
        {
            'user_id': '10',
            'id': '10',
        }
    ])


def downgrade():
    from blog.models import Author
    from blog.models.database import db
    for _id in [8, 9, 10]:
        author = Author.query.filter_by(id=_id).one_or_none()
        db.session.delete(author)
    db.session.commit()
