#!/bin/python3

"""
GRIDDLE: Git Repository Indexing and Digital Documentation Linking Engine 
Author: Antonius Torode
Created: July 21, 2025
Description: A system designed to unify and streamline documentation across multiple Git repositories
"""

import argparse
import sys
import os

def parse_arguments() -> argparse.Namespace:
    """
    Parse command-line arguments for GRIDDLE.
    """
    parser = argparse.ArgumentParser(
        description="GRIDDLE: Process document files in a specified folder."
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output for detailed logging.'
    )
    parser.add_argument(
        '-d', '--debug',
        action='store_true',
        help='Enable debug mode for development and troubleshooting.'
    )
    parser.add_argument(
        '-i', '--input',
        required=True,
        type=str,
        help='Input folder containing document files.'
    )
    parser.add_argument(
        '-o', '--output',
        required=True,
        type=str,
        help='Output folder for processed files.'
    )
    return parser.parse_args()


def main():
    """
    Main function to run GRIDDLE.
    """
    args = parse_arguments()
    
    # Print parsed arguments for demonstration
    print(f"Verbose mode: {args.verbose}")
    print(f"Debug mode: {args.debug}")
    print(f"Input folder: {args.input}")
    print(f"Output folder: {args.output}")

    for root, dirs, files in os.walk(args.input):
        for filename in files:
            file_path = os.path.join(root, filename)
            full_path = os.path.abspath(file_path)
            name_no_ext = os.path.splitext(filename)[0]
            ext = os.path.splitext(filename)[1].lstrip('.')
            new_file = args.output + "/" + replace_extension(file_path, "html")
            #ensure_path_exists(new_file)
            
            #if "md" in ext:
            #    convert_md_to_html(file_path, new_file)
            #elif "adoc" in ext:
            #    convert_adoc_to_html(file_path, new_file)
            #elif "asciidoc" in ext:
            #    convert_asciidoc_to_html(file_path, new_file)

if __name__ == "__main__":
    main()
