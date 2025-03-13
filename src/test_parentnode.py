import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_leaf_only(self):
        leaf1 = LeafNode("l1", "text_1")
        leaf2 = LeafNode(None, "text_2")
        leaf3 = LeafNode("l3", "text_3")
        parent = ParentNode("p",[leaf1, leaf2, leaf3])
        
        self.assertEqual(parent.to_html(), "<p><l1>text_1</l1>text_2<l3>text_3</l3></p>")
        


if __name__ == "__main__":
    unittest.main()