from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if not isinstance(old_nodes, list):
        raise TypeError("please input a list of nodes into old_nodes")
    if delimiter not in {"**", "_", "`"}:
        raise ValueError("invalid delimiter")
    if text_type not in {TextType.BOLD, TextType.ITALIC, TextType.CODE}:
        raise TypeError("invalid text_type")
    delimiter_type = {"**": TextType.BOLD, "_": TextType.ITALIC, "`": TextType.CODE}
    if text_type != delimiter_type[delimiter]:
        raise ValueError("delimiter does not match text_type")
    new_nodes = []
    for node in old_nodes: 
        print("new node")
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        
        if delimiter not in node.text:
            new_nodes.append(node)
            continue
        
        count = node.text.count(delimiter)
        if count % 2 != 0:
            raise Exception("odd number of delimiters found.")

        split_text = node.text.split(delimiter)
        for i in range(len(split_text)): 
            print(f"this is split_text[i]: {split_text[i]}")
            if split_text[i] == "":
                print("this text is empty, continuing")
                continue
            elif i % 2 != 0: 
                new_node = TextNode(split_text[i], text_type)
            elif i % 2 == 0:
                new_node = TextNode(split_text[i], TextType.TEXT)
            new_nodes.append(new_node)
        
    return new_nodes



# example text: this is a **bold** text.
