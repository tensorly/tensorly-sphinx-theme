from os import path

__version__ = '0.2.0'

def setup(app):
    app.add_html_theme("tensorly_sphinx_theme", path.abspath(path.dirname(__file__)))
