from . import BaseNode, register_renderer, get_mime_type, e


class FeaturedImage(BaseNode):
    type = "featuredimage"

    def is_renderable(self, node):
        attrs = node.get("attrs", {})
        src = attrs.get("src", "")
        return src and bool(
            src.get('image', '').strip() and src.get('fallback', '').strip()
        )

    def inner_render(self, node) -> str:
        alt, caption = '', ''
        attrs = node.get("attrs", {})
        for k, v in attrs.items():
            if isinstance(v, (dict,)):
                urls = [url for image, url in v.items() if url.strip()]
            if 'alt' in k:
                alt = v.strip()
            if 'caption' in k:
                caption = v.strip()
        image_url, fallback_url = urls
        image_type, fallback_type = get_mime_type(image_url, fallback_url)
        image_src = f'<img src="{fallback_url}"/>'
        if alt:
            image_src = f'<img src="{fallback_url}" alt ={alt}/>'
        html = f'<picture><source srcset="{image_url}"type="{image_type}"/><source srcset="{fallback_url}" type="{fallback_type}"/>{image_src}</picture>'  # noqa: E501
        if caption:
            html = html + f'<figcaption>{e(caption)}</figcaption>'
        return f'<figure class="featured-image">{html}</figure>'


register_renderer(FeaturedImage)
