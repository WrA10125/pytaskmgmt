
from flask import Flask, jsonify, request
from flask_cors import CORS
from database import mongo
from routes.task_routes import task_bp

app = Flask(__name__)

# CORS configuration with allowed origins and methods
CORS(app, origins=["http://localhost:4200"], methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])

# Explicit handling of OPTIONS requests (pre-flight)
@app.route('/api/tasks', methods=['OPTIONS'])
def handle_options():
    response = jsonify({'message': 'CORS Pre-flight request'})
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:4200')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    return response

# Configure MongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/techstack"
mongo.init_app(app)

# Register Blueprints
app.register_blueprint(task_bp, url_prefix="/api/tasks")

if __name__ == "__main__":
    app.run(debug=True)
