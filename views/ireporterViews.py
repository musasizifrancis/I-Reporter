from flask import Blueprint,request, jsonify
from api.controllers.ireportercontrollers import addUser, addIncident, getAllIncidents, searchId, incidents, deleteId, users 
import json

bp = Blueprint("ireporterViews", __name__, url_prefix="/api/v1")

@bp.route("/users", methods=["POST"])
def createUser():
    return addUser()

@bp.route("/red-flags", methods=["POST"])
def createIncident():
	data = request.get_json()
	
	user = {
	'userId': data.get('userId'),
	'firstName': data.get('firstName'),
	'lastName': data.get('lastName'),
	'otherNames': data.get('otherNames'),
	'userName': data.get('userName'),
	'email': data.get('email'),
	'password': data.get('password')}
	users.append(user)
	return jsonify(user), 200

@bp.route("/red-flags", methods=["GET"])
def get_all_red_flag_records():
    return getAllIncidents()

@bp.route("/red-flags/<int:red_flag_id>", methods=["GET"])
def get_specific_redflag(red_flag_id):
    return searchId(red_flag_id, incidents)

@bp.route("/red-flags/<int:red_flag_id>/location", methods=["PATCH"])
def edit_specific_redflag_location():
    pass

@bp.route("/red-flags/<int:red_flag_id>/comment", methods=["PATCH"])
def add_comment_to_specific_redflag_record():
    pass

@bp.route("/red-flags/<int:red_flag_id>", methods=["DELETE"])
def delete_specific_redflag_record(red_flag_id):
    return deleteId(red_flag_id, incidents)
