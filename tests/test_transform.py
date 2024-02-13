import os

import pytest

import tiptapy

tags_to_test = (
    "simple",
    "blockquote",
    "bulletlist",
    "mark_tags",
    "ordered_list",
    "paragraph",
    "paragraph-is_renderable",
    "paragraph-codemark",
    "paragraph-escape",
    "image",
    "image-is_renderable",
    "image-missing_caption",
    "image-no_caption",
    "image-mime_type",
    "image-height_width",
    "featuredimage",
    "featuredimage-is_renderable",
    "featuredimage-missing_caption",
    "featuredimage-no_caption",
    "featuredimage-mime_type",
    "featuredimage-height_width",
    "horizontal_rule",
    "embed",
    "embed-missing_caption",
    "embed-no_caption",
    "embed-null_caption",
    "heading",
    "is_renderable",
    "code_block",
    "code_block-is_renderable",
    "audio",
    "audio-no_caption",
    "audio-is_renderable",
    "document-pdf",
    "document-is_renderable",
    "document-sketch",
    "camel-case",
    "data_attributes",
    "xss",
)


class config:
    """
    Config class to store constans which are used by the othe nodes.
    """

    DOMAIN = "python.org"


def build_test_data(rebuild_html=False):
    """
    Scan data directories and return test data

    :param rebuild_html: If True, rebuild the html files
    """
    store = {"json": {}, "html": {}}
    for data_type in store:
        dir_path = os.path.abspath(f"tests/data/{data_type}/")
        for file in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file)
            with open(file_path) as f:
                data = f.read()
                store[data_type][file.split(f".{data_type}")[0]] = data

            # Use this to (re)generate the html files
            if rebuild_html and data_type == "json":
                with open(file_path.replace("json", "html"), "w") as f:
                    f.write(tiptapy.BaseDoc(config).render(data))

    return store["json"], store["html"]


json_data, html_data = build_test_data()


@pytest.mark.parametrize("tag", tags_to_test)
def test_html_tag(tag):
    """
    Test expected json input with the expected html.
    """
    tag_data = json_data[tag]
    expected_html = html_data[tag]

    renderer = tiptapy.BaseDoc(config)
    assert renderer.render(tag_data) == expected_html.strip()
