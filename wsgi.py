import os

from blog.app import create_app
# from blog.models.database import db
# from werkzeug.security import generate_password_hash

app = create_app()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True,
    )
