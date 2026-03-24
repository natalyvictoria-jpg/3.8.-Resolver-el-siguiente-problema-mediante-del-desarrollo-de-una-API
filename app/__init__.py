from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flasgger import Swagger
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    db.init_app(app)
    CORS(app)

    swagger_config = {
        "headers": [],
        "specs": [{"endpoint": "apispec", "route": "/apispec.json"}],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/docs/"
    }
    swagger_template = {
        "info": {
            "title": "API Tareas - ITIC",
            "version": "1.0.0",
            "description": "API REST para administrar tareas personales"
        }
    }
    Swagger(app, config=swagger_config, template=swagger_template)

    from .routes import tareas_bp
    app.register_blueprint(tareas_bp)

    @app.route("/")
    def index():
        return redirect("/docs/")

    return app