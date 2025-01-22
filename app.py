from flask import Flask, jsonify, request
from flask_cors import CORS
from database import mongo
from routes.task_routes import task_bp

app = Flask(__name__)
CORS(app, origins=["https://angtaskmgmt.vercel.app"], methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
@app.route('/api/tasks', methods=['OPTIONS'])
def handle_options():
    response = jsonify({'message': 'CORS Pre-flight request'})
   
    response.headers.add('Access-Control-Allow-Origin', 'https://angtaskmgmt.vercel.app')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    return response

app.config["MONGO_URI"] = "mongodb+srv://ajaygore:Ajaygore%404046@aava.gb3aw.mongodb.net/techstack?retryWrites=true&w=majority"
mongo.init_app(app)

app.register_blueprint(task_bp, url_prefix="/api/tasks")

if __name__ == "__main__":
   app.run(host="0.0.0.0",port=5000,debug=True)
