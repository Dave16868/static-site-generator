from textnode import TextNode, TextType
from split_links import split_nodes_image, split_nodes_link
from split_delimiter import split_nodes_delimiter


def text_to_textnodes(text):
    first_node = TextNode(text, TextType.TEXT)
    nodes = [first_node]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    return nodes

