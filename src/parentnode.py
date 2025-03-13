from htmlnode import HTMLNode
from leafnode import LeafNode

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


        html_string = ""
        for child in self.children:
            if isinstance(child, LeafNode):
                html_string += child.to_html()
            elif isinstance(child, ParentNode):
                html_string += child.to_html()
            else:
                raise ValueError("invalid node found in children")
        return f"<{self.tag}{self.props_to_html()}>{html_string}</{self.tag}>" 
