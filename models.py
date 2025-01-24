# from datetime import datetime
# def task_serializer(task):
#     return {
#         "_id": str(task["_id"]),
#         "entity_name": task["entity_name"],
#         "task_type": task["task_type"],
#         "time": task["time"],
#         "contact_person": task["contact_person"],
#         "note": task.get("note", ""),
#         "status": task["status"],
#         "created_at": task["created_at"]
#     }

from datetime import datetime
from bson import ObjectId

def task_serializer(task):

    return {
        "_id": str(task["_id"]),  
        "entity_name": task["entity_name"],
        "task_type": task["task_type"],
        "time": task["time"],
        "contact_person": task["contact_person"],
        "note": task.get("note", ""), 
        "status": task["status"],
        "created_at": task["created_at"].isoformat() if isinstance(task["created_at"], datetime) else task["created_at"]
    }

def task_deserializer(data):
  
    return {
        "entity_name": data["entity_name"],
        "task_type": data["task_type"],
        "time": data["time"],
        "contact_person": data["contact_person"],
        "note": data.get("note", ""),
        "status": data.get("status", "open"),
        "created_at": datetime.utcnow()  
    }


