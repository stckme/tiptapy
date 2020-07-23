import tiptapy.image


def test_mime():
    assert tiptapy.image.SUPPORTED_FORMATS_MAP['JPEG'] == 'image/jpeg'
    assert tiptapy.image.SUPPORTED_FORMATS_MAP['JPG'] == 'image/jpeg'
    assert tiptapy.image.url2mime('https://example.com/coolcat.webp') == 'image/webp'
