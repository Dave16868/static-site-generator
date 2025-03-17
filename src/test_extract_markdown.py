from extract_markdown import extract_markdown_images, extract_markdown_links
import re
import unittest

class TestExtract(unittest.TestCase):
    def test_image(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
            )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_link(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
            )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)
   
    def test_empty(self):
        matches = extract_markdown_links("abc")
        self.assertListEqual([], matches)    

    def test_empty_2(self):
        matches = extract_markdown_links("abc[]()")
        self.assertListEqual([("", "")], matches)


if __name__ == "__main__":
    unittest.main()