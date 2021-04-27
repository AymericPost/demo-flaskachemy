from models import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(200), unique = True, nullable = False)
    address_id = db.Column(db.Integer, db.ForeignKey("addresses.id"))

    address = db.relationship("Address")

    def __repr__(self):
        return "<User {}>".format(self.email)

    def toJson(self):
        userAddress = None

        if(not self.address == None):
            userAddress = self.address
            del userAddress.users
            userAddress = userAddress.toJson()

        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "address": userAddress
        }
