#!/bin/python3
"""
adoc_to_html.py

This file contains various tools and methods needed for use in converting adoc (asciidoc)
files to html. To use this file, simple import it and call the needed methods.
"""

import asciidoc
import os

def convert_adoc_to_html(input_file, output_file):
    """
    Convert an AsciiDoc (.adoc) file to HTML.
    """
    try:
        # Check if input file exists
        if not os.path.exists(input_file):
            print(f"Error: Input file '{input_file}' does not exist.")
            return
        
        # Check if input file has .adoc extension
        if not input_file.lower().endswith('.adoc'):
            print("Warning: Input file does not have a .adoc extension.")
        
        # Read the AsciiDoc file
        with open(input_file, 'r', encoding='utf-8') as adoc_file:
            adoc_content = adoc_file.read()
        
        # Convert AsciiDoc to HTML
        html_content = asciidoc.convert(adoc_content, backend='html5')
        
        # Create basic HTML template
        html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{os.path.basename(input_file)}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            line-height: 1.6;
        }}
        pre {{
            background: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
        }}
        code {{
            background: #f4f4f4;
            padding: 2px 4px;
            border-radius: 3px;
        }}
    </style>
</head>
<body>
    {html_content}
</body>
</html>
"""
        
        # Write to output HTML file
        with open(output_file, 'w', encoding='utf-8') as html_file:
            html_file.write(html_template)
        
        print(f"Successfully converted '{input_file}' to '{output_file}'")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def convert_asciidoc_to_html(input_file, output_file):
    """
    Convert an AsciiDoc (.asciidoc) file to HTML.
    """
    try:
        # Check if input file exists
        if not os.path.exists(input_file):
            print(f"Error: Input file '{input_file}' does not exist.")
            return
        
        # Check if input file has .asciidoc extension
        if not input_file.lower().endswith('.asciidoc'):
            print("Warning: Input file does not have a .asciidoc extension.")
        
        # Read the AsciiDoc file
        with open(input_file, 'r', encoding='utf-8') as asciidoc_file:
            asciidoc_content = asciidoc_file.read()
        
        # Convert AsciiDoc to HTML
        html_content = asciidoc.convert(asciidoc_content, backend='html5')
        
        # Create basic HTML template
        html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{os.path.basename(input_file)}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            line-height: 1.6;
        }}
        pre {{
            background: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
        }}
        code {{
            background: #f4f4f4;
            padding: 2px 4px;
            border-radius: 3px;
        }}
    </style>
</head>
<body>
    {html_content}
</body>
</html>
"""
        
        # Write to output HTML file
        with open(output_file, 'w', encoding='utf-8') as html_file:
            html_file.write(html_template)
        
        print(f"Successfully converted '{input_file}' to '{output_file}'")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
