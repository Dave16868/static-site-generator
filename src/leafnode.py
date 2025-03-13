from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    # tag and value are required. But value may be none.
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        
        if self.tag is None or self.tag.strip() == "":
            return self.value

        
        # to html wit tags and values without props
        if self.props == None:
            return f'<{self.tag}>{self.value}</{self.tag}>'

        # to html with tags, values, and props
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>' ###