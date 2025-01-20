# from flask import Blueprint, request, jsonify
# from bson.objectid import ObjectId
# from database import mongo 
# from models import task_serializer

# task_bp = Blueprint("task_routes", __name__)

# # Create Task
# @task_bp.route("/", methods=["POST"])
# def create_task():
#     data = request.json
#     task = {
#         "entity_name": data["entity_name"],
#         "task_type": data["task_type"],
#         "time": data["time"],
#         "contact_person": data["contact_person"],
#         "note": data.get("note", ""),
#         "status": "open",
#         "created_at": data.get("created_at", str(datetime.utcnow()))
#     }
#     result = db.tasks.insert_one(task)
#     return jsonify({"message": "Task created", "task_id": str(result.inserted_id)}), 201

# # Get All Tasks
# @task_bp.route("/", methods=["GET"])
# def get_tasks():
#     tasks = list(mongo.db.tasks.find({}, {"_id": 0}))  # Fetch tasks from MongoDB
#     return jsonify(tasks), 200

# # Update Task
# @task_bp.route("/<task_id>", methods=["PUT"])
# def update_task(task_id):
#     data = request.json
#     db.tasks.update_one({"_id": ObjectId(task_id)}, {"$set": data})
#     return jsonify({"message": "Task updated"})

# # Delete Task
# @task_bp.route("/<task_id>", methods=["DELETE"])
# def delete_task(task_id):
#     db.tasks.delete_one({"_id": ObjectId(task_id)})
#     return jsonify({"message": "Task deleted"})

from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from datetime import datetime  # ✅ Added missing import

from database import mongo  # ✅ Use mongo, not db
from models import task_serializer # ✅ Assuming you have this model

task_bp = Blueprint("task_routes", __name__)

# Create Task
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
    result = mongo.db.tasks.insert_one(task)  # ✅ Fixed `db.tasks` -> `mongo.db.tasks`
    return jsonify({"message": "Task created", "task_id": str(result.inserted_id)}), 201

# Get All Tasks
@task_bp.route("/", methods=["GET"])
def get_tasks():
    tasks = mongo.db.tasks.find({})
    task_list = [
        {**task, "_id": str(task["_id"])} for task in tasks
    ]  # ✅ Convert `_id` to string
    return jsonify(task_list), 200

# Update Task
@task_bp.route("/<task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.json
    mongo.db.tasks.update_one({"_id": ObjectId(task_id)}, {"$set": data})  # ✅ Fixed `db.tasks`
    return jsonify({"message": "Task updated"})

# Delete Task
@task_bp.route("/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    mongo.db.tasks.delete_one({"_id": ObjectId(task_id)})  # ✅ Fixed `db.tasks`
    return jsonify({"message": "Task deleted"})
