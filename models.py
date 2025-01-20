from datetime import datetime

def task_serializer(task):
    return {
        "_id": str(task["_id"]),
        "entity_name": task["entity_name"],
        "task_type": task["task_type"],
        "time": task["time"],
        "contact_person": task["contact_person"],
        "note": task.get("note", ""),
        "status": task["status"],
        "created_at": task["created_at"]
    }
