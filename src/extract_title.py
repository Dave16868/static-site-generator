from markdown_to_blocks import markdown_to_blocks
from blocktype import block_to_block_type, BlockType
from markdown_to_html_node import remove_newline, blocktype_to_html_node
import re

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown.strip())
    for block in blocks:
        block = block.strip()
        blocktype = block_to_block_type(block)
        if blocktype == BlockType.HEADING and block.count("#", 0, 1) == 1:
            block = remove_newline(block)
            stripped_block = re.sub(r"^#{1,6} +(.*?)", r"\1", block)
            return stripped_block
    raise Exception("no header found")

