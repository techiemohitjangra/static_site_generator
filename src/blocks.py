from typing import List
from enum import Enum
from parentnode import HTMLNode, ParentNode
from textnode import TextNode, TextType
from images_and_links import text_to_children


class BlockType(Enum):
    PARAGRAPH = "PARAGRAPH"
    HEADING = "HEADING"
    CODE = "CODE"
    QUOTE = "QUOTE"
    UNORDERED_LIST = "UNORDERED_LIST"
    ORDERED_LIST = "ORDERED_LIST"


def markdown_to_blocks(markdown: str) -> List[str]:
    blocks: List[str] = list()
    for block in markdown.strip().split("\n\n"):
        if len(block.strip()) != 0:
            blocks.append(block.strip())
    return blocks


def block_to_block_type(block: str) -> BlockType:
    # check for heading block
    if block[0] == '#':
        for i in range(1, 7):
            if block.split()[0] == "#"*i:
                return BlockType.HEADING

    # check for code block
    if block[:3] == "```" and block[-3:] == "```":
        return BlockType.CODE

    # check for quote block
    if block[0] == '>':
        quote_block: bool = True
        for line in block.split('\n'):
            if line[0] != '>':
                quote_block = False
                break
        if quote_block:
            return BlockType.QUOTE

    # check for unordered list block
    if block[0] == '-':
        unordered_list_block: bool = True
        for line in block.split('\n'):
            if line[0] != '-':
                unordered_list_block = False
                break
        if unordered_list_block:
            return BlockType.UNORDERED_LIST

    # check for ordered list block
    if block[0].isnumeric and block[1] == '0':
        unordered_list_block: bool = True
        for line in block.split('\n'):
            if not line[0].isnumeric() or line[1] != '.':
                unordered_list_block = False
                break
        if unordered_list_block:
            return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH


def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    res: List[HTMLNode] = list()
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                paragraph = " ".join(
                    [line for line in block.strip().split("\n")])
                text_nodes = text_to_children(paragraph)
                parent = ParentNode(
                    tag="p",
                    children=map(lambda x: x.textnode_to_htmlnode(),
                                 text_nodes))
                res.append(parent)
            case BlockType.HEADING:
                heading_type = block.strip().split(" ")[0]
                is_valid_heading = all(heading_type, lambda x: x == '#') \
                    and 1 >= len(heading_type) <= 6
                if is_valid_heading:
                    text_nodes = text_to_children(block)
                    parent = ParentNode(
                        tag=f"h{len(heading_type)}",
                        children=map(lambda x: x.textnode_to_htmlnode(),
                                     text_nodes))
                    res.append(parent)
                else:
                    raise Exception("invalid heading")
            case BlockType.CODE:
                text_node = TextNode(block.strip("`").lstrip(),
                                     text_type=TextType.CODE)
                parent = ParentNode(
                    tag="pre",
                    children=[text_node.textnode_to_htmlnode()],
                )
                res.append(parent)
            case BlockType.QUOTE:
                text_nodes = text_to_children(block)
                parent = ParentNode(
                    tag="blockquote",
                    children=map(lambda x: x.textnode_to_htmlnode(),
                                 text_nodes)
                )
                res.append(parent)
            case BlockType.UNORDERED_LIST:
                text_nodes = text_to_children(block)
                parent = ParentNode(
                    tag="ul",
                    children=map(lambda x: x.textnode_to_htmlnode(),
                                 text_nodes)
                )
                res.append(parent)
            case BlockType.ORDERED_LIST:
                text_nodes = text_to_children(block)
                parent = ParentNode(
                    tag="ol",
                    children=map(lambda x: x.textnode_to_htmlnode(),
                                 text_nodes)
                )
                res.append(parent)
            case _:
                raise Exception((f"Invalid block type: \"{block_type}\" for "
                                 f"block \"{block}\""))
    return ParentNode("div", children=res)
