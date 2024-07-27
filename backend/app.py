# Main Backend for Application
from flask import Flask, request, jsonify

app = Flask(__name__)

# TODO: Connect to MongoDB database

# TODO: Endpoint to add a resource

# TODO: Function to validate resource URL using Google Safe Browsing API

# TODO: Endpoint to get all resources (for listing in the resource library)

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)