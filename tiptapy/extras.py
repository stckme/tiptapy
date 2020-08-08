from . import BaseContainer, Image, register_renderer


class FeaturedImage(Image):
    type = "featuredimage"
    css_class = "featured-image"


class Lock(BaseContainer):
    type = "lock"


register_renderer(FeaturedImage)
register_renderer(Lock)
