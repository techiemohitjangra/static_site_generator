from typing import Tuple, List, Union
from textnode import TextNode, TextType
from split_delimiters import split_nodes_delimiter
import re


def extract_markdown_images(text) -> Tuple[str, str]:
    matches = re.findall("!\\[(.*?)\\]\\((.*?)\\)",
                         text,
                         flags=re.RegexFlag.MULTILINE)
    return matches


def extract_markdown_links(text) -> Tuple[str, str]:
    matches = re.findall("[^!]\\[(.*?)\\]\\((.*?)\\)",
                         text,
                         flags=re.RegexFlag.MULTILINE)
    return matches


def split_nodes_image(old_nodes: List[Union[TextNode, str]]):
    res: List[TextNode] = []
    for node in old_nodes:
        if isinstance(node, str):
            matches = re.findall("!\\[(.*?)\\]\\((.*?)\\)", node)
            start = 0
            end = len(node) - 1
            for match in matches:
                image = f"![{match[0]}]({match[1]})"
                start_idx = node.find(image)
                end_idx = node.find(image) + len(image) - 1  # end inclusive
                res.append(TextNode(node[start:start_idx], TextType.TEXT))
                res.append(TextNode(match[0], TextType.IMAGE, match[1]))
                start = end_idx + 1
            remaining_text: str = node[start:end+1]
            if len(remaining_text.strip()) != 0:
                res.append(TextNode(remaining_text, TextType.TEXT))
        if isinstance(node, TextNode):
            if node.text_type == TextType.TEXT:
                matches = re.findall("!\\[(.*?)\\]\\((.*?)\\)", node.text)
                start = 0
                end = len(node.text) - 1
                for match in matches:
                    image = f"![{match[0]}]({match[1]})"
                    start_idx = node.text.find(image)
                    end_idx = node.text.find(
                        image) + len(image) - 1  # end inclusive
                    res.append(
                        TextNode(node.text[start:start_idx], TextType.TEXT))
                    res.append(TextNode(match[0], TextType.IMAGE, match[1]))
                    start = end_idx + 1
                remaining_text: str = node.text[start:end+1]
                if len(remaining_text.strip()) != 0:
                    res.append(TextNode(remaining_text, TextType.TEXT))
            else:
                res.append(node)
    return res


def split_nodes_link(old_nodes: List[Union[TextNode, str]]):
    res: List[TextNode] = []
    for node in old_nodes:
        if isinstance(node, str):
            matches = re.findall("[^!]\\[(.*?)\\]\\((.*?)\\)", node)
            start = 0
            end = len(node) - 1
            for match in matches:
                link = f"[{match[0]}]({match[1]})"
                start_idx = node.find(link)
                end_idx = node.find(link) + len(link) - 1  # end inclusive
                res.append(TextNode(node[start:start_idx], TextType.TEXT))
                res.append(TextNode(match[0], TextType.LINK, match[1]))
                start = end_idx + 1
            remaining_text: str = node[start:end+1]
            if len(remaining_text.strip()) != 0:
                res.append(TextNode(remaining_text, TextType.TEXT))
        if isinstance(node, TextNode):
            if node.text_type == TextType.TEXT:
                matches = re.findall("[^!]\\[(.*?)\\]\\((.*?)\\)", node.text)
                start = 0
                end = len(node.text) - 1
                for match in matches:
                    link = f"[{match[0]}]({match[1]})"
                    start_idx = node.text.find(link)
                    end_idx = node.text.find(
                        link) + len(link) - 1  # end inclusive
                    res.append(
                        TextNode(node.text[start:start_idx], TextType.TEXT))
                    res.append(TextNode(match[0], TextType.LINK, match[1]))
                    start = end_idx + 1
                remaining_text: str = node.text[start:end+1]
                if len(remaining_text.strip()) != 0:
                    res.append(TextNode(remaining_text, TextType.TEXT))
            else:
                res.append(node)
    return res


def text_to_children(text: str):
    parse_code = split_nodes_delimiter([text], "```", TextType.CODE)
    parse_italic = split_nodes_delimiter(parse_code.copy(),
                                         "_", TextType.ITALIC)
    parse_bold = split_nodes_delimiter(parse_italic.copy(),
                                       "**", TextType.BOLD)
    parse_inline_code = split_nodes_delimiter(parse_bold.copy(),
                                              "`", TextType.CODE)
    return split_nodes_link(split_nodes_image(parse_inline_code.copy()).copy())
