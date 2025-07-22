#!/bin/python3

###########################################################################################
# GRIDDLE: 
# Author: Antonius Torode
# Created: July 21, 2025
# Description: TODO
###########################################################################################

import argparse

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

if __name__ == "__main__":
    main()
