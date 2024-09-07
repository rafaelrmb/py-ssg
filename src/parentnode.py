from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")

        if len(self.children) == 0:
            raise ValueError("ParentNode children cannot be an empty list")

        html = ""

        for child in self.children:
            html += child.to_html()

        return f"<{self.tag}>" + html + f"</{self.tag}>"
