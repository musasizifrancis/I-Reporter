from flask import request, Response, json, jsonify
from api.models.ireportermodels import User, users, Incident, incidents
import uuid

def addUser():
    request_data = request.get_json()
    user = User()
    user.firstName = request_data["firstName"]
    user.LastName = request_data["lastName"]
    user.otherNames = request_data["otherNames"]
    user.email = request_data["email"]
    user.password = request_data["password"]
    user.registered = request_data["registered"]

    usersData = {
        "userId": len(users)+1,
        "firstName": user.firstName,
        "lastName": user.lastName,
        "otherNames": user.otherNames,
        "email": user.email,
        "password": user.password,
        "registered": user.registered,
        "public_userId": str(uuid.uuid4())
        }
    users.append(usersData)
    return jsonify({
                    "data":users,
                    "status":201,
                    "id":usersData['userId'],
                    "message":"user created successully"
                    })

def addIncident():
    request_data = request.get_json()
    inc = Incident()
    inc.createdOn = request_data["createdOn"]
    inc.createdBy = request_data["createdBy"]
    inc.incidentType = request_data["incidentType"]
    inc.location = request_data["location"]
    inc.images = request_data["images"]

    incidentData = {
        "incidentId": len(incidents) + 1,
        "cretedOn": inc.createdOn,
        "createdBy": inc.createdBy,
        "incidentType": inc.incidentType,
        "location": inc.location,
        "image": inc.images.split(",")

    }

    incidents.append(incidentData)
    return jsonify({
                    "data":incidents,
                    "status":201,
                    "id":incidentData['incidentId'],
                    "message":"Incident created successully"
                    })

def getAllIncidents():
    return jsonify({
                    "status":201,
                    "data":incidents
                    })

def searchId(search_item, list_of_Items):
    search_list = []
    for item in list_of_Items:
        [search_list.append(item) for key in item if item[key] == search_item]
    return jsonify({
                    "status":201,
                    "data":search_list
                    })

def deleteId(search_item, list_of_Items):
    for item in list_of_Items:
        [list_of_Items.remove(item) for key in item if item[key] == search_item]
    return jsonify({
                    "status":200,
                    "id": search_item,
                    "data":incidents,
                    "message":"red-flag record deleted successfully"
                    })