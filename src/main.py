from textnode import TextNode, TextType


def main() -> int:
    obj = TextNode("This is some anchor text",
                   TextType.LINK, "https://www.boot.dev")
    print(obj)


if __name__ == "__main__":
    main()
