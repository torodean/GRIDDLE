#!/bin/python3
"""
html_tools.py

This file contains various tools and methods needed for use for processing html files.
"""


def replace_autogen_nav_section(file_path, replacement_str):
    """
    Replace the marker '<!-- AUTOGEN - NAVIGATION SECTION -->' in the file with replacement_str.

    Args:
        file_path (str): Path to the file to modify.
        replacement_str (str): String to replace the marker with.

    Raises:
        FileNotFoundError: If the file doesn't exist.
        Exception: For other errors.
    """
    marker = "<!-- AUTOGEN - NAVIGATION SECTION -->"

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if marker not in content:
        # Optional: raise error or just return
        return

    new_content = content.replace(marker, replacement_str)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
