import unittest
from split_delimiters import split_nodes_delimiter
from textnode import TextType, TextNode


class TestInlineElements(unittest.TestCase):

    def test_inline_bold(self):
        input = "This is text with a **bolded phrase** in the middle"
        res = split_nodes_delimiter([input], '**', TextType.BOLD)
        expected_res = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.TEXT),
        ]
        self.assertListEqual(res, expected_res)

    def test_inline_codeblock(self):
        node = TextNode("This is text with a ```code block``` word",
                        TextType.TEXT)
        res = split_nodes_delimiter([node], "```", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertListEqual(res, expected)

    def test_inline_italic(self):
        node = TextNode(
            "This is text with _italic texts is here_ words", TextType.TEXT)
        res = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected = [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("italic texts is here", TextType.ITALIC),
            TextNode(" words", TextType.TEXT),
        ]
        self.assertListEqual(res, expected)


if __name__ == "__main__":
    unittest.main()
