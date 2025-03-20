from htmlnode import HTMLNode
from textnode import TextNode, TextType
from parentnode import ParentNode
from text_to_textnodes import text_to_textnodes
from text_to_html_node import text_node_to_html_node
from markdown_to_blocks import markdown_to_blocks
from blocktype import block_to_block_type, BlockType
import re


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown.strip()) # list of blocks, no whitespace in each block, just "\n" 
    blocknodes = []
    for block in blocks:
        blocktype = block_to_block_type(block) # get blocktype
        blocknode = blocktype_to_html_node(block, blocktype) # turn block to HTMLNode
        blocknodes.append(blocknode) # add to list of blocknodes
    parent = ParentNode("div", blocknodes)
    return parent



# helper #1 based on type of block, creates a html node
def blocktype_to_html_node(block, blocktype):
    if blocktype == BlockType.HEADING:
        block = remove_newline(block.strip())
        stripped_block = re.sub(r"^#{1,6} +(.*?)", r"\1",block)
        num_of_headings = block.count("#", 0, 6)
        return ParentNode(f"h{num_of_headings}", text_to_children(stripped_block))
    
    if blocktype == BlockType.CODE:
        stripped_block = re.sub(r"^``` *\n([\s\S]*?)```$", r"\1",block)
        code_node = TextNode(stripped_block, TextType.CODE)
        return ParentNode("pre", [text_node_to_html_node(code_node)])
    
    if blocktype == BlockType.QUOTE:
        block = remove_newline(block.strip())
        stripped_block = re.sub(r"> *(.*?)", r"\1", block)
        return ParentNode("blockquote", text_to_children(stripped_block))

    if blocktype == BlockType.UNORDERED:
        items = [item.strip()[2:] for item in block.split("\n")]
        li_nodes = []
        for item in items:
            li_node = ParentNode("li", text_to_children(item))
            li_nodes.append(li_node)

        return ParentNode("ul", li_nodes)

    if blocktype == BlockType.ORDERED:
        items = [item.strip()[3:] for item in block.split("\n")]
        li_nodes = []
        for item in items:
            li_node = ParentNode("li", text_to_children(item))
            li_nodes.append(li_node)

        return ParentNode("ol", li_nodes)

    if blocktype == BlockType.PARAGRAPH:
        block = remove_newline(block.strip())
        return ParentNode("p", text_to_children(block))

    else: 
        raise ValueError(f"blocktype_to_html_node: blocktype: \"{blocktype}\" doesn't match any known BlockTypes.")



# helper #2 converts text to list of textnodes, then to list of leafnodes. Supplements helper #1
def text_to_children(text): 
    textnodes = text_to_textnodes(text)
    children = []
    for node in textnodes:
        children.append(text_node_to_html_node(node))
    return children

# helper #3 remove "\n". supplements helper #1
def remove_newline(text):
    filtered_text = re.sub(r" *\n *", " ", text)
    return filtered_text