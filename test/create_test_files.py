#!/bin/python3
# create_test_files.py: Generate a test folder structure with unique Markdown and AsciiDoc files
# Author: [Your Name]
# Created: July 21, 2025
# Description: Creates a test folder with directories, subdirectories, and random .md, .adoc, and .asciidoc files
# with unique content for testing purposes.

import os
import random
import string
import uuid
from pathlib import Path

def generate_unique_content(file_type: str, file_id: str) -> str:
    """
    Generate unique content for a given file type (md, adoc, or asciidoc) using a unique identifier.
    """
    # Generate random title and paragraphs
    title = ''.join(random.choices(string.ascii_letters, k=10)) + f"_{file_id[:8]}"
    paragraphs = [
        ''.join(random.choices(string.ascii_letters + ' ', k=50)) + f" (ID: {file_id})"
        for _ in range(random.randint(2, 5))
    ]
    
    if file_type in ['adoc', 'asciidoc']:
        # AsciiDoc format with unique content
        content = f"= {title}\n\n"
        for para in paragraphs:
            content += f"{para}\n\n"
        content += f"== Section {file_id[:8]}\n\nUnique section content for {file_id}.\n"
    else:
        # Markdown format with unique content
        content = f"# {title}\n\n"
        for para in paragraphs:
            content += f"{para}\n\n"
        content += f"## Section {file_id[:8]}\n\nUnique section content for {file_id}.\n"
    
    return content

def create_file(file_path: Path, file_type: str) -> None:
    """
    Create a single file with unique content based on file type.
    """
    try:
        # Generate a unique identifier for this file
        file_id = str(uuid.uuid4())
        content = generate_unique_content(file_type, file_id)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Created file: {file_path}")
    except Exception as e:
        print(f"Error creating file {file_path}: {str(e)}")

def create_test_structure(root_folder: str) -> None:
    """
    Create test folder structure with directories, subdirectories, and unique files.
    """
    root = Path(root_folder)
    
    # Create root test folder
    root.mkdir(exist_ok=True)
    print(f"Created root folder: {root}")

    # Define directory structure
    directories = [
        ("docs", ["guides", "tutorials"]),
        ("notes", ["personal", "work"]),
        ("projects", ["proj1", "proj2"])
    ]

    # Supported file extensions
    file_extensions = ['.md', '.adoc', '.asciidoc']

    for dir_name, subdirs in directories:
        # Create main directory
        main_dir = root / dir_name
        main_dir.mkdir(exist_ok=True)
        print(f"Created directory: {main_dir}")

        # Create 1-3 files in main directory
        for _ in range(random.randint(1, 3)):
            ext = random.choice(file_extensions)
            file_name = f"file_{random.randint(1, 1000)}{ext}"
            create_file(main_dir / file_name, ext.lstrip('.'))

        # Create subdirectories
        for subdir in subdirs:
            sub_dir = main_dir / subdir
            sub_dir.mkdir(exist_ok=True)
            print(f"Created subdirectory: {sub_dir}")

            # Create 1-3 files in each subdirectory
            for _ in range(random.randint(1, 3)):
                ext = random.choice(file_extensions)
                file_name = f"file_{random.randint(1, 1000)}{ext}"
                create_file(sub_dir / file_name, ext.lstrip('.'))

def main():
    """
    Main function to set up test folder structure with unique files.
    """
    test_folder = "test_folder"
    try:
        create_test_structure(test_folder)
        print(f"Successfully created test structure in {test_folder}")
    except Exception as e:
        print(f"Error creating test structure: {str(e)}")

if __name__ == "__main__":
    main()
