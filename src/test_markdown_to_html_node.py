import unittest
from markdown_to_html_node import markdown_to_html_node, markdown_to_blocks

class Block_To_HTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph       
    text in a p
    tag here            

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading(self):
        md = """
    ### heading 
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html, 
            "<div><h3>heading</h3></div>"
        )
    
    def test_unordered(self):
        md = """
    - item 1
    - item 2
    - item 3
    - item 4
    - item 5
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html, 
            "<div><ul><li>item 1</li><li>item 2</li><li>item 3</li><li>item 4</li><li>item 5</li></ul></div>"
        )

    def test_ordered(self):
        md = """
    1. thing
    2. like
    3. this
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html, 
            "<div><ol><li>thing</li><li>like</li><li>this</li></ol></div>"
        )

    def test_quote(self):
        md = """
    > quote 1
    >quote 2
    >  quote 3
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html, 
            "<div><blockquote>quote 1 quote 2 quote 3</blockquote></div>"
        )

def temp():
    md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    print(html)

temp()

if __name__ == "__main__":
    unittest.main()