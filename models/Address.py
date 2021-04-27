from models import db

class Address(db.Model):
    __tablename__ = "addresses"
    id = db.Column(db.Integer, primary_key = True)
    line1 = db.Column(db.String(500), nullable=False)
    line2 = db.Column(db.String(500), nullable=True)
    line3 = db.Column(db.String(500), nullable=True)
    zipcode = db.Column(db.String(5), nullable=False)
    city = db.Column(db.String(200), nullable=False)

    users = db.relationship("User", backref="addresses", lazy=True)

    def __repr__(self):
        return "<Address {}>".format(self.id)
    
    def toJson(self):
        result =  {
            "id": self.id,
            "line1": self.line1,
            "line2": self.line2,
            "line3": self.line3,
            "zipcode": self.zipcode,
            "city": self.city,
            "users": []
        }

        for user in self.users:
            jsonUser = user.toJson()
            jsonUser.pop("address", None)
            result["users"].append(jsonUser)
        
        return result