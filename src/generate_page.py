from markdown_to_html_node import markdown_to_html_node
from parentnode import ParentNode
from extract_title import extract_title
import os
from pathlib import Path

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
    
def generate_pages_recursively(dir_path_content, template_path, dest_dir_path):
    print(f"checking if file '{dir_path_content}' exists...")
    if os.path.exists(dir_path_content):
        print(f"it exists! creating list of what's inside...")
        list_to_copy = os.listdir(dir_path_content)
        print(f"list of things to copy: {list_to_copy}")
        for item in list_to_copy:
            item_path = os.path.join(dir_path_content, item)
            print(f"checking if '{item_path}' is a file or directory...")
            is_file = os.path.isfile(item_path)
            if is_file and item_path.endswith('.md'):
                print(f"its a file!")
                copy_path = os.path.join(dest_dir_path, item.replace(".md", ".html"))
                print(f"Generating page from '{item_path}' to '{copy_path}' using '{template_path}'")
                with open(item_path, "r") as f:
                    markdown = f.read()
                with open(template_path, "r") as f:
                    template = f.read()
                
                title = extract_title(markdown)
                parent = markdown_to_html_node(markdown)
                HTML_string = parent.to_html()

                final_HTML = template.replace("{{ Title }}", title)
                final_HTML = final_HTML.replace("{{ Content }}", HTML_string)

                os.makedirs(os.path.dirname(copy_path), exist_ok=True)

                print(f"converting markdown from '{item_path}' into HTML in '{copy_path}'")
                with open(copy_path, "w") as f:
                    f.write(final_HTML)

            if not is_file:
                copy_path = os.path.join(dest_dir_path, item)
                print(f"its a directory! calling this function again with dir_path_content: '{item_path}' and dest_dir_path: '{copy_path}'")
                os.mkdir(copy_path)
                generate_pages_recursively(item_path, template_path, copy_path)
        print(f"Finished generating pages from {dir_path_content} to {dest_dir_path}.")
    else:
        raise ValueError(f"dir_path_content doesn't exist! : {dir_path_content}")
    
def generate_pages_recursively2(dir_path_content, template_path, dest_dir_path):
    content_path = Path(dir_path_content)
    template_path = Path(template_path)
    dest_path = Path(dest_dir_path)
    print(f"checking if file '{dir_path_content}' exists...")
    if content_path.exists():
        print(f"it exists! creating list of what's inside...")
        print(f"everything inside '{content_path}': {[str(path) for path in content_path.rglob('*')]}")
        for item in content_path.rglob("*"):
            rel_path = item.relative_to(content_path)
            print(f"for '{item}', relative path : '{rel_path}")
            print(f"checking if '{item}' is a markdown file")
            if item.is_file() and item.suffix == ".md":
                print("markdown file!")
                copy_path = dest_path / rel_path.with_suffix(".html")
                with open(item, "r") as f:
                    print("reading markdown")
                    markdown = f.read()
                with open(template_path, "r") as f:
                    print("reading template")
                    template = f.read()

                title = extract_title(markdown)
                parent = markdown_to_html_node(markdown)
                HTML_string = parent.to_html()

                final_HTML = template.replace("{{ Title }}", title)
                final_HTML = final_HTML.replace("{{ Content }}", HTML_string)

                copy_path.parent.mkdir(parents=True, exist_ok=True)

                print(f"converting markdown from '{item}' into HTML in '{copy_path}'")
                with open(copy_path, "w") as f:
                    f.write(final_HTML)
            if not item.is_file():
                print("directory!")
                new_dir_path = dest_path / rel_path
                generate_pages_recursively2(item, template_path, new_dir_path)
            if item.is_file() and item.suffix != ".md":
                print("non-markdown file found. Skipping...")
        print(f"Finished generating pages from {dir_path_content} to {dest_dir_path}.")
    else:
        raise ValueError(f"dir_path_content doesn't exist! : {dir_path_content}")
