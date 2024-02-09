import pkgutil
from html import escape
from string import Template
from urllib.parse import urlparse


def make_img_src(attrs):
    alt = escape(attrs.get("alt", "").strip())
    height = escape(str(attrs.get("height", "")))
    width = escape(str(attrs.get("width", "")))
    fallback_url = escape(attrs["src"]["fallback"].strip())
    img = f'img src="{fallback_url}"'
    if alt:
        img += f' alt="{alt}"'
    if width:
        img += f' width="{width}"'
    if height:
        img += f' height="{height}"'

    return img


def build_link_handler(config):
    def handle_links(attrs):
        retval = None
        if attrs:
            url = attrs.get("href", "").strip()
            link = urlparse(url)
            if not (
                link.netloc == config.DOMAIN
                or link.netloc.endswith(f".{config.DOMAIN}")
            ):
                attrs["target"] = "_blank"
                attrs["rel"] = "noopener nofollow"
            retval = " ".join(
                f'{k}="{escape(v)}"' for k, v in attrs.items() if v is not None
            )
        return retval

    return handle_links


def get_audio_player_block():
    audio_player_block = pkgutil.get_data(
        __name__, "templates/stack-audio-player.html"
    ).decode()
    return audio_player_block


def get_doc_block(ext, fname, size, src):
    document_block = pkgutil.get_data(
        __name__, "templates/stack-document.html"
    ).decode()
    document = Template(document_block)
    html = document.substitute(
        fileformat=ext[:4], filename=fname, filesize=size, filesrc=src
    )
    return html
