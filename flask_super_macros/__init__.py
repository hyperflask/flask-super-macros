from jinja_super_macros import configure_environment
import os
import click
from .storybook import storybook_bp


class SuperMacros:
    def __init__(self, app=None, **kwargs):
        if app:
            self.init_app(app, **kwargs)

    def init_app(self, app, macros_folder="macros", register_from_env=True):
        self.app = app
        configure_environment(app.jinja_env, register_from_env)
        app.macros = app.jinja_env.macros
        app.macro = app.macros.macro

        if macros_folder:
            app.macros.register_from_directory(os.path.join(app.root_path, macros_folder), filter_func=lambda f: not f.endswith(".macro.html"))
            app.macros.create_from_directory(os.path.join(app.root_path, macros_folder))

        if app.debug:
            app.register_blueprint(storybook_bp)

        @app.cli.command()
        @click.option("--watch", is_flag=True, help="Watch for changes")
        def create_macro_stories():
            pass

    def __getattr__(self, name):
        return getattr(self.app.macros, name)
