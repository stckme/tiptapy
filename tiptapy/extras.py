import re
from . import BaseNode, Image, register_renderer, e


class FeaturedImage(Image):
    type = "featuredimage"
    css_class = "featured-image"


class StackAudio(BaseNode):
    type = "audio"
    wrap_tag = "figure"

    def is_renderable(self, node):
        attrs = node.get("attrs", {})
        return bool(attrs.get("src", ""))

    def inner_render(self, node):
        attrs = node["attrs"]
        src = attrs.get('src', '').strip()
        caption = attrs.get('caption', '').strip()
        audio_link = f'<audio src={src}></audio>'
        with open('tiptapy/templates/stack-audio-player.html', 'r') as f:
            data = f.read()
        # Removing whitespaces between html tags.
        audio_player_block = re.sub(r'\s\s+', '', data)
        html = f'<div>{audio_link}{audio_player_block}</div>'
        if caption:
            html = html + f'<figcaption>{e(caption)}</figcaption>'
        return html


register_renderer(FeaturedImage)
register_renderer(StackAudio)
