from leafnode import LeafNode


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, target: object) -> bool:
        if not isinstance(target, TextNode):
            return False

        for attr, value in self.__dict__.items():
            if target.__dict__.get(attr) != value:
                return False

        return True

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.text}, {self.text_type}, {self.url})"

    def text_node_to_html_node(text_node):
        types_dict = {
            "text": None,
            "bold": "b",
            "italic": "i",
            "code": "code",
            "link": "a",
            "image": "img",
        }

        if text_node.text_type not in types_dict:
            raise ValueError(
                "Invalid text type. Valid types are: " + " ".join(types_dict.keys())
            )

        if text_node.text_type == "link":
            return LeafNode(
                text_node.text, types_dict[text_node.text_type], {"href": text_node.url}
            )

        if text_node.text_type == "image":
            return LeafNode(
                "",
                types_dict[text_node.text_type],
                {"src": text_node.url, "alt": text_node.text},
            )

        return LeafNode(text_node.text, types_dict[text_node.text_type])
