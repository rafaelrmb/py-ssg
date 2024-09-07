import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_attr_access(self):
        children_nodes = (
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
            ],
        )
        parent = ParentNode("p", children_nodes, {"class": "text"})

        self.assertEqual(parent.children, children_nodes)
        self.assertEqual(parent.tag, "p")
        self.assertEqual(parent.props, {"class": "text"})

    def test_not_none_children(self):
        children_nodes = (
            [
                LeafNode("b", "Bold text"),
            ],
        )
        parent = ParentNode("p", children_nodes, {"class": "text"})

        self.assertIsNotNone(parent.children)

    def test_not_empty_children(self):
        parent = ParentNode(
            "p",
            [
                LeafNode("Bold text", "b"),
            ],
            {"class": "text"},
        )

        self.assertGreater(len(parent.children), 0)

    def test_not_none_tag(self):
        parent = ParentNode([], "a", {"class": "text"})

        self.assertIsNotNone(parent.tag)

    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("Bold text", "b"),
                LeafNode("Normal text", None),
                LeafNode("italic text", "i"),
                LeafNode("Normal text", None),
            ],
        )

        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_to_html_nested_parents(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("Bold text", "b"),
                    ],
                ),
                LeafNode("italic text", "i"),
            ],
        )

        self.assertEqual(
            node.to_html(),
            "<div><p><b>Bold text</b></p><i>italic text</i></div>",
        )
