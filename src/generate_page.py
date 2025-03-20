from markdown_to_html_node import markdown_to_html_node
from parentnode import ParentNode
from extract_title import extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r") as f:
        template = f.read()

    title = extract_title(markdown)

    parent = markdown_to_html_node(markdown)
    HTML_string = parent.to_html()

    final_HTML = template.replace("{{ Title }}", title)
    final_HTML = final_HTML.replace("{{ Content }}", HTML_string)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(final_HTML)
    
