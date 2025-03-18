from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED = "unordered_list"
    ORDERED = "ordered_list"
    

def block_to_block_type(markdown):
    md = markdown.strip()
    if len(md.split("\n\n")) > 1:
        raise ValueError("please input only 1 block")

    if re.search(r"^#{1,6} [^\n]+", md):
        return BlockType.HEADING
    
    if re.search(r"^`{3}[^`]*`{3}$", md):
        return BlockType.CODE
    
    if all(re.fullmatch(r"^>.*", line) for line in md.splitlines()):
        return BlockType.QUOTE
    
    if all(re.fullmatch(r"^\s*-\s+.*", line) for line in md.splitlines()):
        return BlockType.UNORDERED
    
    if all(re.fullmatch(r"^\d+\.\s+.*", line) for line in md.splitlines()):
        for i, line in enumerate(md.splitlines(), 1):
            if not line.startswith(f"{i}. "):
                raise ValueError("ordered list is not ordered properly!")
        return BlockType.ORDERED
    
    else: 
        return BlockType.PARAGRAPH