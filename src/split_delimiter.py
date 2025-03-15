from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if not isinstance(old_nodes, list):
        raise Exception("please input a list of nodes into old_nodes")
    if delimiter not in ["**", "_", "`"]:
        raise Exception("invalid delimiter")
    if text_type not in [TextType.BOLD, TextType.ITALIC, TextType.CODE]:
        raise Exception("invalid text_type")
    new_nodes = []
    for node in old_nodes: 
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        
        if delimiter not in node.text:
            raise Exception("node without a delimiter found.") 
        
        count = node.text.count(delimiter)
        if count % 2 != 0:
            raise Exception("odd number of delimiters found.")

        split_text = node.text.split(delimiter)
        for i in range(split_text): 
            if split_text[0] == "": # first item is always "normal", do nothing if empty 
                continue
            elif i % 2 != 0: 
                new_node = TextNode(split_text[i], text_type)
            elif i % 2 == 0:
                new_node = TextNode(split_text[i], TextType.TEXT)
            new_nodes.append(new_node)
        
    return new_nodes



# example text: this is a **bold** text.
