from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.views import _views
    _views.init_app(app)

    return app
