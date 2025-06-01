from typing import Optional, Dict
from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag: Optional[str],
                 value: str,
                 props: Optional[Dict[str, str]] = None):
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("All leaf node must have a value")
        if self.tag is None:
            return self.value
        props = " " + self.props_to_html() if self.props is not None else ""
        return f"<{self.tag}{props}>{self.value}</{self.tag}>"
