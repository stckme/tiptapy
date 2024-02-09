import pkgutil
from html import escape
from string import Template
from urllib.parse import quote_plus, urlparse


def make_img_src(attrs):
    alt = attrs.get("alt", "").strip()
    height = attrs.get("height", "")
    width = attrs.get("width", "")
    fallback_url = quote_plus(attrs["src"]["fallback"]).strip()
    image_src = f'img src="{fallback_url}"'
    if alt:
        image_src += f' alt="{escape(alt)}"'
    if width:
        image_src += f' width="{width}"'
    if height:
        image_src += f' height="{height}"'

    return image_src


def build_link_handler(config):
    def handle_links(attrs):
        retval = None
        if attrs:
            url = quote_plus(attrs.pop("href", "")).strip()
            link = urlparse(url)
            if not (
                link.netloc == config.DOMAIN
                or link.netloc.endswith(f".{config.DOMAIN}")
            ):
                attrs["href"] = url
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
