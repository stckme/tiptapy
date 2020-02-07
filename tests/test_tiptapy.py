import pytest
import tiptapy


def test_to_html():
    """Test to check to_html() function"""
    simple_json = """
    {
    "type": "doc",
    "content": [
      {
        "type": "paragraph",
        "content": [
          {
            "type": "text",
            "text": "Here is an example of simple formatted text"
          }
        ]
      }
    ]
  }"""
    expected_html = """<p>Here is an example of simple formatted text</p>"""
    assert tiptapy.to_html(simple_json) == expected_html


def test_blockquote():
    """Test to check BlockQuote"""
    blockquote_json = """
    {
    "type": "doc",
    "content": [
      {
        "type": "blockquote",
        "content": [
          {
            "type": "paragraph",
            "content": [
              {
                "type": "text",
                "text": "This is a blockquote"
              }
            ]
          }
        ]
      }
    ]
  }
  """
    expected_html = """<blockquote><p>This is a blockquote</p></blockquote>"""
    assert tiptapy.to_html(blockquote_json) == expected_html


@pytest.mark.skip(reason="Need to generate hardbreak json")
def test_hardbreak():
    """Test to check HardBreak"""
    hardbreak_json = """
  """
    expected_html = """"""
    assert tiptapy.to_html(hardbreak_json) == expected_html


def test_bulletlist():
    """Test to check BulletList"""
    bulletlist = """{
  "type": "doc",
  "content": [
    {
      "type": "bullet_list",
      "content": [
        {
          "type": "list_item",
          "content": [
            {
              "type": "paragraph",
              "content": [
                {
                  "type": "text",
                  "text": "Un"
                }
              ]
            }
          ]
        },
        {
          "type": "list_item",
          "content": [
            {
              "type": "paragraph",
              "content": [
                {
                  "type": "text",
                  "text": "dos"
                }
              ]
            }
          ]
        },
        {
          "type": "list_item",
          "content": [
            {
              "type": "paragraph",
              "content": [
                {
                  "type": "text",
                  "text": "tres"
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
  """
    expected_html = """<ul><li><p>Un</p></li><li><p>dos</p></li><li><p>tres</p></li></ul>"""
    assert tiptapy.to_html(bulletlist) == expected_html


def test_text():
    """Test to check mark_tags bold,italic,link"""
    text_json = """
  {
  "type": "doc",
  "content": [
    {
      "type": "paragraph",
      "content": [
        {
          "type": "text",
          "text": "This is "
        },
        {
          "type": "text",
          "marks": [
            {
              "type": "bold"
            }
          ],
          "text": "bold"
        },
        {
          "type": "text",
          "text": ", this is "
        },
        {
          "type": "text",
          "marks": [
            {
              "type": "italic"
            }
          ],
          "text": "italic"
        },
        {
          "type": "text",
          "text": " and this has a "
        },
        {
          "type": "text",
          "marks": [
            {
              "type": "link",
              "attrs": {
                "href": "https://foobar.withgoogle.com/"
              }
            }
          ],
          "text": "link"
        }
      ]
    }
  ]
}
  """
    expected_html = """<p>This is <strong>bold</strong>, this is <em>italic</em> and this has a <a href="https://foobar.withgoogle.com/">link</a></p>"""
    assert tiptapy.to_html(text_json) == expected_html
