from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if self.tag is None or self.tag.split() == "":
            raise ValueError("Parent needs a tag!")
        if self.children is None or self.children == []:
            raise ValueError("Parent needs children!")
        
        # will need to access a list of Html/leafnodes
        # for each item, if its a leaf node, will need to .to_html() it to concat string
        # if its html, will access children
    
        # ASSUMING PARENTNODE ONLY HAS LEAFNODES AS CHILDREN 
        leaf_string = ""
        for i in range(len(self.children)): # index 0 to 2 (3 children)
            leaf_string += self.children[i].to_html()
            # empty string is now concat with all 3 leafnodes
        return f'<{self.tag}>{leaf_string}</{self.tag}>'