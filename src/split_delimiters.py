from typing import List, Union
from textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes: List[Union[str, TextNode]],
                          delimiter: str,
                          text_type: TextType) -> List[TextNode]:
    res: List[TextNode] = []
    for node in old_nodes:
        start = 0
        if isinstance(node, str):
            end = len(node) - 1
            while start < end and node.find(delimiter, start+1, end) != -1:
                start_index = node.find(delimiter, start, end)
                end_index = node.find(delimiter, start_index+1, end)
                if end_index == -1:
                    raise Exception("closing delimiter not found for "
                                    f"'{delimiter}' for starting '{delimiter}'"
                                    " at index {start_index}"
                                    )
                res.append(TextNode(node[start:start_index], TextType.TEXT))
                match delimiter:
                    case '```':
                        res.append(
                            TextNode(node[start_index+3:end_index],
                                     text_type))
                        start = end_index+3
                    case '`':
                        res.append(
                            TextNode(node[start_index+1:end_index],
                                     text_type))
                        start = end_index+1
                    case '**':
                        res.append(
                            TextNode(node[start_index+2:end_index],
                                     text_type))
                        start = end_index+2
                    case '_':
                        res.append(
                            TextNode(node[start_index+1:end_index],
                                     text_type))
                        start = end_index+1
                    case _:
                        raise Exception(f"Invalid delimiter \"{delimiter}\"")
            res.append(TextNode(node[start:], TextType.TEXT))
        elif isinstance(node, TextNode):
            if node.text_type == TextType.TEXT:
                end = len(node.text)-1
                while start < end and  \
                        node.text.find(delimiter, start+1, end) != -1:
                    start_index = node.text.find(delimiter, start, end)
                    end_index = node.text.find(delimiter, start_index+1, end)
                    if end_index == -1:
                        raise Exception("closing delimiter not found for "
                                        f"'{delimiter}' for starting "
                                        f"'{delimiter}' at index {start_index}"
                                        )
                    res.append(
                        TextNode(node.text[start:start_index], TextType.TEXT))
                    match delimiter:
                        case '```':
                            res.append(
                                TextNode(node.text[start_index+3:end_index],
                                         text_type))
                            start = end_index+3
                        case '`':
                            res.append(
                                TextNode(node.text[start_index+1:end_index],
                                         text_type))
                            start = end_index+1
                        case '**':
                            res.append(
                                TextNode(node.text[start_index+2:end_index],
                                         text_type))
                            start = end_index+2
                        case '_':
                            res.append(
                                TextNode(node.text[start_index+1:end_index],
                                         text_type))
                            start = end_index+1
                        case _:
                            raise Exception(
                                f"Invalid delimiter \"{delimiter}\"")
                res.append(TextNode(node.text[start:], TextType.TEXT))
            else:
                res.append(node)

    return res
