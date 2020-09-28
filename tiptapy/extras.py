import pkg_resources
from . import BaseNode, Image, register_renderer, e


class FeaturedImage(Image):
    type = "featuredimage"
    css_class = "featured-image"


class StackAudio(BaseNode):
    type = "audio"

    def is_renderable(self, node):
        attrs = node.get("attrs", {})
        return bool(attrs.get("src", ""))

    def inner_render(self, node):
        attrs = node["attrs"]
        src = attrs.get('src', '').strip()
        caption = attrs.get('caption', '').strip()
        audio_src_block = f'<audio src={src}></audio>'
        audio_player_block = pkg_resources.resource_stream(
            __name__, 'templates/stack-audio-player.html'
        ).read().decode()
        html = f'<div>{audio_src_block}{audio_player_block}</div>'
        if caption:
            html = html + f'<figcaption>{e(caption)}</figcaption>'
        return f'<figure class="audio-player-container">{html}</figure>'


register_renderer(FeaturedImage)
register_renderer(StackAudio)
