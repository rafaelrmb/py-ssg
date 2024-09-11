import unittest

from leafnode import LeafNode
from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
        self.assertTrue(node.__eq__(node2))

    def test_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node3 = TextNode("This is a text node", "bold", "fakeurl.fake")
        self.assertNotEqual(node, node3)
        self.assertFalse(node.__eq__(node3))

    def test_repr(self):
        node = TextNode("Test Node", "bold", "fakeurl.fake")
        self.assertEqual(node.__repr__(), "TextNode(Test Node, bold, fakeurl.fake)")

    def test_attr_access(self):
        node = TextNode("Test Node", "bold", "fakeurl.fake")
        self.assertEqual(node.text, "Test Node")
        self.assertEqual(node.text_type, "bold")
        self.assertEqual(node.url, "fakeurl.fake")

    def test_empty_url_attr(self):
        node = TextNode("This is a text node", "bold")

        self.assertIsNone(node.url)

    def test_non_empty_url_attr(self):
        node_with_url = TextNode("This is a text node", "bold", "urlhere")
        self.assertIsNotNone(node_with_url.url)

    def test_text_to_html_no_props(self):
        node = TextNode("This is a text node", "bold")

        self.assertEqual(
            node.text_node_to_html_node(node).__repr__(),
            LeafNode("This is a text node", "b").__repr__(),
        )

    def test_text_to_html_with_props(self):
        node_with_url = TextNode("This is a text node", "link", "fakeurl.com")

        self.assertEqual(
            node_with_url.text_node_to_html_node(node_with_url).__repr__(),
            LeafNode("This is a text node", "a", {"href": "fakeurl.com"}).__repr__(),
        )

    def test_text_to_html_invalid_text_type(self):
        node_with_url = TextNode("This is a text node", "wrong")

        with self.assertRaises(ValueError):
            node_with_url.text_node_to_html_node(node_with_url)

    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", "text")

        self.assertEqual(
            node.split_nodes_by_delimiter([node], "`", "code"),
            [
                TextNode("This is text with a ", "text"),
                TextNode("code block", "code"),
                TextNode(" word", "text"),
            ],
        )

    def test_split_nodes_multiple_delimiters(self):
        node = TextNode(
            "This is text with a `code block` word and another `code block here`",
            "text",
        )

        self.assertEqual(
            node.split_nodes_by_delimiter([node], "`", "code"),
            [
                TextNode("This is text with a ", "text"),
                TextNode("code block", "code"),
                TextNode(" word and another ", "text"),
                TextNode("code block here", "code"),
            ],
        )

    def test_split_nodes_different_delimiters(self):
        node = TextNode(
            "This is text with a **bold word** and another *italic word*",
            "text",
        )

        self.assertEqual(
            node.split_nodes_by_delimiter([node], "**", "bold"),
            [
                TextNode("This is text with a ", "text"),
                TextNode("bold word", "bold"),
                TextNode(" and another *italic word*", "text"),
            ],
        )


if __name__ == "__main__":
    unittest.main()
