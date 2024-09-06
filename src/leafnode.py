from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self):
        props_string = ""

        if self.value is None or self.value == "":
            raise ValueError

        if self.tag is None or self.tag == "":
            return self.value

        if self.props:
            props_string = self.props_to_html()

        return f"<{self.tag}{props_string}>{self.value}</{self.tag}>"
