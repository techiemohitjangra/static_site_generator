import unittest
from split_delimiters import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitDelimiters(unittest.TestCase):
    def test_split_delilmiters_code(self):
        text = ("this is a test for splitting code delimiters ```here is the "
                "code block``` split this code block and text")
        res = split_nodes_delimiter([text], '```', TextType.CODE)
        expected = [
            TextNode("this is a test for splitting code delimiters ",
                     TextType.TEXT),
            TextNode("here is the code block", TextType.CODE),
            TextNode(" split this code block and text", TextType.TEXT),
        ]
        self.assertListEqual(res, expected)

    def test_split_delilmiters_italic(self):
        text = ("this is a test for splitting italic delimiters _here is the "
                "italic text_ split this italic text and regular text")
        res = split_nodes_delimiter([text], '_', TextType.ITALIC)
        expected = [
            TextNode("this is a test for splitting italic delimiters ",
                     TextType.TEXT),
            TextNode("here is the italic text", TextType.ITALIC),
            TextNode(" split this italic text and regular text",
                     TextType.TEXT),
        ]
        self.assertListEqual(res, expected)

    def test_split_delilmiters_bold(self):
        text = ("this is a test for splitting bold delimiters **here is the "
                "bold text** split this bold text and regular text")
        res = split_nodes_delimiter([text], '**', TextType.BOLD)
        expected = [
            TextNode("this is a test for splitting bold delimiters ",
                     TextType.TEXT),
            TextNode("here is the bold text", TextType.BOLD),
            TextNode(" split this bold text and regular text", TextType.TEXT),
        ]
        self.assertListEqual(res, expected)

    def test_split_delilmiters_bold_and_italic(self):
        text = ("this is a test for splitting bold and italic delimiters"
                " **here is the bold text** split this bold text and _here"
                " is the italic text_ now split them both")
        res_bold_split = split_nodes_delimiter([text], '**', TextType.BOLD)
        expected_bold_split = [
            TextNode(
                "this is a test for splitting bold and italic delimiters ",
                TextType.TEXT
            ),
            TextNode(
                "here is the bold text",
                TextType.BOLD
            ),
            TextNode(
                (" split this bold text and _here is the italic text_ now "
                    "split them both"),
                TextType.TEXT),
        ]
        self.assertListEqual(res_bold_split, expected_bold_split)
        res = split_nodes_delimiter(res_bold_split, '_', TextType.ITALIC)
        expected_res = [
            TextNode(
                "this is a test for splitting bold and italic delimiters ",
                TextType.TEXT
            ),
            TextNode(
                "here is the bold text",
                TextType.BOLD
            ),
            TextNode(" split this bold text and ", TextType.TEXT),
            TextNode("here is the italic text", TextType.ITALIC),
            TextNode(" now split them both", TextType.TEXT),
        ]
        self.assertListEqual(res, expected_res)


if __name__ == "__main__":
    unittest.main()
