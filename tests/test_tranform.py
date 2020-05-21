import os
import pytest
import tiptapy
import json
from tiptapy import extras


tags_to_test = (
    "simple",
    "blockquote",
    "bulletlist",
    "mark_tags",
    "ordered_list",
    "image",
    "image-missing_caption",
    "image-no_caption",
    "featuredimage",
    "featuredimage-missing_caption",
    "featuredimage-no_caption",
    "horizontal_rule",
    "embed",
    "embed-missing_caption",
    "embed-no_caption"
)


def build_test_data():
    """
    Scan data directories and return test data
    """
    store = {'json': {}, 'html': {}}
    for data_type in store:
        dir_path = os.path.abspath(f'tests/data/{data_type}/')
        for file in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file)
            with open(file_path) as f:
                data = f.read()
                store[data_type][file.split(f'.{data_type}')[0]] = data
    return store['json'], store['html']


json_data, html_data = build_test_data()


@pytest.mark.parametrize("tag", tags_to_test)
def test_html_tag(tag):
    """
    Test expected json input with the expected html.
    """
    tag_data = json_data[tag]
    expected_html = html_data[tag]
    assert tiptapy.to_html(tag_data) == expected_html
