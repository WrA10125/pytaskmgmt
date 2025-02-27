from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from datetime import datetime
from database import mongo
from models import task_serializer, task_deserializer

task_bp = Blueprint("task_routes", __name__)

@task_bp.route("/", methods=["POST"])
def create_task():
    data = request.json

    task_data = task_deserializer(data)

    required_fields = ["entity_name", "task_type", "time", "contact_person"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    try:
     
        result = mongo.db.tasks.insert_one(task_data)
      
        return jsonify({"message": "Task created", "task_id": str(result.inserted_id)}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@task_bp.route("/", methods=["GET"])
def get_tasks():
    try:
        tasks = mongo.db.tasks.find({})
        task_list = [task_serializer(task) for task in tasks]
        return jsonify(task_list), 200
    except Exception as e:
        return jsonify({"error": f"Error fetching tasks: {str(e)}"}), 500


@task_bp.route("/<task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.json

  
    if not ObjectId.is_valid(task_id):
        return jsonify({"error": "Invalid task ID"}), 400

    updated_task_data = task_deserializer(data)

    try:
    
        result = mongo.db.tasks.update_one({"_id": ObjectId(task_id)}, {"$set": updated_task_data})
        if result.matched_count == 0:
            return jsonify({"error": "Task not found"}), 404
        return jsonify({"message": "Task updated"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@task_bp.route("/<task_id>", methods=["DELETE"])
def delete_task(task_id):

    if not ObjectId.is_valid(task_id):
        return jsonify({"error": "Invalid task ID"}), 400

    try:
      
        result = mongo.db.tasks.delete_one({"_id": ObjectId(task_id)})
        if result.deleted_count == 0:
            return jsonify({"error": "Task not found"}), 404
        return jsonify({"message": "Task deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

