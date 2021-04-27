from flask import Blueprint, jsonify, request

from models import db
from models.Address import Address

address_blueprint = Blueprint("adress", __name__)

@address_blueprint.route("", methods = ["POST"])
def create_user():
    body = request.json

    try:
        newAddress = Address()
        newAddress.line1 = body["line1"]
        newAddress.zipcode = body["zipcode"]
        newAddress.city = body["city"]

        if("line2" in body):
            newAddress.line2 = body["line2"]

        if("line3" in body):
            newAddress.line3 = body["line3"]

    
        db.session.add(newAddress)
        db.session.commit()
    
        return jsonify( newAddress.toJson() )
    except:
        return jsonify({"error": "BAD_REQUEST", "message": "incomplete request"}), 400


@address_blueprint.route("", methods = ["GET"])
def all_users():
    resp = Address.query.all()

    for i in range( len(resp) ):
        resp[i] = resp[i].toJson()
    
    return jsonify(resp)

@address_blueprint.route("/<userId>", methods = ["GET"])
def get_user_by_id(userId):
    resp = Address.query.get(userId)

    if(resp == None):
        return jsonify({"error": "NOT_FOUND", "message": "No entity found"}), 404
    else:
        return jsonify( resp.toJson() )

@address_blueprint.route("", methods = ["PUT"])
def update_user():
    body = request.json

    if("id" not in body):
        return jsonify({"error": "BAD_REQUEST", "message": "no id in request"}), 400
    
    updating = Address.query.get(body["id"])

    if("line1" in body):
        updating.line1 = body["line1"]

    if("line2" in body):
        updating.line2 = body["line2"]

    if("line3" in body):
        updating.line3 = body["line3"]

    if("zipcode" in body):
        updating.zipcode = body["zipcode"]

    if("city" in body):
        updating.city = body["city"]

    try:
        db.session.commit()
    except:
        return jsonify({"error": "TEAPOT", "message": "wha happun?"}), 418
    
    return jsonify( updating.toJson() )

@address_blueprint.route("/<userId>", methods = ["DELETE"])
def del_user(userId):
    addr = Address.query.get(userId)

    if( addr == None ):
        return jsonify({"error": "NOT_FOUND", "message": "No entity found"}), 404
    else:
        db.session.delete(addr)
        db.session.commit()
        return jsonify({"status": "ACCEPTED", "message": "Entity deleted"}), 202