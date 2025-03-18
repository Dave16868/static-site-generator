from markdown_to_blocks import markdown_to_blocks
from blocktype import block_to_block_type, BlockType


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown) # list of blocks, no whitespace in each block, just "\n" 
    for block in blocks:
        blocktype = block_to_block_type(block) # get blocktype

# need a helper function that bases the type of block, creates a html node
def blocktype_to_html_node(block, blocktype):
    if blocktype == BlockType.HEADING:

    if blocktype == BlockType.CODE:

    if blocktype == BlockType.QUOTE:

    if blocktype == BlockType.UNORDERED:

    if blocktype == BlockType.ORDERED:

    if blocktype == BlockType.PARAGRAPH: