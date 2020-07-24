from . import Image, register_renderer


class FeaturedImage(Image):
    type = "featuredimage"
    css_class = "featured-image"


register_renderer(FeaturedImage)
