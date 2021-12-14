from html import escape
from urllib.parse import urlparse


class config:
    """
    Config class to store constans which are used by the othe nodes.
    """
    DOMAIN = "python.org"


def is_trusted_link(url):
    """
    Check if the domain is the same as in the config.
    """
    link = urlparse(url)
    # Getting the domain of the link
    link = link.netloc
    return link.endswith(config.DOMAIN)


def make_img_src(attrs):
    alt = attrs.get('alt', '').strip()
    height = attrs.get('height', '')
    width = attrs.get('width', '')
    fallback_url = attrs['src']['fallback']
    image_src = f'img src="{fallback_url}"'
    if alt:
        image_src += f' alt="{escape(alt)}"'
    if height and width:
        image_src += f'width="{width}" height="{height}"'

    return image_src


def handle_links(attrs):
    retval = None
    if attrs:
        url = attrs.get("href") or ""
        if not is_trusted_link(url):
           attrs["target"] = "_blank"
           attrs["rel"] = "noopener nofollow"
        retval = " ".join(
            f'{k}="{escape(v)}"' for k, v in attrs.items()
        )

    return retval
