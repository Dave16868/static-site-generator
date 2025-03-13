import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_leaf_only(self):
        leaf1 = LeafNode("l1", "text_1")
        leaf2 = LeafNode(None, "text_2")
        leaf3 = LeafNode("l3", "text_3")
        boss = ParentNode("p",[leaf1, leaf2, leaf3])
        
        self.assertEqual(boss.to_html(), "<p><l1>text_1</l1>text_2<l3>text_3</l3></p>")

    def test_parent(self):
        leaf1 = LeafNode("l1", "text_1")
        leaf2 = LeafNode(None, "text_2")
        leaf3 = LeafNode("l3", "text_3")
        parent1 = ParentNode("p1", [leaf1])
        parent2 = ParentNode("p2", [leaf2])
        parent3 = ParentNode("p3", [leaf3])
        boss = ParentNode("boss", [parent1, parent2, parent3])
        
        self.assertEqual(boss.to_html(), "<boss><p1><l1>text_1</l1></p1><p2>text_2</p2><p3><l3>text_3</l3></p3></boss>")

    def test_props(self):
            leaf1 = LeafNode("l1", "text_1", {"goblck": "nvrgobck"})
            leaf2 = LeafNode(None, "text_2")
            leaf3 = LeafNode("l3", "text_3")
            parent1 = ParentNode("p1", [leaf1])
            parent2 = ParentNode("p2", [leaf2])
            parent3 = ParentNode("p3", [leaf3], {"genre": "ntr", "#": 21})
            boss = ParentNode("boss", [parent1, parent2, parent3])
            
            self.assertEqual(boss.to_html(), '<boss><p1><l1 goblck="nvrgobck">text_1</l1></p1><p2>text_2</p2><p3 genre="ntr" #="21"><l3>text_3</l3></p3></boss>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()