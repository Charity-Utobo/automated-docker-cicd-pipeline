from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return jsonify({
            "application": "Flask CI/CD API",
            "message": "Welcome to my automated deployment project!",
            "status": "running"
        }), 200

    @app.route("/health")
    def health():
        return jsonify({
            "status": "healthy"
        }), 200

    return app