import unittest

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


if __name__ == "__main__":
    unittest.main()
