"""
About Writer

The About Writer is a Python script that adds an "about" statement to the specified files.
It is designed to help add metadata information, such as author and timestamp, to source code files.
The script supports various file formats and can recursively process files in a specified folder.

Author: ZION

Usage:
    python about_writer.py [-h] [-x EXTS] [-v] path name

Arguments:
    path: The path to the file or folder.
    name: The name to be set as the author of the file.

Options:
    -x EXTS: Only modify files with the given extension(s). Separate multiple extensions with a comma (,).
    -v: Show verbose output.

Supported File Formats:
    - Python (.py)
    - Java (.java)
    - C (.c)
    - PHP (.php)
    - HTML (.html)
    - JSON (.json)
    - CSS (.css)
    - JavaScript (.js)
    - Perl (.pl)
    - Shell Script (.sh)
    - C++ (.cpp)
    - C# (.cs)
    - R (.r)
    - Text (.txt)
"""


import subprocess
import pathlib
import os
import argparse
import re

INCLUDED_EXTS = {
    "*.py": ("\"\"\"", "\"\"\""),
    "*.java": ("/*", "*/"),
    "*.c": ("/*", "*/"),
    "*.php": ("/*", "*/"),
    "*.html": ("<!--", "-->"),
    "*.json": ("/*", "*/"),
    "*.css": ("/*", "*/"),
    "*.js": ("/*", "*/"),
    "*.pl": ("=pod", "=cut"),
    "*.sh": (": '", "'"),
    "*.cpp": ("/*", "*/"),
    "*.cs": ("/*", "*/"),
    "*.r": ("#", ""),
    "*.txt": ("", ""),
}

EXCLUDED_EXTS = ["exe", "class", "pickle"]
FILES_LIST = []


def get_folder(foldername, exts=["*"], verbose=False):
    """
    Recursively gets all the files in the specified folder with the given extensions.

    :param foldername: The folder name
    :type foldername: str
    :param exts: The extensions of files to include, defaults to ["*"]
    :type exts: list, optional
    :param verbose: Flag to print verbose output, defaults to False
    :type verbose: bool, optional
    """
    for i in exts:
        for child in pathlib.Path(foldername).rglob(i):
            if child not in FILES_LIST and child.is_file():
                FILES_LIST.append(child)
                print(f"[*] Appended {child} to files_list") if verbose else print("")
            elif child.is_dir():
                get_folder(child, exts, verbose)


def perm_edit(name, verbose=False):
    """
    Applies the about statement to all the files in the files_list.

    :param name: The name to be set as the author of the file
    :type name: str
    :param verbose: Flag to print verbose output, defaults to False
    :type verbose: bool, optional
    """
    for child in FILES_LIST:
        if child.is_file():
            print(str(child).center(75, "="))
            try:
                edit_file(child, name, verbose)
            except Exception:
                ext = "*." + str(child).suffix
                print(f"[!] Couldn't write to \"{child}\" because file format \"{ext}\" is not supported") if verbose else print("")


def edit_file(filepath, name, verbose=False):
    """
    Edits the specified file to add the about statement.

    :param filepath: The path of the file to edit
    :type filepath: str
    :param name: The name to be set as the author of the file
    :type name: str
    :param verbose: Flag to print verbose output, defaults to False
    :type verbose: bool, optional
    """
    if os.sep in str(filepath):
        filepath = str(filepath).replace(os.sep, os.altsep)
    filename = str(filepath).split(os.altsep)[-1].upper()
    with open(filepath, "r") as file:
        content = file.read()
    print(f"[*] Reading content of \"{filepath}\"") if verbose else print("")
    if filename not in content:
        get_date_time_info = subprocess.run(["dir", "/Tc", filepath], shell=True, capture_output=True, text=True).stdout
        date = re.search(r"\r\n(\d+\W\w+\W\d+)", get_date_time_info)
        time = re.search(r"(\d+\W\d+\W+\w+)", get_date_time_info)
        ext = "*." + str(filepath).split(os.altsep)[-1].split(".")[-1]
        if ext not in INCLUDED_EXTS.keys():
            print(f"[!] Couldn't write to \"{filepath}\" because file format \"{ext}\" is not supported")
        else:
            for i in INCLUDED_EXTS:
                if i == ext:
                    print(f"[*] Writing about statement to \"{filepath}\"") if verbose else print("")
                    if "<DOCTYPE html>".lower() not in content.lower() and ext != "*.r":
                        text = f"{INCLUDED_EXTS[i][0]}\n{filename} Source Code\n{name}, {date[0].strip()} @ {time[0].strip()}.\n{INCLUDED_EXTS[i][-1]}\n\n\n"
                    elif ext == "*.r":
                        text = f"{INCLUDED_EXTS['*.r'][0]}\t{filename} Source Code\n{INCLUDED_EXTS['*.r'][0]}\t{name}, {date[0].strip()} @ {time[0].strip()}.\n\n\n"
                    else:
                        text = f"{INCLUDED_EXTS['*.html'][0]}\n{filename} Source Code\n{name}, {date[0].strip()} @ {time[0].strip()}.\n{INCLUDED_EXTS['*.html'][-1]}\n\n\n"
                    with open(filepath, "r", encoding="utf-8") as file:
                        if ext == "*.php":
                            if "<DOCTYPE html>".lower() not in content.lower():
                                file.seek(5)
                        content = file.read()
                    with open(filepath, "w", encoding="utf-8") as file:
                        if ext == "*.php":
                            if "<DOCTYPE html>".lower() not in content.lower():
                                text = "<?php\n" + text
                        content = text + content
                        file.write(content)
                    print(f"[*] Finished writing about statement to \"{filepath}\"") if verbose else print("")
    else:
        print(f"[!] About statement has already been written to \"{filepath}\"")


def main():
    parser = argparse.ArgumentParser(description="About Writer")
    parser.add_argument("path", help="Path to the file or folder")
    parser.add_argument("name", help="Value to be set as the author of the file")
    parser.add_argument("-x", "--exts", help="Only modify files with the given extension(s). Separate multiple extensions with comma (,)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Show verbose output")
    args = parser.parse_args()

    if os.path.isdir(args.path):
        exts = ["*"] if not args.exts else args.exts.split(",")
        get_folder(foldername=args.path, exts=exts, verbose=args.verbose)
        perm_edit(name=args.name, verbose=args.verbose)
    elif os.path.isfile(args.path):
        edit_file(filepath=args.path, name=args.name, verbose=args.verbose)


if __name__ == "__main__":
    main()
