import re

def extract_markdown_images(text):
    alt_url = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return alt_url

def extract_markdown_links(text):
    anchor_url = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return anchor_url
