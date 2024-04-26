from tiptapy import BaseDoc
import json

doc = """{"default": {"type": "doc", "content": [{"type": "paragraph", "attrs": {"id": "7ae508d6-54f0-4680-b564-31cd1f8d2092", "indent": 0, "textAlign": "left"}, "content": [{"type": "text", "text": "I'm happy to help, but I think there may be some confusion. As a government analyst, I'm tasked with assisting my colleague in drafting a reply to a federal contract proposal. I don't think writing a short story about cops and robbers would be relevant to this task."}]}, {"type": "paragraph", "attrs": {"id": "fb1635df-d833-4373-ab89-7b13da9da0a7", "indent": 0, "textAlign": "start"}, "content": [{"type": "text", "text": "Could you please clarify or provide more context on how this story relates to the federal contract proposal or the task at hand? I'd be happy to assist you in drafting a response to the proposal, but I want to ensure I'm providing the most relevant and accurate information possible.", "marks": [{"type": "highlight", "attrs": {"color": null}}]}]}, {"type": "paragraph", "attrs": {"id": "78201f08-810e-40dc-a9b3-7621f374dfa8", "indent": 0, "textAlign": "start"}, "content": [{"type": "text", "text": "select documents.content from documents\nwhere documents.id = 'cdf7df14-3194-484a-9475-4e01a8db1b51'"}]}, {"type": "codeBlock", "attrs": {"language": "pgsql"}}]}}"""
print(json.loads(doc))


# renderer = BaseDoc(config=None)
# out = renderer.render(json.dumps(json.loads(doc)["default"]))
# print(out)
