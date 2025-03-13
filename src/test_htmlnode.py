import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_1(self):
        node1 = HTMLNode("a", "give yourself", None, {"key1": "value1", "key2": "value2", "key3": "value3"})
        assert node1.props_to_html() == ' key1="value1" key2="value2" key3="value3"'

    def test_2(self):
        node2 = HTMLNode("b", "a present", None, {"1key": "1value"})
        assert node2.props_to_html() == ' 1key="1value"'

    def test_3(self):
        node3 = HTMLNode("c", "every day", None, None)
        node4 = HTMLNode("e", None, None, None)
        node5 = HTMLNode()
        assert node3.props_to_html() == ""
        assert node4.props_to_html() == ""
        assert node5.props_to_html() == ""

if __name__ == "__main__":
    unittest.main()