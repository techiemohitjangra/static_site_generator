from htmlnode import HTMLNode
from typing import Optional, List, Dict


class ParentNode(HTMLNode):
    def __init__(self, tag: str,
                 children: List["HTMLNode"],
                 props: Optional[Dict[str, str]] = None):
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children is None:
            raise ValueError("ParentNode must have children")

        res = ""
        res += f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            res += child.to_html()
        res += f"</{self.tag}>"
        return res
