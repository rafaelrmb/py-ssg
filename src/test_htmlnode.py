import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_attr_access(self):
        node_attr = {
            "href": "https://www.google.com",
            "target": "_blank",
        }

        node = HTMLNode("a", "some value here", "test_children", node_attr)

        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "some value here")
        self.assertEqual(node.children, "test_children")
        self.assertEqual(node.props, node_attr)

    def test_eq(self):
        node = HTMLNode("a", "some value here", "test_children", "props_here")
        node2 = HTMLNode("a", "some value here", "test_children", "props_here")

        self.assertTrue(node.__eq__(node2))

    def test_repr(self):
        node = HTMLNode("a", "some value here", "test_children", "props_here")
        self.assertEqual(
            node.__repr__(), "HTMLNode(a, some value here, test_children, props_here)"
        )

    def test_all_attr_none(self):
        node = HTMLNode()

        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_props_is_dict(self):
        node = HTMLNode("tag", "value", "chidren", {"prop": "value"})

        self.assertTrue(node.props is not None and isinstance(node.props, dict))
        self.assertDictEqual(node.props, {"prop": "value"})

    def test_children_is_list(self):
        node = HTMLNode("tag", "value", [], "props")

        self.assertTrue(node.children is not None and isinstance(node.children, list))
        self.assertListEqual(node.children, [])

    def test_to_html(self):
        node = HTMLNode()
        with self.assertRaises(Exception):
            node.to_html()

    def test_props_to_html(self):
        node_attr = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode("tag", "value", "chidren", node_attr)
        print(node.props_to_html())
        self.assertEqual(
            node.props_to_html(), ' href="https://www.google.com" target="_blank" '
        )
