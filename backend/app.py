# Main Backend for Application
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Load environment variables from .env
load_dotenv()

# Connect to MongoDB database
# make sure to create .env file with MONGO_URI variable (.gitignore ensures it won't be committed to github)
mongo_uri = os.getenv("MONGO_URI") 
client = MongoClient(mongo_uri)
db = client['resourceLibrary']  # accesses resourceLibrary database or creates it if it doesn't exist
collection = db['resources']  # accesses resources collection or creates it if it doesn't exist

# TODO: Endpoint to create/add a resource

# TODO: Function to validate resource URL using Google Safe Browsing API

# TODO: Endpoint to get all resources (for listing in the resource library)

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)