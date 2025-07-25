#!/bin/python3

"""
griddle_utils.py

This file contains various standalone methods and tools used by the griddle system. To use
this file, simple import it and call the needed methods.

Many of the methods were taken and/or adapted from: 
    https://github.com/torodean/DnD/blob/main/mmorpdnd.py
"""
import os
import subprocess
import shutil

def output_text(text, option="text"):
    """
    Print text to the console in a specified color using ANSI escape codes.

    Args:
        text (str): The text to be printed.
        option (str, optional): The color option for the text. Valid options are "text" (default, no color), 
            "warning" (yellow), "error" (red), "note" (blue), "success" (green), "command" (cyan), 
            "test" (magenta), and "program" (orange). Defaults to "text". Invalid options result in uncolored text.

    Returns:
        None

    Note:
        This function uses ANSI escape codes for color formatting. Colors may not display correctly 
        in all environments (e.g., some IDEs or Windows terminals without ANSI support).
    """
    color_codes = {
        "text": "\033[0m",      # Reset color
        "warning": "\033[93m",  # Yellow - Warning text
        "error": "\033[91m",    # Red - Error text
        "note": "\033[94m",     # Blue - Notes or program information
        "success": "\033[92m",  # Green - Success text
        "command": "\033[36m",  # Cyan - Command output text
        "test": "\033[35m",     # Magenta - Testing
        "program": "\033[38;5;208m"  # Orange - Program-specific output
    }
    
    text = str(text)  # Ensure text is a string
    
    if option == "error":
        if "error" not in text.lower():
            text = f"ERROR: {text}"
    elif option == "warning":
        if "error" not in text.lower():
            text = f"WARNING: {text}"
    
    if option in color_codes:
        color_code = color_codes[option]
        reset_code = color_codes["text"]
        print(f"{color_code}{text}{reset_code}")
    else:
        print(text)
        

def find_all_files_with_extensions(extensions, directory=".", excludes=None):
    """
    Finds all files with given extensions inside of a directory and includes the corresponding Git URL.

    Args:
        extensions (list of str): File extensions to include (e.g., ["md", "adoc", "txt"]).
        directory (str): Root directory to start searching from. Defaults to the current directory.
        excludes (list of str, optional): Substrings to filter out matching file paths. Defaults to an empty list.

    Returns:
        list of dict: Each dictionary contains:
            - 'name_no_ext': Filename without extension
            - 'name_with_ext': Full filename with extension
            - 'full_path': Absolute file path on disk
            - 'url': Git URL pointing to the file in the current branch    """
    if excludes is None:
        excludes = []
        
    repo_root = subprocess.check_output(['git', 'rev-parse', '--show-toplevel']).decode().strip()
    remote_url = subprocess.check_output(['git', 'config', '--get', 'remote.origin.url']).decode().strip()
    branch = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).decode().strip()

    if remote_url.endswith('.git'):
        remote_url = remote_url[:-4]
    if remote_url.startswith("git@"):
        remote_url = remote_url.replace(":", "/").replace("git@", "https://")

    matched_files = []
    for root, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(root, filename)

            if any(exclude in file_path for exclude in excludes):
                continue

            ext = os.path.splitext(filename)[1].lstrip('.').lower()
            if ext in extensions:
                rel_path = os.path.relpath(file_path, repo_root)
                file_url = f"{remote_url}/blob/{branch}/{rel_path}".replace("\\", "/")                
                name_no_ext = os.path.splitext(filename)[0]
                matched_files.append({
                    'name_no_ext': name_no_ext,
                    'name_with_ext': filename,
                    'full_path': file_path,                    
                    'url': file_url
                })
    return matched_files


def generate_nav_html(folder_path: str) -> str:
    """
    Generate HTML navigation structure from HTML files in the given folder.
    
    Args:
        folder_path (str): Path to the folder containing HTML files.
    
    Returns:
        str: HTML string with the navigation structure, without indentation.
    """
    try:
        root_dir = Path(folder_path)
        if not root_dir.exists():
            raise FileNotFoundError(f"Folder '{folder_path}' does not exist.")
        if not root_dir.is_dir():
            raise NotADirectoryError(f"Path '{folder_path}' is not a directory.")

        nav_html = '<div class="navbar"><ul class="tree"><li><a href="#" data-url="home.html">Home</a></li>'

        folder_structure = {}
        for html_file in root_dir.rglob('*.html'):
            rel_path = html_file.relative_to(root_dir)
            parts = rel_path.parts
            current = folder_structure
            for part in parts[:-1]:
                current = current.setdefault(part, {})
            current[parts[-1]] = rel_path.as_posix()

        def build_ul(structure: dict) -> str:
            html = '<ul>'
            for name, content in sorted(structure.items()):
                if isinstance(content, dict):
                    html += f'<li><span class="folder">{name}</span>'
                    html += build_ul(content)
                    html += '</li>'
                else:
                    html += f'<li><a href="#" data-url="{content}">{name}</a></li>'
            html += '</ul>'
            return html

        nav_html += build_ul(folder_structure)
        nav_html += '</ul></div>'

        return nav_html

    except Exception as e:
        print(f"Error generating navigation HTML: {str(e)}")
        return ""


def ensure_path_exists(file_path):
    """
    Ensures that all directories in the given file path exist.
    
    Args:
        file_path (str): Full path to a file (including filename).
    """
    dir_path = os.path.dirname(file_path)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)


def replace_extension(file_path, new_ext):
    """
    Replace the file extension of a given file path.

    Args:
        file_path (str): Original file path.
        new_ext (str): New extension to apply (with or without leading dot).

    Returns:
        str: File path with the new extension.
    """
    base = os.path.splitext(file_path)[0]
    return f"{base}.{new_ext.lstrip('.')}"
    
    
def copy_folder(src_dir, dest_dir):
    """
    Copy an entire folder and its contents to a new location.

    Args:
        src_dir (str): Path to the source folder.
        dest_dir (str): Path to the destination folder.

    Raises:
        FileNotFoundError: If the source folder doesn't exist.
        FileExistsError: If the destination folder already exists.
        Exception: For other unexpected errors.
    """
    if not os.path.exists(src_dir):
        raise FileNotFoundError(f"Source folder '{src_dir}' does not exist.")

    if os.path.exists(dest_dir):
        raise FileExistsError(f"Destination folder '{dest_dir}' already exists.")

    shutil.copytree(src_dir, dest_dir)
    
    

def copy_folder_contents(src_dir, dest_dir):
    """
    Copy the contents of a folder into another folder.

    Args:
        src_dir (str): Path to the source folder.
        dest_dir (str): Path to the destination folder. Created if it doesn't exist.

    Raises:
        FileNotFoundError: If the source folder doesn't exist.
        Exception: For unexpected errors.
    """
    if not os.path.exists(src_dir):
        raise FileNotFoundError(f"Source folder '{src_dir}' does not exist.")

    os.makedirs(dest_dir, exist_ok=True)
    output_text(f"Copying contents from '{src_dir}' to '{dest_dir}'", "note")

    for item in os.listdir(src_dir):
        s = os.path.join(src_dir, item)
        d = os.path.join(dest_dir, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
            output_text(f"Copied directory '{s}' to '{d}'", "success")
        else:
            shutil.copy2(s, d)
            output_text(f"Copied file '{s}' to '{d}'", "success")

    output_text(f"Finished copying contents to '{dest_dir}'", "note")
