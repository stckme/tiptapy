from tiptapy import is_trusted_link


def test_is_trusted_link():
    url = "https://pypi.org/"
    assert is_trusted_link(url) is False
