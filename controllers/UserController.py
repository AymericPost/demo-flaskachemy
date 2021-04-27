from flask import Blueprint, jsonify, request

from models import db
from models.User import User

user_blueprint = Blueprint("users", __name__)

@user_blueprint.route("", methods = ["POST"])
def create_user():
    body = request.json

    if("name" in body and "email" in body):
        newUser = User()
        newUser.name = body["name"]
        newUser.email = body["email"]

        if("address_id" in body):
            newUser.address_id = body["address_id"]

        try:
            db.session.add(newUser)
            db.session.commit()
        
            return jsonify( newUser.toJson() )
        except:
            return jsonify({"error": "BAD_REQUEST", "message": "email already exists"}), 400
    else:
        return jsonify({"error": "BAD_REQUEST", "message": "name and/or email missing"}), 400

@user_blueprint.route("", methods = ["GET"])
def all_users():
    resp = User.query.all()

    for i in range( len(resp) ):
        resp[i] = resp[i].toJson()
    
    return jsonify(resp)

@user_blueprint.route("/<userId>", methods = ["GET"])
def get_user_by_id(userId):
    resp = User.query.get(userId)

    if(resp == None):
        return jsonify({"error": "NOT_FOUND", "message": "No entity found"}), 404
    else:
        return jsonify( resp.toJson() )

@user_blueprint.route("/search", methods = ["GET"])
def get_user_by_name():
    term = request.args["q"]

    resp = User.query.filter_by(name = term).all()

    for i in range( len(resp) ):
        resp[i] = resp[i].toJson()
    
    return jsonify(resp)

@user_blueprint.route("", methods = ["PUT"])
def update_user():
    body = request.json

    if("id" not in body):
        return jsonify({"error": "BAD_REQUEST", "message": "no id in request"}), 400
    
    updating = User.query.get(body["id"])

    if("name" in body):
        updating.name = body["name"]

    if("email" in body):
        updating.email = body["email"]

    if("address_id" in body):
            newUser.address_id = body["address_id"]

    try:
        db.session.commit()
    except:
        return jsonify({"error": "BAD_REQUEST", "message": "email already exists"}), 400
    
    return jsonify( updating.toJson() )

@user_blueprint.route("/<userId>", methods = ["DELETE"])
def del_user(userId):
    usr = User.query.get(userId)

    if( usr == None ):
        return jsonify({"error": "NOT_FOUND", "message": "No entity found"}), 404
    else:
        db.session.delete(usr)
        db.session.commit()
        return jsonify({"status": "ACCEPTED", "message": "Entity deleted"}), 202