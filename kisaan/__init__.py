from flask import Flask

from .routes import main
from .store import store


def create_app() -> Flask:
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static",
        static_url_path="/static",
    )
    app.config["SECRET_KEY"] = "dev"
    store.initialize()
    app.register_blueprint(main)
    return app
