import shutil
import os
from recursive_copier import recursive_copier
from generate_page import generate_page, generate_pages_recursively, generate_pages_recursively2


def main():
    if os.path.exists("public"):
        shutil.rmtree("public")
    os.mkdir("public")
    recursive_copier("static", "public")
    generate_pages_recursively2("content", "template.html", "public")

main()
