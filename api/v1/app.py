#!/usr/bin/python3
"""Flask web application and the blueprint app_vews"""

from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS


app = Flask(__name__)

app.register_blueprint(app_views)

cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown_context(exception):
    """Calls storage.close() at the end of the request"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Handler for 404 errors"""
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    HOST = getenv("HBNB_API_HOST", '0.0.0.0')
    PORT = int(getenv("HBNB_API_PORT", '5000'))
    app.run(host=HOST, port=PORT, threaded=True, debug=True)
