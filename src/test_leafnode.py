import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_access_attr(self):
        node = LeafNode("some value", "a", {"prop": "value"})

        self.assertEqual(node.value, "some value")
        self.assertIsNone(node.children)
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.props, {"prop": "value"})

    def test_to_html(self):
        props_node = LeafNode("Click me!", "a", {"href": "https://www.google.com"})
        self.assertEqual(
            props_node.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )

    def test_to_html_no_value_node(self):
        no_value_node = LeafNode(None, "p", {"href": "https://www.google.com"})

        with self.assertRaises(ValueError):
            no_value_node.to_html()

    def test_to_html_no_props(self):
        no_props_node = LeafNode("This is a paragraph of text.", "p")
        self.assertEqual(no_props_node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_to_html_no_tags(self):
        no_tags_node = LeafNode("This is raw text")
        self.assertEqual(no_tags_node.to_html(), "This is raw text")
