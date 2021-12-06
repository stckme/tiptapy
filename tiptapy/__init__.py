import json
from inspect import isclass
from jinja2 import FileSystemLoader, Environment, select_autoescape
from typing import Dict
from urllib.parse import urlparse


__version__ = '0.12.0'

renderers: Dict = {}


def init_env(path='tiptapy/templates/'):
    return Environment(loader=FileSystemLoader(path),
                       autoescape=select_autoescape(
                           enabled_extensions=('jinja2'))
                       )


class BaseDoc:

    node_type = 'doc'
    templates_path = 'base-templates-dir'

    def __init__(self):
        templates = init_env()
        self.t = templates.get_template(f'{self.node_type}.html')


    def render(self, in_data):
        node = in_data if isinstance(in_data, dict) else json.loads(in_data)
        return self.t.render(node=node)


class config:
    """
    Config class to store constans which are used by the othe nodes.
    """
    DOMAIN = "python.org"



def register_renderer(cls):
    renderers[cls.node_type] = cls()


for o in tuple(locals().values()):
    if isclass(o) and issubclass(o, BaseDoc):
        register_renderer(o)


def convert_any(in_data):
    typ = in_data.get("type")
    renderer = renderers.get(typ)
    return renderer.render(in_data)


def is_trusted_link(url):
    """
    Check if the domain is the same as in the config.
    """
    link = urlparse(url)
    # Getting the domain of the link
    link = link.netloc
    return link.endswith(config.DOMAIN)


def to_html(s):
    in_data = s if isinstance(s, dict) else json.loads(s)
    return convert_any(in_data)
