import shutil
import os
from recursive_copier import recursive_copier
from generate_page import generate_page, generate_pages_recursively, generate_pages_recursively2
import sys

basepath = "/"
if len(sys.argv) > 1:
    basepath = sys.argv[1]
print(f"using basepath: {basepath}")

def main():
    if os.path.exists("docs"):
        shutil.rmtree("docs")
    os.mkdir("docs")
    recursive_copier("static", "docs")
    generate_pages_recursively2("content", "template.html", "docs", basepath)

main()
