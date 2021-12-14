import pkgutil
from string import Template
from . import BaseDoc, Image, register_renderer, init_env


def get_audio_player_block():
    audio_player_block = pkgutil.get_data(
        __name__, 'templates/stack-audio-player.html').decode()
    return audio_player_block


class FeaturedImage(Image):
    node_type = "featuredimage"
    templates_path = 'tiptapy/templates/extras'


class StackAudio:
    node_type = "audio"
    templates_path = 'tiptapy/templates/extras'

    def __init__(self):
        environ = init_env(self.templates_path)
        environ.globals['get_audio_player_block'] = get_audio_player_block
        self.t = environ.get_template(f'{self.node_type}.html')
#
#
# class StackDocument(BaseNode):
#     type = "document"
#
#     def is_renderable(self, node):
#         attrs = node.get("attrs", {})
#         reqd_attrs = {'src', 'format', 'name', 'size'}
#         return set(attrs).issuperset(reqd_attrs)
#
#     def inner_render(self, node):
#         attrs = node["attrs"]
#         src = attrs.get('src', '').strip()
#         caption = attrs.get('caption', '').strip()
#         name = e(attrs.get('name', '').strip())
#         size = attrs.get('size', '').strip()
#         extension = attrs.get('format', '').strip()[:4]
#         document_block = pkgutil.get_data(
#             __name__, 'templates/stack-document.html'
#         ).decode()
#         document = Template(document_block)
#         html = document.substitute(fileformat=extension,
#                                    filename=name, filesize=size, filesrc=src)
#         if caption:
#             html = html + f'<figcaption>{e(caption)}</figcaption>'
#         return f'<figure class="file-attachment">{html}</figure>'


register_renderer(FeaturedImage)
register_renderer(StackAudio)
# register_renderer(StackDocument)
