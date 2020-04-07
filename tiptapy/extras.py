from . import BaseNode, register_renderer


class FeatureImage(BaseNode):
    type = "featureimage"
    wrap_tag: str = "figure"

    def inner_render(self, node) -> str:
        special_attrs_map = {'caption': 'figcaption'}
        attrs = node.get("attrs", {})
        attrs_s = " ".join(f'{k}="{v}"'
                           for k, v in attrs.items()
                           if k not in special_attrs_map
                           )
        html = f"<picture><img {attrs_s}><picture>"
        for attr in special_attrs_map:
            if attr in attrs:
                tag = special_attrs_map[attr]
                html += f"<{tag}> {attrs[attr]} </{tag}>"
        return html


register_renderer(FeatureImage)
