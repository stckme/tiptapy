import json
from html import escape
from inspect import isclass
from jinja2 import FileSystemLoader, Environment, select_autoescape
from typing import Dict
from .image import url2mime
from .macros import make_img_src, handle_links


__version__ = '0.12.0'

renderers: Dict = {}


def init_env(path):
    env = Environment(loader=FileSystemLoader(path),
                      autoescape=select_autoescape(enabled_extensions=('html')))
    # https://stackoverflow.com/a/6038550
    env.globals['url2mime'] = url2mime
    env.globals['make_img_src'] = make_img_src
    env.globals['handle_links'] = handle_links
    # Cause jinja2 `e` filter is not exactly same as html.escape
    env.globals['escape'] = escape

    return env


class BaseDoc:

    doc_type = 'doc'
    templates_path = ['tiptapy/templates/', 'tiptapy/templates/extras']

    def __init__(self):
        environ = init_env(self.templates_path)
        self.t = environ.get_template(f'{self.doc_type}.html')


    def render(self, in_data):
        node = in_data if isinstance(in_data, dict) else json.loads(in_data)
        return self.t.render(node=node)



def register_renderers(cls):
    renderer = BaseDoc()
    renderers[renderer.doc_type] = BaseDoc()


def to_html(s):
    in_data = s if isinstance(s, dict) else json.loads(s)
    typ = in_data.get("type")
    renderer = renderers.get(typ)
    return renderer.render(in_data)


register_renderers(BaseDoc)
