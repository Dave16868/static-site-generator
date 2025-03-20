import re

def markdown_to_blocks(markdown):
    if re.search(r"^`{3}[^`]*`{3}$", markdown): # if is 1 code block
        return [markdown]
    blocks = markdown.split("\n\n")
    result = []
    for block in blocks:
        stripped_block = block.strip()
        filtered_block = re.sub(r" *\n *", "\n", stripped_block)
        if filtered_block != "":
            result.append(filtered_block)
    return result