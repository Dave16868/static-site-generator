from split_links import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType
from extract_markdown import extract_markdown_links, extract_markdown_images
import unittest

class Test_Split(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and another [2nd link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "2nd link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_empty_text(self):
        node1 = TextNode("",TextType.TEXT)
        node2 = TextNode("this isn't empty", TextType.TEXT)
        new_nodes = split_nodes_link([node1,node2])
        self.assertListEqual(
            [node2],
            new_nodes,
        )
    
    def test_empty_link(self):
        node = TextNode(
            "This is text without a link [](), with only an anchor [2nd link]() and with only url [](www.url.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text without a link ", TextType.TEXT),
                TextNode(", with only an anchor ", TextType.TEXT),
                TextNode(" and with only url ", TextType.TEXT),
            ],
            new_nodes,
        )
    
    def test_empty_image(self):
        node = TextNode(
            "This is text without an image ![](), with only an alt ![alt text]() and with only url ![](www.url.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text without an image ", TextType.TEXT),
                TextNode(", with only an alt ", TextType.TEXT),
                TextNode(" and with only url ", TextType.TEXT),
            ],
            new_nodes,
        )
    
    def test_image_with_link(self):
        node = TextNode(
            "This is text with an image ![image](www.image.com) and link [url](www.link.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an image ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "www.image.com"),
                TextNode(" and link [url](www.link.com)", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_link_with_image(self):
        node = TextNode(
            "This is text with an image ![image](www.image.com) and link [url](www.link.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an image ![image](www.image.com) and link ", TextType.TEXT),
                TextNode("url", TextType.LINK, "www.link.com"),
            ],
            new_nodes,
        )
    
    def test_chain(self):
        node = TextNode(
            "This is text with an image ![image](www.image.com) and link [url](www.link.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        new_nodes = split_nodes_image(new_nodes)
        self.assertListEqual(
            [
                TextNode("This is text with an image ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "www.image.com"),
                TextNode(" and link ", TextType.TEXT),
                TextNode("url", TextType.LINK, "www.link.com"),
            ],
            new_nodes,
        )

    def test_multiple_nodes(self):
        node1 = TextNode(
        "Check this out ![image1](http://image1.com) or visit [site1](http://site1.com). Here's another ![image2](http://image2.com) and this [site2](http://site2.com). Plain text here.",
        TextType.TEXT
        )
        node2 = TextNode(
            "This is text with an image ![image](www.image.com) and link [url](www.link.com)",
            TextType.TEXT,
        )
        node3 = TextNode("abc", TextType.ITALIC)
        node4 = TextNode("this has **bold** text", TextType.BOLD)
        
        new_nodes = split_nodes_link([node1, node2, node3, node4])
        new_nodes = split_nodes_image(new_nodes)
        self.assertListEqual(
            [
                TextNode("Check this out ", TextType.TEXT),
                TextNode("image1", TextType.IMAGE, "http://image1.com"),
                TextNode(" or visit ", TextType.TEXT),
                TextNode("site1", TextType.LINK, "http://site1.com"),
                TextNode(". Here's another ", TextType.TEXT),
                TextNode("image2", TextType.IMAGE, "http://image2.com"),
                TextNode(" and this ", TextType.TEXT),
                TextNode("site2", TextType.LINK, "http://site2.com"),
                TextNode(". Plain text here.", TextType.TEXT),
                TextNode("This is text with an image ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "www.image.com"),
                TextNode(" and link ", TextType.TEXT),
                TextNode("url", TextType.LINK, "www.link.com"),
                TextNode("abc", TextType.ITALIC),
                TextNode("this has **bold** text", TextType.BOLD)
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()


