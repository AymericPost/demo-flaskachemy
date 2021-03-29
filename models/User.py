from models import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(200), unique = True, nullable = False)

    def toJson(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }
