class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, target: object) -> bool:
        print(self.__class__.__name__)
        if not isinstance(target, TextNode):
            return False

        for attr, value in self.__dict__.items():
            if target.__dict__.get(attr) != value:
                return False

        return True

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.text}, {self.text_type}, {self.url})"
