from . import BaseNode, register_renderer


class FeaturedImage(BaseNode):
    type = "featuredimage"

    def is_renderable(self, node):
        attrs = node.get("attrs", {})
        return bool(attrs.get('src', '').strip())

    def inner_render(self, node) -> str:
        special_attrs_map = {'caption': 'figcaption'}
        attrs = node.get("attrs", {})
        attrs_s = " ".join(f'{k}="{v}"'
                           for k, v in attrs.items()
                           if k not in special_attrs_map and v.strip()
                           )
        html = f"<img {attrs_s}>"
        caption = attrs.get('caption', '').strip()
        if caption:
            tag = special_attrs_map['caption']
            html += f"<{tag}>{caption}</{tag}>"
        return f'<figure class="featured-image">{html}</figure>'


register_renderer(FeaturedImage)
