import unittest
from split_delimiter import split_nodes_delimiter
from textnode import TextType, TextNode

class TestSplitDelimiter(unittest.TestCase):
    def test_one_node(self):
        node = TextNode("text with **bold text**, pretty cool right?", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("text with ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(", pretty cool right?", TextType.TEXT)
                                     ])
        
    def test_multiple_nodes(self):
        node1 = TextNode("text with **bold text**, pretty cool right?", TextType.TEXT)
        node2 = TextNode("text also with **bold text**", TextType.TEXT)
        node3 = TextNode("**bold text** in the house", TextType.TEXT)

        new_nodes = split_nodes_delimiter([node1, node2, node3], "**", TextType.BOLD)

        self.assertEqual(new_nodes, [
            TextNode("text with ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(", pretty cool right?", TextType.TEXT),
            TextNode("text also with ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode("bold text", TextType.BOLD),
            TextNode(" in the house", TextType.TEXT)
        ])
    
    def test_non_list_node(self):
        node1 = TextNode("abc", TextType.TEXT)

        with self.assertRaises(TypeError) as context:
            split_nodes_delimiter(node1, "**", TextType.BOLD)
        self.assertEqual(str(context.exception), "please input a list of nodes into old_nodes")


    def test_invalid_TextType(self):
        node1 = TextNode("abc", TextType.TEXT)

        with self.assertRaises(TypeError) as context:
            split_nodes_delimiter([node1], "**", "INVALID")
        self.assertEqual(str(context.exception), "invalid text_type")

    def test_invalid_delimiter(self):
        node1 = TextNode("abc", TextType.TEXT)

        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node1], "delim", TextType.BOLD)
        self.assertEqual(str(context.exception), "invalid delimiter")

    def test_non_text_node(self):
        node1 = TextNode("abc", TextType.CODE)
        new_nodes = split_nodes_delimiter([node1], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("abc", TextType.CODE)])

    def test_missing_delimiter(self):
        node1 = TextNode("there should be a ****bold word here**", TextType.TEXT)

        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node1], "**", TextType.BOLD)
        self.assertEqual(str(context.exception), "odd number of delimiters found.")

    def test_empty_strings(self):
        node = TextNode("text with ******bold text**, pretty cool right?", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("text with ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(", pretty cool right?", TextType.TEXT)
                                     ])
    
    def test_delimiter_match_text_type(self):
        node1 = TextNode("abc", TextType.TEXT)

        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter([node1], "**", TextType.ITALIC)
        self.assertEqual(str(context.exception), "delimiter does not match text_type")

    def test_chain_usage(self):
        node1 = TextNode("text with **bold text**, pretty cool right?", TextType.TEXT)
        node2 = TextNode("text also with _italic_ text", TextType.TEXT)
        node3 = TextNode("`code text` in the house", TextType.TEXT)

        new_nodes = split_nodes_delimiter([node1, node2, node3], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)

        self.assertEqual(new_nodes, [
            TextNode("text with ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(", pretty cool right?", TextType.TEXT),
            TextNode("text also with ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
            TextNode("code text", TextType.CODE),
            TextNode(" in the house", TextType.TEXT)
        ])

def test_temp():
    node1 = TextNode("text with **bold text**, pretty cool right?", TextType.TEXT)
    node2 = TextNode("text also with _italic_ text", TextType.TEXT)
    node3 = TextNode("`code text` in the house", TextType.TEXT)

    new_nodes = split_nodes_delimiter([node1, node2, node3], "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    print(new_nodes)


if __name__ == "__main__":
    unittest.main()