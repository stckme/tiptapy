# Tiptapy
### Library that generates HTML output from JSON export of tiptap editor 

![tiptapy](https://github.com/scrolltech/tiptapy/workflows/tiptapy/badge.svg)

### Install 


```bash
pip install tiptapy
```

### Usage

``` {.sourceCode .python}
import tiptapy

s = """

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
              "text": "Readability counts."
            }
          ]
        },
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "marks": [
                {
                  "type": "link",
                  "attrs": { "href": "https://en.wikipedia.org/wiki/Zen_of_Python" }
                }
              ],
              "text": "Zen of Python"
            },
            {
              "type": "text", "text": " By "
            },
            {
              "type": "text",
              "marks": [
                {
                  "type": "bold"
                }
              ],
              "text": "Tom Peters"
            }
          ]
        }
      ]
    }
  ]
}
"""

out = tiptapy.to_html(s)
print(out)
```

#### Output
``` {.sourceCode .html}
<blockquote>
  <p>Readability counts.</p>
  <p>
      <a href="https://en.wikipedia.org/wiki/Zen_of_Python">Zen of Python</a> By 
      <strong>Tom Peters</strong>
  </p>
</blockquote>
```
