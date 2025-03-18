from blocktype import block_to_block_type, BlockType
import unittest

class Test_BlockType(unittest.TestCase):
    def test_heading(self):
        md = "### this is a heading"
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)
    def test_code(self):
        md = "```this is code```"
        self.assertEqual(block_to_block_type(md), BlockType.CODE)
    def test_quote(self):
        md = "> this is quote\n>this is quote\n>    yah quote"
        self.assertEqual(block_to_block_type(md), BlockType.QUOTE)
    def test_unordered(self):
        md = """- item 1\n- item 2\n- item 3"""
        self.assertEqual(block_to_block_type(md), BlockType.UNORDERED)
    def test_ordered(self):
        md = """1. this is\n2. the greatest\n3. victory royale"""
        self.assertEqual(block_to_block_type(md), BlockType.ORDERED)


if __name__ == "__main__":
    unittest.main()