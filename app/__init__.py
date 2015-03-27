# coding=utf-8
from flask import Flask


def _create_app():
    from app.cube_summation.views import cube_views

    web_app = Flask(__name__)
    web_app.register_blueprint(cube_views)
    return web_app

app = _create_app()