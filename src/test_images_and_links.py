from images_and_links import extract_markdown_images, extract_markdown_links
from images_and_links import split_nodes_image, split_nodes_link
from images_and_links import text_to_children
from textnode import TextType, TextNode
import unittest


class TestImageLinkExtraction(unittest.TestCase):

    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        matches = extract_markdown_images(text)
        expected_matches = [("image", "https://i.imgur.com/zjjcJKZ.png")]
        self.assertListEqual(expected_matches, matches)

    def test_extract_markdown_images2(self):
        text = ("This is text with a "
                "![rick roll](https://i.imgur.com/aKaOqIh.gif) "
                "and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
        matches = extract_markdown_images(text)
        expected_matches = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertListEqual(expected_matches, matches)

    def test_extract_markdown_links(self):
        text = ("This is text with a link [to boot dev](https://www.boot.dev)"
                "and [to youtube](https://www.youtube.com/@bootdotdev)")
        matches = extract_markdown_links(text)
        expected_matches = [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev")
        ]
        self.assertListEqual(expected_matches, matches)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) "
            "and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE,
                         "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image",
                    TextType.IMAGE,
                    "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        text = ("This is text with a link [to boot dev](https://www.boot.dev) "
                "and [to youtube](https://www.youtube.com/@bootdotdev)")
        node = TextNode(text, TextType.TEXT)
        new_nodes = split_nodes_link([node])
        expected_nodes = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK,
                     "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertListEqual(expected_nodes, new_nodes)

    def test_text_to_textnode(self):
        self.maxDiff = None
        text = ("This is **text** with an _italic_ word and a ```code block```"
                " and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)"
                " and a [link](https://boot.dev)")
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE,
                     "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        new_nodes = text_to_children(text)
        self.assertListEqual(new_nodes, expected_nodes)


if __name__ == "__main__":
    unittest.main()
