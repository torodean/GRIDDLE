#!/bin/python3
"""
pdf_to_html.py

Generates an HTML page that embeds a PDF for in-browser viewing.
"""

from .griddle_utils import output_text
import os

def convert_pdf_to_html(pdf_path, output_html):
    try:
        if not os.path.exists(pdf_path):
            output_text(f"Error: PDF file '{pdf_path}' not found.", "error")
            return

        if not pdf_path.lower().endswith(".pdf"):
            output_text("Warning: File does not have a .pdf extension.", "warning")

        pdf_filename = os.path.basename(pdf_path)

        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{pdf_filename}</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
        }}
        iframe {{
            width: 100%;
            height: 100vh;
            border: none;
        }}
    </style>
</head>
<body>
    <iframe src="{pdf_filename}" type="application/pdf"></iframe>
</body>
</html>
"""

        with open(output_html, 'w', encoding='utf-8') as f:
            f.write(html_content)

        output_text(f"HTML viewer for '{pdf_path}' saved to '{output_html}'", "success")

    except Exception as e:
        output_text(f"An error occurred: {str(e)}", "error")
