from flask import Blueprint, current_app, request


storybook_bp = Blueprint("storybook", __name__, url_prefix="/storybook")


@storybook_bp.route("/<macro_name>")
def index(macro_name):
    return current_app.jinja_env.macros.render(macro_name, **request.args)