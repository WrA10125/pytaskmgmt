import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from database import mongo
from routes.task_routes import task_bp

app = Flask(__name__)


CORS(app, origins=["https://angtaskmgmt.vercel.app", "http://localhost:4200","*"], methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])

@app.before_request
def handle_preflight():
    """Global handling of pre-flight OPTIONS requests"""
    if request.method == 'OPTIONS':
        response = jsonify({'message': 'CORS Pre-flight request'})
        response.headers.add('Access-Control-Allow-Origin', 'https://angtaskmgmt.vercel.app')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        return response


app.config["MONGO_URI"] = "mongodb+srv://ajaygore:Ajaygore%404046@aava.gb3aw.mongodb.net/techstack?retryWrites=true&w=majority"
mongo.init_app(app)


app.register_blueprint(task_bp, url_prefix="/api/tasks")


port = int(os.environ.get('PORT', 10000)) 
app.run(host='0.0.0.0', port=port, debug=False)  
