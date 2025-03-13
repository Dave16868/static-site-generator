import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_1(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_2(self):
        node = LeafNode("papi", "Drake has a huge snake")
        self.assertEqual(node.to_html(), "<papi>Drake has a huge snake</papi>")

    def test_leaf_to_html_3(self):
        node = LeafNode(None, "I will rip your cock out and stick it into your mother's decapitated head")
        self.assertEqual(node.to_html(), "I will rip your cock out and stick it into your mother's decapitated head")

    def test_leaf_to_html_4(self):
        node = LeafNode("apex", "fortnite and mark ass twinkie", {"will": "smith", "john": "sins"})
        self.assertEqual(node.to_html(), '<apex will="smith" john="sins">fortnite and mark ass twinkie</apex>')

    def test_leaf_to_html_4(self):
        node = LeafNode("", "oh no empty tag")
        self.assertEqual(node.to_html(), "oh no empty tag")

if __name__ == "__main__":
    unittest.main()