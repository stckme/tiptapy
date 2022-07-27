import os
import sys
import json
from html import escape
from jinja2 import FileSystemLoader, Environment, select_autoescape
from typing import Dict
from .image import url2mime
from .macros import (make_img_src, build_link_handler,
                     get_audio_player_block, get_doc_block)


__version__ = '0.15.0'

renderers: Dict = {}


def init_env(path, config):
    env = Environment(loader=FileSystemLoader(path),
                      autoescape=select_autoescape(
                          enabled_extensions=('html')))
    # https://stackoverflow.com/a/6038550
    env.globals['url2mime'] = url2mime
    env.globals['make_img_src'] = make_img_src
    env.globals['handle_links'] = build_link_handler(config)
    # Cause jinja2 `e` filter is not exactly same as html.escape
    env.globals['escape'] = escape
    env.globals['get_audio_player_block'] = get_audio_player_block
    env.globals['get_doc_block'] = get_doc_block

    return env


def _get_abs_template_path(path_str):
    # This is equivalent of pkgutil.get_data
    # But when diris passed to pkgutil.get_data it throws IsDirectoryError
    # Hence this function
    # Ref: https://github.com/python/cpython/blob/3.10/Lib/pkgutil.py#L614
    pkg_dir = os.path.dirname(sys.modules[__name__].__file__)
    return os.path.join(pkg_dir, path_str)


class BaseDoc:

    doc_type = 'doc'
    templates_path = (_get_abs_template_path('templates'),
                      _get_abs_template_path('templates/extras'))
    locked = False
    # `locked` helps in templates determine to show/hide in anonymous views
    # Useful in case where code is referring same template for both protected
    # and guest views

    def __init__(self, config):
        environ = init_env(self.templates_path, config)
        self.t = environ.get_template(f'{self.doc_type}.html')
        self.t.environment.globals['locked'] = self.locked

    def render(self, in_data):
        in_data = in_data if isinstance(in_data, dict) else json.loads(in_data)
        node = in_data if isinstance(in_data, dict) else json.loads(in_data)
        return self.t.render(node=node)
