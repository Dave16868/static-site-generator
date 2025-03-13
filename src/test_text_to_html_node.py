import unittest
from text_to_html_node import text_node_to_html_node
from textnode import TextNode, TextType

class Test_text_to_html_node(unittest.TestCase):
    def test_text(self):
        node = TextNode(1738, TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, 1738)

    
    def test_url(self):
        node = TextNode("sickest ntr", TextType.LINK, "www.reddit/ratatatata.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "sickest ntr")
        self.assertEqual(html_node.props_to_html(), ' href="www.reddit/ratatatata.com"')

    def test_image(self):
        node = TextNode("giant tiddies", TextType.IMAGE, "www.imgur/nekopara64.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props_to_html(), ' src="www.imgur/nekopara64.com" alt="giant tiddies"')

    def test_none(self):
        with self.assertRaises(ValueError) as context:
            text_node_to_html_node(None)
        self.assertEqual(str(context.exception), "dude you put in a None object as a text_node")


if __name__ == "__main__":
    unittest.main()
