# Image file type and it's MIME type mappings that are suported by tiptapy.
# Detailed documentation can be found about Image file type and format guide.
# Link: https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Image_types
from os.path import splitext

class SupportedFormatsMapper(dict):

    def __missing__(self, ext):
        return 'image'


SUPPORTED_FORMATS_MAP = SupportedFormatsMapper(
    PNG='image/png',
    JPG='image/jpeg',
    JPEG='image/jpeg',
    GIF='image/gif',
    BMP='image/bmp',
    WEBP='image/webp',
    SVG='image/svg+xml'
)


def url2mime(url):
    ext = splitext(url)[-1]
    ext = (ext[1:] if ext.startswith('.') else ext).upper()
    return SUPPORTED_FORMATS_MAP[ext]
