from typing import Dict, List, Optional


class HTMLNode:
    def __init__(self, tag: Optional[str] = None, value: Optional[str] = None,
                 children: Optional[List["HTMLNode"]] = None,
                 props: Optional[Dict[str, str]] = None):

        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        print(self.tag)
        raise NotImplementedError()

    def props_to_html(self) -> str:
        prop_list = []
        if self.props is None:
            return ""
        for key, value in self.props.items():
            prop_list.append(f"{key}=\"{value}\"")
        return " ".join(prop_list)

    def __repr__(self) -> str:
        return f"tag={self.tag}\nvalue={self.value}\n"
        f"children={self.children}\nprops={self.props_to_html()}"
