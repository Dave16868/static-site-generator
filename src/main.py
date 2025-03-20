import shutil
import os
from recursive_copier import recursive_copier
from generate_page import generate_page

def main():
    if os.path.exists("public"):
        shutil.rmtree("public")
    os.mkdir("public")
    recursive_copier("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")
    generate_page("content/blog/glorfindel/index.md", "template.html", "public/blog/glorfindel/index.html")
    generate_page("content/blog/majesty/index.md", "template.html", "public/blog/majesty/index.html")
    generate_page("content/blog/tom/index.md", "template.html", "public/blog/tom/index.html")
    generate_page("content/contact/index.md", "template.html", "public/contact/index.html")

main()
