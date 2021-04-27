from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    app.app_context().push()
    db.init_app(app)

    from models import User, Address

    db.create_all()

    return app