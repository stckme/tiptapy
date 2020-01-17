# tiptapy
Library that generates HTML output from JSON export of tiptap editor

``` {.sourceCode .python}
import tiptapy

s = """
{
  "type": "doc",
  "content": [
    {
      "type": "paragraph",
      "content": [
        {
          "type": "text",
          "text": "This is some inserted text. 👋"
        }
      ]
    }
  ]
}
"""

out = tiptapy.to_html(s)
print(out)
# '<p>This is some inserted text. 👋</p>'
