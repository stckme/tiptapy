import json
import os
import sys
from html import escape
from html.parser import HTMLParser
from typing import Dict

from jinja2 import Environment, FileSystemLoader, select_autoescape

from .image import url2mime
from .macros import (
    build_link_handler,
    get_audio_player_block,
    get_doc_block,
    make_img_src,
)

__version__ = "0.18.0"

renderers: Dict = {}


def init_env(path, config):
    env = Environment(
        loader=FileSystemLoader(path),
        autoescape=select_autoescape(enabled_extensions=("html")),
    )
    # https://stackoverflow.com/a/6038550
    env.globals["url2mime"] = url2mime
    env.globals["make_img_src"] = make_img_src
    env.globals["handle_links"] = build_link_handler(config)
    env.globals["get_audio_player_block"] = get_audio_player_block
    env.globals["get_doc_block"] = get_doc_block

    return env


def _get_abs_template_path(path_str):
    # This is equivalent of pkgutil.get_data
    # But when diris passed to pkgutil.get_data it throws IsDirectoryError
    # Hence this function
    # Ref: https://github.com/python/cpython/blob/3.10/Lib/pkgutil.py#L614
    pkg_dir = os.path.dirname(sys.modules[__name__].__file__)
    return os.path.join(pkg_dir, path_str)


class IFrameParser(HTMLParser):
    allowed_tag = "iframe"

    def __init__(self):
        super().__init__()
        self.iframe = ""

    def handle_starttag(self, tag, attrs):
        if tag != self.allowed_tag:
            return

        if self.iframe:
            # Ignore more than one iframe
            return

        _attrs = " ".join(
            [k if v is None else f'{escape(k)}="{escape(v)}"' for k, v in attrs]
        )
        self.iframe = f"<{tag} {_attrs}></{tag}>"


def escape_values_recursive(node):
    html_key = "html"  # key to look for html content
    if isinstance(node, dict):
        for k, v in node.items():
            esc_k = escape(k)
            if k != esc_k:
                node.pop(k)
            if esc_k == html_key:
                # Allow only iframe tag
                p = IFrameParser()
                p.feed(v)
                node[esc_k] = p.iframe
            else:
                node[esc_k] = escape_values_recursive(v)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            node[i] = escape_values_recursive(v)
    elif isinstance(node, str):
        return escape(node)
    return node


class BaseDoc:
    doc_type = "doc"
    templates_path = (
        _get_abs_template_path("templates"),
        _get_abs_template_path("templates/extras"),
    )
    locked = False
    # `locked` helps in templates determine to show/hide in anonymous views
    # Useful in case where code is referring same template for both protected
    # and guest views

    def __init__(self, config):
        environ = init_env(self.templates_path, config)
        self.t = environ.get_template(f"{self.doc_type}.html")
        self.t.environment.globals["locked"] = self.locked

    def render(self, in_data):
        in_data = in_data if isinstance(in_data, dict) else json.loads(in_data)
        node = in_data if isinstance(in_data, dict) else json.loads(in_data)
        node = escape_values_recursive(node)
        return self.t.render(node=node)
