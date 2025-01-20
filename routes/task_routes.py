from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from datetime import datetime  

from database import mongo 
from models import task_serializer 

task_bp = Blueprint("task_routes", __name__)

@task_bp.route("/", methods=["POST"])
def create_task():
    data = request.json
    task = {
        "entity_name": data["entity_name"],
        "task_type": data["task_type"],
        "time": data["time"],
        "contact_person": data["contact_person"],
        "note": data.get("note", ""),
        "status": "open",
        "created_at": data.get("created_at", str(datetime.utcnow()))
    }
    result = mongo.db.tasks.insert_one(task)  
    return jsonify({"message": "Task created", "task_id": str(result.inserted_id)}), 201


@task_bp.route("/", methods=["GET"])
def get_tasks():
    tasks = mongo.db.tasks.find({})
    task_list = [
        {**task, "_id": str(task["_id"])} for task in tasks
    ]  
    return jsonify(task_list), 200


@task_bp.route("/<task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.json
    mongo.db.tasks.update_one({"_id": ObjectId(task_id)}, {"$set": data})  # 
    return jsonify({"message": "Task updated"})


@task_bp.route("/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    mongo.db.tasks.delete_one({"_id": ObjectId(task_id)})  
    return jsonify({"message": "Task deleted"})
