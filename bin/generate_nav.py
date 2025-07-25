#!/bin/python3
"""
generate_nav.py: Generate HTML navigation from a folder of HTML files
Author: Antonius Torode
Created: July 22, 2025
"""

from collections import defaultdict
from pathlib import Path
from typing import List
from bs4 import BeautifulSoup


def get_all_html_files(folder_path: str) -> List[str]:
    """
    Collect all HTML files in the given folder and subdirectories.

    Args:
        folder_path (str): Path to the folder.

    Returns:
        List[str]: List of relative paths to HTML files.
    """
    try:
        root_dir = Path(folder_path)
        if not root_dir.exists():
            raise FileNotFoundError(f"Folder '{folder_path}' does not exist.")
        if not root_dir.is_dir():
            raise NotADirectoryError(f"Path '{folder_path}' is not a directory.")

        return [str(path.relative_to(root_dir)) for path in root_dir.rglob('*.html')]

    except Exception as e:
        print(f"Error getting HTML files: {str(e)}")
        return []


def print_html_file_list(html_files: List[str]) -> None:
    """
    Prints the list of HTML files for debugging.

    Args:
        html_files (List[str]): List of HTML file paths.
    """
    print("HTML Files Found:")
    for file_path in html_files:
        print(f" - {file_path}")


def generate_nav_html_from_list(html_files: List[str]) -> str:
    """
    Generate nested HTML navigation structure from list of HTML file paths.

    Args:
        html_files (list[str]): List of relative HTML file paths.

    Returns:
        str: HTML string of the navigation structure.
    """

    def insert_path(structure, parts, full_path):
        for part in parts[:-1]:
            structure = structure.setdefault(part, {})
        display_name = parts[-1].replace('.html', '').replace('_', ' ').title()
        structure[parts[-1]] = {"display": display_name, "path": full_path}

    # Build a nested dictionary structure
    tree = {}
    for path in html_files:
        parts = path.split('/')
        insert_path(tree, parts, path)

    def build_html(structure) -> str:
        html = ''
        for key in sorted(structure.keys()):
            value = structure[key]
            if isinstance(value, dict) and 'path' in value:
                html += f'<li><a href="#" data-url="{value["path"]}">{value["display"]}</a></li>'
            else:
                html += f'<li><span class="folder">{key}</span>'
                html += '<ul>'
                html += build_html(value)
                html += '</ul></li>'
        return html

    html_output = '<div class="navbar"><ul class="tree">'
    html_output += '<li><a href="#" data-url="home.html">Home</a></li>'
    html_output += build_html(tree)
    html_output += '</ul></div>'
    return html_output


def format_html_pretty(html_str: str) -> str:
    """
    Formats raw HTML string with indentation for readability.

    Args:
        html_str (str): Raw HTML string.

    Returns:
        str: Pretty-formatted HTML string.
    """
    soup = BeautifulSoup(html_str, "html.parser")
    return soup.prettify()


def get_full_html_nav_block(input_folder):
    """
    Generate a fully formatted HTML navigation block from HTML files in a folder.

    Args:
        input_folder (str): Path to the folder containing HTML files.

    Returns:
        str: Indented and formatted HTML navigation block as a string.
    """

    html_files = get_all_html_files(input_folder)
    nav_html = generate_nav_html_from_list(html_files)
    formatted_html = format_html_pretty(nav_html)
    return formatted_html


def main():
    """
    Test the navigation generation.
    """
    print(get_full_html_nav_block("out_folder"))

if __name__ == "__main__":
    main()
