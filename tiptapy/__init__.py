import json
from html import escape as e
from inspect import isclass
from jinja2 import FileSystemLoader, Environment, select_autoescape
from typing import Dict
from urllib.parse import urlparse
from .image import url2mime


__version__ = '0.12.0'

renderers: Dict = {}


def make_img_src(attrs):
    alt = attrs.get('alt', '').strip()
    height = attrs.get('height', '')
    width = attrs.get('width', '')
    fallback_url = attrs['src']['fallback']
    image_src = f'img src="{fallback_url}"'
    if alt:
        image_src += f' alt="{e(alt)}"'
    if height and width:
        image_src += f'width="{width}" height="{height}"'

    return image_src


def handle_links(attrs):
    retval = None
    if attrs:
        url = attrs.get("href") or ""
        if not is_trusted_link(url):
           attrs["target"] = "_blank"
           attrs["rel"] = "noopener nofollow"
        retval = " ".join(
            f'{k}="{e(v)}"' for k, v in attrs.items()
        )

    return retval



def init_env(path='tiptapy/templates/'):
    env = Environment(loader=FileSystemLoader(path),
                       autoescape=select_autoescape(
                           enabled_extensions=('jinja2'))
                       )
    # https://stackoverflow.com/a/6038550
    env.globals['url2mime'] = url2mime
    env.globals['make_img_src'] = make_img_src
    env.globals['handle_links'] = handle_links

    return env



class BaseDoc:

    node_type = 'doc'
    templates_path = 'base-templates-dir'

    def __init__(self):
        templates = init_env()
        self.t = templates.get_template(f'{self.node_type}.html')


    def render(self, in_data):
        node = in_data if isinstance(in_data, dict) else json.loads(in_data)
        return self.t.render(node=node)


class Image(BaseDoc):

    node_type = 'image'

    # Discussed with Pradhvan and decided to keep it here in python
    def is_renderable(self, node):
        attrs = node.get("attrs", {})
        src = attrs.get("src", "")
        return src and bool(
            src.get('image', '').strip() or src.get('fallback', '').strip()
        )


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
