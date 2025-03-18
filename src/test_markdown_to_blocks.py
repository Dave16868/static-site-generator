from markdown_to_blocks import markdown_to_blocks
import unittest

class Test_Markdown_To_Blocks(unittest.TestCase):
    def test_1(self):
        md = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_2(self):
        md = """LINE 111111111

    LINE 2222
    22222

    LINE 3333
    3333333
    3333333



    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "LINE 111111111",
                "LINE 2222\n22222",
                "LINE 3333\n3333333\n3333333",
            ],
        )




if __name__ == "__main__":
    unittest.main()