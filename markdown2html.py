#!/usr/bin/python3
"""script markdown2html.py that takes an argument 2 strings"""

import sys
import markdown2

def convert_markdown_to_html(input_file, output_file):
    """function that converts markdown file to html"""
    try:
        with open(input_file, 'r') as md_file:
            markdown_text = md_file.read()

        html_content = markdown2.markdown(markdown_text)

        with open(output_file, 'w') as html_file:
            html_file.write(html_content)

        return 0

    except FileNotFoundError:
        print("Missing {}".format(input_file), file=sys.stderr)

        return 1

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    exit_code = convert_markdown_to_html(input_file, output_file)
    sys.exit(exit_code)
