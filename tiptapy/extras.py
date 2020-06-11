from . import BaseNode, register_renderer


class FeaturedImage(BaseNode):
    type = "featuredimage"

    def inner_render(self, node) -> str:
        special_attrs_map = {'caption': 'figcaption'}
        attrs = node.get("attrs", {})
        attrs_s = " ".join(f'{k}="{v}"'
                           for k, v in attrs.items()
                           if k not in special_attrs_map and v.strip()
                           )
        image = f"<picture><img {attrs_s}></picture>"
        caption = attrs.get('caption', '').strip()
        if caption:
            tag = special_attrs_map['caption']
            image += f"<{tag}>{attrs['caption']}</{tag}>"
        rendered_html = " "
        if attrs_s:
            rendered_html = f'<figure class="featured-image">{image}</figure>'
        return rendered_html


register_renderer(FeaturedImage)
