from . import Image, register_renderer, e


class FeaturedImage(Image):
    type = "featuredimage"
    css_class = "featured-image"


register_renderer(FeaturedImage)
