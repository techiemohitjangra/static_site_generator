from leafnode import LeafNode
import unittest


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_p_alt(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {
                        "href": "https://www.google.com"})
        self.assertEqual(node.to_html(),
                         "<a href=\"https://www.google.com\">Click me!</a>")


if __name__ == "__main__":
    unittest.main()
