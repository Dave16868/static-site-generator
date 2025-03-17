from textnode import TextNode, TextType
from extract_markdown import extract_markdown_links, extract_markdown_images

def split_nodes_image(old_nodes):
    if not isinstance(old_nodes, list):
        raise TypeError("please input a list of nodes into old_nodes")
    new_nodes = []
    for node in old_nodes: 
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        if node.text == "":
            continue
        extracted_images = extract_markdown_images(node.text) # list of tuples
        if extracted_images == []:
            new_nodes.append(node)
            continue
        
        remaining_text = node.text
        for alt,url in extracted_images:
            remaining_text = remaining_text.split(f"![{alt}]({url})", 1)
            before = remaining_text[0]
            remaining_text = remaining_text[1]
            if before != "":
                new_nodes.append(TextNode(before, TextType.TEXT))
            if alt != "" and url != "": # IF EITHER ALT TEXT OR URL IS EMPTY STRING, IT'S REMOVED FROM NODES TO BE CONVERTED TO HTML
                new_nodes.append(TextNode(alt, TextType.IMAGE, url)) 
            if extract_markdown_images(remaining_text) == [] and remaining_text != "":
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    if not isinstance(old_nodes, list):
        raise TypeError("please input a list of nodes into old_nodes")
    new_nodes = []
    for node in old_nodes: 
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        if node.text == "":
            continue
        extracted_links = extract_markdown_links(node.text) # list of tuples
        if extracted_links == []:
            new_nodes.append(node)
            continue
        
        remaining_text = node.text
        for anchor,url in extracted_links:
            remaining_text = remaining_text.split(f"[{anchor}]({url})", 1)
            before = remaining_text[0]
            remaining_text = remaining_text[1]
            if before != "":
                new_nodes.append(TextNode(before, TextType.TEXT))
            if anchor != "" and url != "":
                new_nodes.append(TextNode(anchor, TextType.LINK, url))
            if extract_markdown_links(remaining_text) == [] and remaining_text != "":
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes
            