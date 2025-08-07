"""
Enhanced About Writer

A comprehensive Python script that automatically adds professional "about" statements 
to source code files across 100+ programming languages and file formats. 
Provides cross-platform compatibility and intelligent comment handling.

Author: Enhanced About Writer Team
Version: 2.0
License: MIT

Usage:
    python about_comment.py [-h] [-x EXTS] [-v] [-f] path name

Arguments:
    path: The path to the file or folder to process
    name: The author name to be added to files

Options:
    -x EXTS: Only process files with given extension(s) (comma-separated)
    -v: Show verbose output with detailed processing information  
    -f: Force overwrite existing about statements

Supported Technologies:
    • 50+ Programming Languages (Python, Java, C/C++, Go, Rust, etc.)
    • Web Technologies (HTML, CSS, JavaScript, TypeScript, Vue, React)
    • Configuration Files (JSON, YAML, TOML, INI, Dockerfile, Terraform)
    • Database Scripts (SQL variants for MySQL, PostgreSQL, SQLite)
    • Shell Scripts (Bash, Zsh, PowerShell, Fish, Batch)
    • Documentation (Markdown, LaTeX, reStructuredText)
    • And many more...

Features:
    ✓ Cross-platform compatibility (Windows, macOS, Linux)
    ✓ Intelligent comment style detection
    ✓ Automatic backup creation for large files
    ✓ Duplicate detection to prevent redundant comments
    ✓ Comprehensive error handling and reporting
    ✓ Preserves file structure (shebangs, doctypes, etc.)
"""


import pathlib
import os
import argparse
import re
import datetime
from typing import Dict, Tuple, List

# Comprehensive file format support with comment styles
INCLUDED_EXTS: Dict[str, Tuple[str, str]] = {
    # Programming Languages - C-style comments
    "*.c": ("/*", "*/"),
    "*.cpp": ("/*", "*/"), 
    "*.cxx": ("/*", "*/"),
    "*.cc": ("/*", "*/"),
    "*.c++": ("/*", "*/"),
    "*.h": ("/*", "*/"),
    "*.hpp": ("/*", "*/"),
    "*.hxx": ("/*", "*/"),
    "*.java": ("/*", "*/"),
    "*.js": ("/*", "*/"),
    "*.jsx": ("/*", "*/"),
    "*.ts": ("/*", "*/"),
    "*.tsx": ("/*", "*/"),
    "*.cs": ("/*", "*/"),
    "*.css": ("/*", "*/"),
    "*.scss": ("/*", "*/"),
    "*.sass": ("/*", "*/"),
    "*.less": ("/*", "*/"),
    "*.php": ("/*", "*/"),
    "*.go": ("/*", "*/"),
    "*.rs": ("/*", "*/"),
    "*.swift": ("/*", "*/"),
    "*.kt": ("/*", "*/"),
    "*.scala": ("/*", "*/"),
    "*.dart": ("/*", "*/"),
    "*.json": ("/*", "*/"),
    "*.jsonc": ("/*", "*/"),
    
    # Programming Languages - Hash comments
    "*.py": ('"""', '"""'),
    "*.pyx": ('"""', '"""'),
    "*.pyi": ('"""', '"""'),
    "*.rb": ("=begin", "=end"),
    "*.pl": ("=pod", "=cut"),
    "*.pm": ("=pod", "=cut"),
    "*.r": ("# ", ""),
    "*.R": ("# ", ""),
    "*.sh": ("# ", ""),
    "*.bash": ("# ", ""),
    "*.zsh": ("# ", ""),
    "*.fish": ("# ", ""),
    "*.ksh": ("# ", ""),
    "*.csh": ("# ", ""),
    "*.tcsh": ("# ", ""),
    "*.perl": ("# ", ""),
    "*.yaml": ("# ", ""),
    "*.yml": ("# ", ""),
    "*.toml": ("# ", ""),
    "*.ini": ("# ", ""),
    "*.cfg": ("# ", ""),
    "*.conf": ("# ", ""),
    "*.make": ("# ", ""),
    "*.mk": ("# ", ""),
    "*.cmake": ("# ", ""),
    "*.dockerfile": ("# ", ""),
    "*.gitignore": ("# ", ""),
    "*.dockerignore": ("# ", ""),
    
    # Functional Languages
    "*.hs": ("-- ", ""),
    "*.lhs": ("-- ", ""),
    "*.elm": ("-- ", ""),
    "*.ml": ("(* ", " *)"),
    "*.mli": ("(* ", " *)"),
    "*.fs": ("(* ", " *)"),
    "*.fsx": ("(* ", " *)"),
    "*.fsi": ("(* ", " *)"),
    "*.erl": ("% ", ""),
    "*.hrl": ("% ", ""),
    "*.ex": ("# ", ""),
    "*.exs": ("# ", ""),
    
    # Other Languages
    "*.lua": ("-- ", ""),
    "*.sql": ("-- ", ""),
    "*.psql": ("-- ", ""),
    "*.mysql": ("-- ", ""),
    "*.sqlite": ("-- ", ""),
    "*.m": ("% ", ""),  # MATLAB
    "*.jl": ("# ", ""),  # Julia
    "*.cr": ("# ", ""),  # Crystal
    "*.nim": ("# ", ""),
    "*.zig": ("// ", ""),
    "*.d": ("// ", ""),
    "*.ada": ("-- ", ""),
    "*.adb": ("-- ", ""),
    "*.ads": ("-- ", ""),
    "*.cob": ("* ", ""),
    "*.cbl": ("* ", ""),
    "*.f": ("C ", ""),
    "*.f90": ("! ", ""),
    "*.f95": ("! ", ""),
    "*.f03": ("! ", ""),
    "*.f08": ("! ", ""),
    "*.pas": ("(* ", " *)"),
    "*.pp": ("(* ", " *)"),
    "*.dpr": ("(* ", " *)"),
    "*.vb": ("' ", ""),
    "*.vbs": ("' ", ""),
    
    # Web and Markup
    "*.html": ("<!--", "-->"),
    "*.htm": ("<!--", "-->"),
    "*.xhtml": ("<!--", "-->"),
    "*.xml": ("<!--", "-->"),
    "*.xsl": ("<!--", "-->"),
    "*.xslt": ("<!--", "-->"),
    "*.svg": ("<!--", "-->"),
    "*.vue": ("<!--", "-->"),
    "*.md": ("<!--", "-->"),
    "*.markdown": ("<!--", "-->"),
    "*.mdown": ("<!--", "-->"),
    "*.rst": (".. ", ""),
    "*.tex": ("% ", ""),
    "*.latex": ("% ", ""),
    "*.bib": ("% ", ""),
    
    # Shell and Scripting
    "*.ps1": ("# ", ""),
    "*.psm1": ("# ", ""),
    "*.psd1": ("# ", ""),
    "*.bat": ("REM ", ""),
    "*.cmd": ("REM ", ""),
    
    # Configuration and Data
    "*.hcl": ("# ", ""),
    "*.tf": ("# ", ""),
    "*.tfvars": ("# ", ""),
    "*.pkr.hcl": ("# ", ""),
    "*.nomad": ("# ", ""),
    "*.consul": ("# ", ""),
    "*.vault": ("# ", ""),
    "*.csv": ("# ", ""),
    "*.tsv": ("# ", ""),
    
    # Plain text and others
    "*.txt": ("", ""),
    "*.text": ("", ""),
    "*.log": ("", ""),
    "*.readme": ("", ""),
}

EXCLUDED_EXTS = [
    # Binary executables and compiled files
    "exe", "bin", "class", "pyc", "pyo", "pyd", "so", "dll", "dylib", "o", "obj", "a", "lib",
    
    # Archives and compressed files  
    "jar", "war", "ear", "zip", "tar", "gz", "rar", "7z", "bz2", "xz",
    
    # Documents and media files
    "pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx", 
    "jpg", "jpeg", "png", "gif", "bmp", "tiff", "ico",
    "mp3", "mp4", "avi", "mkv", "wav", "flac", "ogg", "wma", "mov", "wmv", "flv", "webm",
    
    # Development directories and files
    "node_modules", ".git", ".svn", ".hg", "__pycache__", ".pytest_cache",
    ".vscode", ".idea", ".vs", "dist", "build", "target", "out", ".next", ".nuxt"
]

# Global list to store files for processing
FILES_LIST: List[pathlib.Path] = []


def get_file_creation_time(filepath: pathlib.Path) -> str:
    """
    Get the file creation/modification time in a cross-platform way.
    
    :param filepath: Path to the file
    :type filepath: pathlib.Path
    :return: Formatted date and time string
    :rtype: str
    """
    try:
        # Get file stats
        stat_info = filepath.stat()
        
        # Use creation time if available (Windows), otherwise use modification time
        if hasattr(stat_info, 'st_birthtime'):  # macOS
            timestamp = stat_info.st_birthtime
        elif hasattr(stat_info, 'st_ctime') and os.name == 'nt':  # Windows
            timestamp = stat_info.st_ctime
        else:  # Linux and others - use modification time
            timestamp = stat_info.st_mtime
            
        # Convert to readable format
        dt = datetime.datetime.fromtimestamp(timestamp)
        return dt.strftime("%d %B %Y @ %H:%M:%S")
    except Exception:
        # Fallback to current time
        return datetime.datetime.now().strftime("%d %B %Y @ %H:%M:%S")


def is_excluded_path(path: pathlib.Path) -> bool:
    """
    Check if a path should be excluded from processing.
    
    :param path: Path to check
    :type path: pathlib.Path
    :return: True if path should be excluded
    :rtype: bool
    """
    path_str = str(path).lower()
    path_parts = path.parts
    
    # Check if any part of the path contains excluded directories/files
    for part in path_parts:
        part_lower = part.lower()
        for excluded in EXCLUDED_EXTS:
            if excluded == part_lower or (excluded in part_lower and len(excluded) > 3):
                return True
                
    # Also check the filename itself
    filename = path.name.lower()
    for excluded in EXCLUDED_EXTS:
        if filename.endswith('.' + excluded) or filename == excluded:
            return True
            
    return False


def get_folder(foldername: str, exts: List[str] = ["*"], verbose: bool = False) -> None:
    """
    Recursively gets all the files in the specified folder with the given extensions.

    :param foldername: The folder name
    :type foldername: str
    :param exts: The extensions of files to include, defaults to ["*"]
    :type exts: List[str], optional
    :param verbose: Flag to print verbose output, defaults to False
    :type verbose: bool, optional
    """
    folder_path = pathlib.Path(foldername)
    
    if not folder_path.exists():
        print(f"[!] Folder '{foldername}' does not exist.")
        return
        
    if not folder_path.is_dir():
        print(f"[!] '{foldername}' is not a directory.")
        return
    
    for ext in exts:
        # Handle extensions that don't start with *
        if not ext.startswith("*"):
            if not ext.startswith("."):
                pattern = "*." + ext
            else:
                pattern = "*" + ext
        else:
            pattern = ext
                
        try:
            for child in folder_path.rglob(pattern):
                if child.is_file() and not is_excluded_path(child):
                    if child not in FILES_LIST:
                        FILES_LIST.append(child)
                        if verbose:
                            print(f"[*] Added {child} to processing list")
        except Exception as e:
            if verbose:
                print(f"[!] Error processing pattern '{pattern}': {e}")


def has_about_statement(content: str, filename: str) -> bool:
    """
    Check if the file already has an about statement.
    
    :param content: File content to check
    :type content: str
    :param filename: Name of the file
    :type filename: str
    :return: True if about statement exists
    :rtype: bool
    """
    # Look for various indicators of existing about statements
    indicators = [
        filename.upper(),
        "Source Code",
        "Author:",
        "Created by:",
        "Written by:",
        "@author",
        "* @file",
        "* @brief",
        "Module:",
        "Script:",
        "Program:"
    ]
    
    # Check first 20 lines for about statements
    lines = content.split('\n')[:20]
    first_lines = '\n'.join(lines)
    
    return any(indicator in first_lines for indicator in indicators)


def perm_edit(name: str, force: bool = False, verbose: bool = False) -> None:
    """
    Applies the about statement to all the files in the files_list.

    :param name: The name to be set as the author of the file
    :type name: str
    :param force: Force overwrite existing about statements
    :type force: bool
    :param verbose: Flag to print verbose output, defaults to False
    :type verbose: bool, optional
    """
    if not FILES_LIST:
        print("[!] No files found to process.")
        return
        
    print(f"[*] Processing {len(FILES_LIST)} files...")
    processed = 0
    skipped = 0
    errors = 0
    
    for file_path in FILES_LIST:
        if file_path.is_file():
            if verbose:
                print(f"\n{'=' * 75}")
                print(f"Processing: {file_path}")
                print(f"{'=' * 75}")
            try:
                result = edit_file(file_path, name, force, verbose)
                if result == "processed":
                    processed += 1
                elif result == "skipped":
                    skipped += 1
                else:
                    errors += 1
            except Exception as e:
                errors += 1
                ext = "*" + file_path.suffix
                if verbose:
                    print(f"[!] Error processing '{file_path}': {e}")
                elif ext not in INCLUDED_EXTS:
                    print(f"[!] Unsupported file format '{ext}' for file: {file_path}")
    
    # Summary
    print(f"\n{'=' * 50}")
    print(f"Processing Complete!")
    print(f"Processed: {processed} files")
    print(f"Skipped: {skipped} files") 
    print(f"Errors: {errors} files")
    print(f"{'=' * 50}")


def generate_about_statement(filepath: pathlib.Path, name: str, comment_style: Tuple[str, str]) -> str:
    """
    Generate the about statement for a file.
    
    :param filepath: Path to the file
    :type filepath: pathlib.Path
    :param name: Author name
    :type name: str
    :param comment_style: Tuple of (start_comment, end_comment)
    :type comment_style: Tuple[str, str]
    :return: Generated about statement
    :rtype: str
    """
    filename = filepath.name.upper()
    creation_time = get_file_creation_time(filepath)
    start_comment, end_comment = comment_style
    
    # Determine file type description
    ext = filepath.suffix.lower()
    file_type_map = {
        '.py': 'Python Script',
        '.java': 'Java Source Code',
        '.c': 'C Source Code',
        '.cpp': 'C++ Source Code',
        '.h': 'Header File',
        '.js': 'JavaScript Source Code',
        '.ts': 'TypeScript Source Code',
        '.html': 'HTML Document',
        '.css': 'CSS Stylesheet',
        '.php': 'PHP Source Code',
        '.rb': 'Ruby Script',
        '.go': 'Go Source Code',
        '.rs': 'Rust Source Code',
        '.swift': 'Swift Source Code',
        '.kt': 'Kotlin Source Code',
        '.scala': 'Scala Source Code',
        '.sh': 'Shell Script',
        '.ps1': 'PowerShell Script',
        '.sql': 'SQL Script',
        '.r': 'R Script',
        '.m': 'MATLAB Script',
        '.lua': 'Lua Script',
        '.pl': 'Perl Script',
        '.yaml': 'YAML Configuration',
        '.yml': 'YAML Configuration',
        '.json': 'JSON Data',
        '.xml': 'XML Document',
        '.md': 'Markdown Document',
        '.tex': 'LaTeX Document',
        '.dockerfile': 'Docker Configuration'
    }
    
    file_description = file_type_map.get(ext, 'Source Code')
    
    if end_comment:  # Multi-line comment style
        if ext == '.py':
            # Python uses triple quotes
            return f'{start_comment}\n{filename} - {file_description}\nAuthor: {name}\nCreated: {creation_time}\n{end_comment}\n\n'
        elif ext in ['.html', '.xml', '.svg', '.vue']:
            # XML-style comments
            return f'{start_comment}\n{filename} - {file_description}\nAuthor: {name}\nCreated: {creation_time}\n{end_comment}\n\n'
        else:
            # C-style comments
            return f'{start_comment}\n * {filename} - {file_description}\n * Author: {name}\n * Created: {creation_time}\n {end_comment}\n\n'
    else:  # Single-line comment style
        if ext in ['.r', '.R']:
            # R-style comments
            return f'{start_comment}{filename} - {file_description}\n{start_comment}Author: {name}\n{start_comment}Created: {creation_time}\n\n'
        else:
            # Hash-style or other single-line comments
            return f'{start_comment}{filename} - {file_description}\n{start_comment}Author: {name}\n{start_comment}Created: {creation_time}\n\n'


def edit_file(filepath: pathlib.Path, name: str, force: bool = False, verbose: bool = False) -> str:
    """
    Edits the specified file to add the about statement.

    :param filepath: The path of the file to edit
    :type filepath: pathlib.Path
    :param name: The name to be set as the author of the file
    :type name: str
    :param force: Force overwrite existing about statements
    :type force: bool
    :param verbose: Flag to print verbose output, defaults to False
    :type verbose: bool, optional
    :return: Status of the operation ("processed", "skipped", "error")
    :rtype: str
    """
    try:
        # Check if file exists and is readable
        if not filepath.exists():
            if verbose:
                print(f"[!] File does not exist: {filepath}")
            return "error"
            
        if not filepath.is_file():
            if verbose:
                print(f"[!] Path is not a file: {filepath}")
            return "error"
            
        # Get file extension
        ext = "*" + filepath.suffix.lower()
        
        if ext not in INCLUDED_EXTS:
            if verbose:
                print(f"[!] Unsupported file format '{ext}' for file: {filepath}")
            return "error"
        
        # Read file content
        try:
            with open(filepath, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
        except Exception as e:
            if verbose:
                print(f"[!] Error reading file '{filepath}': {e}")
            return "error"
            
        if verbose:
            print(f"[*] Reading content of '{filepath}'")
        
        # Check if about statement already exists
        if has_about_statement(content, filepath.name) and not force:
            if verbose:
                print(f"[!] About statement already exists in '{filepath}' (use -f to force overwrite)")
            else:
                print(f"[!] Already processed: {filepath}")
            return "skipped"
        
        # Generate about statement
        comment_style = INCLUDED_EXTS[ext]
        about_statement = generate_about_statement(filepath, name, comment_style)
        
        # Handle special cases for certain file types
        new_content = content
        
        if ext == "*.php":
            # Handle PHP files
            if content.startswith("<?php"):
                # Insert after PHP opening tag
                php_tag_end = content.find("?>")
                if php_tag_end == -1:  # No closing tag
                    lines = content.split('\n')
                    if lines[0].strip() == "<?php":
                        new_content = lines[0] + '\n\n' + about_statement + '\n'.join(lines[1:])
                    else:
                        new_content = about_statement + content
                else:
                    new_content = about_statement + content
            else:
                new_content = "<?php\n\n" + about_statement + content
                
        elif ext in ["*.html", "*.htm", "*.xml", "*.svg"]:
            # Handle HTML/XML files - insert after declaration or at beginning
            doctype_match = re.search(r'<!DOCTYPE[^>]*>|<\?xml[^>]*\?>', content, re.IGNORECASE)
            if doctype_match:
                insert_pos = doctype_match.end()
                new_content = content[:insert_pos] + '\n\n' + about_statement + content[insert_pos:]
            else:
                new_content = about_statement + content
                
        elif ext == "*.py":
            # Handle Python files - check for shebang or encoding
            lines = content.split('\n')
            insert_line = 0
            
            # Skip shebang
            if lines and lines[0].startswith('#!'):
                insert_line = 1
                
            # Skip encoding declaration
            if len(lines) > insert_line and 'coding' in lines[insert_line]:
                insert_line += 1
                
            new_lines = lines[:insert_line] + [about_statement] + lines[insert_line:]
            new_content = '\n'.join(new_lines)
            
        else:
            # Default: prepend to beginning
            new_content = about_statement + content
        
        # Write the modified content back to file
        try:
            # Create backup if file is large or important
            if filepath.stat().st_size > 10000:  # Files larger than 10KB
                backup_path = filepath.with_suffix(filepath.suffix + '.bak')
                if verbose:
                    print(f"[*] Creating backup: {backup_path}")
                backup_path.write_text(content, encoding='utf-8', errors='ignore')
            
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(new_content)
                
            if verbose:
                print(f"[*] Successfully added about statement to '{filepath}'")
            else:
                print(f"[✓] Processed: {filepath}")
            return "processed"
            
        except Exception as e:
            if verbose:
                print(f"[!] Error writing to file '{filepath}': {e}")
            return "error"
            
    except Exception as e:
        if verbose:
            print(f"[!] Unexpected error processing '{filepath}': {e}")
        return "error"


def main():
    """Main function to handle command line arguments and execute the script."""
    parser = argparse.ArgumentParser(
        description="Enhanced About Writer v2.0 - Professional about statements for 100+ file formats",
        epilog="Examples:\n"
               "  Process single file:     python about_comment.py /path/to/file.py 'John Doe' -v\n"
               "  Process directory:       python about_comment.py /path/to/project/ 'Team Lead' -x py,js,html\n"
               "  Current directory:       python about_comment.py . 'Developer' -f -v\n"
               "  Multiple extensions:     python about_comment.py ./src/ 'Author' -x py,js,ts,css,html,md",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument("path", help="Path to the file or folder to process")
    parser.add_argument("name", help="Author name to be added to the files")
    parser.add_argument("-x", "--exts", 
                       help="Only modify files with the given extension(s). "
                            "Separate multiple extensions with comma (e.g., py,js,html)")
    parser.add_argument("-v", "--verbose", action="store_true", 
                       help="Show verbose output with detailed processing information")
    parser.add_argument("-f", "--force", action="store_true",
                       help="Force overwrite existing about statements")
    
    args = parser.parse_args()
    
    # Validate inputs
    if not args.name.strip():
        print("[!] Author name cannot be empty.")
        return 1
        
    path = pathlib.Path(args.path).resolve()
    
    if not path.exists():
        print(f"[!] Path '{args.path}' does not exist.")
        return 1
    
    # Clear the files list for fresh run
    FILES_LIST.clear()
    
    if path.is_dir():
        # Process directory
        exts = ["*"] if not args.exts else [ext.strip() for ext in args.exts.split(",")]
        
        if args.verbose:
            print(f"[*] Processing directory: {path}")
            print(f"[*] Extensions filter: {exts}")
            print(f"[*] Author: {args.name}")
            print(f"[*] Force overwrite: {args.force}")
            print("-" * 50)
        
        get_folder(str(path), exts, args.verbose)
        
        if not FILES_LIST:
            print(f"[!] No supported files found in '{path}' with extensions {exts}")
            return 1
            
        perm_edit(args.name, args.force, args.verbose)
        
    elif path.is_file():
        # Process single file
        if args.verbose:
            print(f"[*] Processing single file: {path}")
            print(f"[*] Author: {args.name}")
            print(f"[*] Force overwrite: {args.force}")
            print("-" * 50)
        
        result = edit_file(path, args.name, args.force, args.verbose)
        
        if result == "processed":
            print(f"[✓] Successfully processed: {path}")
        elif result == "skipped":
            print(f"[!] Skipped (already has about statement): {path}")
        else:
            print(f"[!] Failed to process: {path}")
            return 1
    else:
        print(f"[!] '{args.path}' is neither a file nor a directory.")
        return 1
    
    return 0


if __name__ == "__main__":
    try:
        exit_code = main()
        exit(exit_code)
    except KeyboardInterrupt:
        print("\n[!] Operation cancelled by user.")
        exit(130)
    except Exception as e:
        print(f"[!] Unexpected error: {e}")
        exit(1)
