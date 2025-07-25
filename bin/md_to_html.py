#!/bin/python3
"""
md_to_html.py

This file contains various tools and methods needed for use in converting md (markdown)
files to html. To use this file, simple import it and call the needed methods.
"""

from .griddle_utils import output_text
import markdown
import sys
import os

def convert_md_to_html(input_file, output_file):
    try:
        # Check if input file exists
        if not os.path.exists(input_file):
            output_text(f"Error: Input file '{input_file}' does not exist.", "error")
            return
        
        # Check if input file has .md extension
        if not input_file.lower().endswith('.md'):
            output_text("Warning: Input file does not have a .md extension.", "warning")
        
        # Read the Markdown file
        with open(input_file, 'r', encoding='utf-8') as md_file:
            md_content = md_file.read()
        
        # Convert Markdown to HTML
        html_content = markdown.markdown(md_content, extensions=['extra', 'codehilite', 'toc'])
        
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
        
        output_text(f"Successfully converted '{input_file}' to '{output_file}'", "success")
        
    except Exception as e:
        output_text(f"An error occurred: {str(e)}", "error")
