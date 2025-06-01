import unittest
from htmlnode import HTMLNode
from typing import Dict


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        div_props: Dict[str, str] = dict()
        div_props["name"] = "div"
        div_props["class"] = "cls-body"
        node1 = HTMLNode("div", None, [], div_props)
        props = node1.props_to_html()
        self.assertTrue("name=\"div\"" in props)
        self.assertTrue("class=\"cls-body\"" in props)


if __name__ == "__main__":
    unittest.main()
