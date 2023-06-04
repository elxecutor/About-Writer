# About Writer

The About Writer is a Python script that adds an "about" statement to the specified files. It is designed to help add metadata information, such as author and timestamp, to source code files. The script supports various file formats and can recursively process files in a specified folder.

## Features

- Recursively gets all the files in the specified folder with the given extensions.
- Applies the about statement to all the files in the files_list.
- Edits the specified file to add the about statement.

## Usage

```
python about_writer.py [-h] [-x EXTS] [-v] path name
```

- `path`: The path to the file or folder.
- `name`: The name to be set as the author of the file.
- `-x EXTS` (optional): Only modify files with the given extension(s). Separate multiple extensions with a comma (,).
- `-v` (optional): Show verbose output.

**Note:** The script requires Python 3.x to run.

## Examples

- Process a single file:

  ```
  python about_writer.py /path/to/file.py JohnDoe -v
  ```

- Process a folder recursively:

  ```
  python about_writer.py /path/to/folder/ JohnDoe -x .py,.java -v
  ```

## Supported File Formats

The script supports the following file formats:

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
