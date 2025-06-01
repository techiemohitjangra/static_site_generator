from enum import Enum
from typing import Optional
from leafnode import LeafNode


class TextType(Enum):
    TEXT = "TEXT"
    BOLD = "BOLD"
    ITALIC = "ITALIC"
    CODE = "CODE"
    LINK = "LINK"
    IMAGE = "IMAGE"


class TextNode:
    def __init__(self, text: str, text_type: TextType,
                 url: Optional[str] = None):
        self.text = text
        self.url = url
        if isinstance(text_type, TextType):
            self.text_type = text_type
        else:
            raise Exception("Invalid text_type")
        if self.text_type == TextType.BOLD or\
            self.text_type == TextType.ITALIC or\
            self.text_type == TextType.TEXT or\
                self.text_type == TextType.CODE:
            if self.url is not None:
                raise ValueError("Only LINKs and IMAGEs should have URLs")

    def __eq__(self, other) -> bool:
        if self.text == other.text and \
                self.text_type == other.text_type and \
                self.url == other.url:
            return True
        return False

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    def textnode_to_htmlnode(self) -> LeafNode:
        match self.text_type:
            case TextType.TEXT:
                return LeafNode(None, self.text)
            case TextType.BOLD:
                return LeafNode("b", self.text)
            case TextType.ITALIC:
                return LeafNode("i", self.text)
            case TextType.CODE:
                return LeafNode("code", self.text)
            case TextType.LINK:
                return LeafNode("a", self.text, {"href": self.url})
            case TextType.IMAGE:
                return LeafNode("a", None, {"src": self.url, "alt": self.text})
            case _:
                raise Exception("Invalid TextType")
