# Enhanced About Writer v2.0

A comprehensive Python script that automatically adds professional "about" statements to source code files across **100+ programming languages and file formats**. Features cross-platform compatibility, intelligent comment handling, and robust error management.

## 🎯 Key Features

- **Universal Support**: 100+ file formats including all major programming languages, web technologies, configuration files, and documentation formats
- **Cross-Platform**: Works seamlessly on Windows, macOS, and Linux  
- **Smart Comment Detection**: Uses appropriate comment styles for each file type
- **Duplicate Prevention**: Intelligently detects existing about statements
- **Safe Processing**: Creates automatic backups for large files
- **Batch Processing**: Recursively processes entire directory trees
- **Flexible Filtering**: Process specific file types with extension filters
- **Professional Output**: Clean, consistent about statements with author and timestamp

## 🚀 Quick Start

### Installation
```bash
# Clone the repository
git clone https://github.com/elxecutor/About-Writer.git
cd About-Writer

# No additional dependencies required - uses Python standard library only!
```

### Basic Usage
```bash
# Process a single file
python about_comment.py /path/to/file.py "John Doe"

# Process a directory with specific extensions  
python about_comment.py ./project/ "Jane Smith" -x py,js,html,css

## 📁 Project Structure

```
About-Writer/
├── about_comment.py    # Main script with all functionality
├── README.md          # This documentation  
├── LICENSE           # MIT license
├── .gitignore       # Git ignore patterns
└── .git/           # Git repository data
```

The codebase is intentionally minimal and self-contained:
- **Single file deployment** - Everything in one Python script
- **Zero external dependencies** - Uses only Python standard library  
- **Clean architecture** - Well-organized, documented, and maintainable code
- **Professional grade** - Production-ready with comprehensive error handling

## 🛠️ Command Line Options

```bash
python about_comment.py [-h] [-x EXTS] [-v] [-f] path name
```

| Option | Description |
|--------|-------------|
| `path` | Path to file or directory to process |
| `name` | Author name for about statements |
| `-x EXTS` | Filter by file extensions (comma-separated) |
| `-v` | Verbose output with detailed information |
| `-f` | Force overwrite existing about statements |
| `-h` | Show help message |

## 📋 Usage Examples

```bash
# Process single file with verbose output
python about_comment.py script.py "John Doe" -v

# Process web project files  
python about_comment.py ./webapp/ "Frontend Team" -x html,css,js,ts

# Process Python project, force overwrite
python about_comment.py ./my-project/ "Jane Smith" -x py -f -v

# Process current directory, all supported files
python about_comment.py . "Developer" -v
```

# Force overwrite existing about statements
python about_comment.py ./src/ "Team Lead" -f
```

## 🗂️ Supported File Formats

### Programming Languages
- **C/C++**: `.c`, `.cpp`, `.cxx`, `.cc`, `.c++`, `.h`, `.hpp`, `.hxx`
- **Java**: `.java`
- **Python**: `.py`, `.pyx`, `.pyi`
- **JavaScript/TypeScript**: `.js`, `.jsx`, `.ts`, `.tsx`
- **C#**: `.cs`
- **PHP**: `.php`
- **Go**: `.go`
- **Rust**: `.rs`
- **Swift**: `.swift`
- **Kotlin**: `.kt`
- **Scala**: `.scala`
- **Dart**: `.dart`
- **Ruby**: `.rb`
- **Perl**: `.pl`, `.pm`, `.perl`
- **R**: `.r`, `.R`
- **Lua**: `.lua`
- **MATLAB**: `.m`
- **Julia**: `.jl`
- **Crystal**: `.cr`
- **Nim**: `.nim`
- **Zig**: `.zig`
- **D**: `.d`
- **Ada**: `.ada`, `.adb`, `.ads`
- **COBOL**: `.cob`, `.cbl`
- **Fortran**: `.f`, `.f90`, `.f95`, `.f03`, `.f08`
- **Pascal**: `.pas`, `.pp`, `.dpr`
- **Visual Basic**: `.vb`, `.vbs`

### Functional Languages
- **Haskell**: `.hs`, `.lhs`
- **Elm**: `.elm`
- **OCaml**: `.ml`, `.mli`
- **F#**: `.fs`, `.fsx`, `.fsi`
- **Erlang**: `.erl`, `.hrl`
- **Elixir**: `.ex`, `.exs`

### Web Technologies
- **HTML**: `.html`, `.htm`, `.xhtml`
- **CSS**: `.css`, `.scss`, `.sass`, `.less`
- **XML**: `.xml`, `.xsl`, `.xslt`, `.svg`
- **Vue**: `.vue`

### Shell Scripts
- **Bash**: `.sh`, `.bash`
- **Zsh**: `.zsh`
- **Fish**: `.fish`
- **PowerShell**: `.ps1`, `.psm1`, `.psd1`
- **Batch**: `.bat`, `.cmd`

### Configuration & Data
- **JSON**: `.json`, `.jsonc`
- **YAML**: `.yaml`, `.yml`
- **TOML**: `.toml`
- **INI**: `.ini`, `.cfg`, `.conf`
- **SQL**: `.sql`, `.psql`, `.mysql`, `.sqlite`
- **CSV**: `.csv`, `.tsv`

### Infrastructure as Code
- **Terraform**: `.tf`, `.tfvars`
- **HCL**: `.hcl`
- **Docker**: `.dockerfile`

### Documentation
- **Markdown**: `.md`, `.markdown`, `.mdown`
- **reStructuredText**: `.rst`
- **LaTeX**: `.tex`, `.latex`, `.bib`
- **Plain Text**: `.txt`, `.text`, `.log`, `.readme`

### Build Systems
- **Make**: `.make`, `.mk`
- **CMake**: `.cmake`

## 🎯 Comment Styles

The script automatically uses the appropriate comment style for each file type:

- **C-style comments**: `/* comment */` for C, Java, JavaScript, etc.
- **Hash comments**: `# comment` for Python, Shell, YAML, etc.
- **XML comments**: `<!-- comment -->` for HTML, XML, SVG, etc.
- **SQL comments**: `-- comment` for SQL files
- **Percent comments**: `% comment` for LaTeX, MATLAB
- **And many more...**

## 📊 Output Example

```bash
$ python about_comment.py ./src/ "John Doe" -x py,js -v

[*] Processing directory: /path/to/src
[*] Extensions filter: ['py', 'js']
[*] Author: John Doe
[*] Force overwrite: False
--------------------------------------------------
[*] Added /path/to/src/main.py to processing list
[*] Added /path/to/src/utils.js to processing list
[*] Processing 2 files...

===========================================================================
Processing: /path/to/src/main.py
===========================================================================
[*] Reading content of '/path/to/src/main.py'
[*] Successfully added about statement to '/path/to/src/main.py'

===========================================================================
Processing: /path/to/src/utils.js
===========================================================================
[*] Reading content of '/path/to/src/utils.js'
[*] Successfully added about statement to '/path/to/src/utils.js'

==================================================
Processing Complete!
Processed: 2 files
Skipped: 0 files
Errors: 0 files
==================================================
```

## ⚠️ Important Notes

- The script creates backups (`.bak` files) for files larger than 10KB before modification
- Files are processed with UTF-8 encoding
- Binary files and common build artifacts are automatically excluded
- The script intelligently handles special file structures (PHP tags, HTML doctypes, Python shebangs, etc.)

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests to improve the Enhanced About Writer!

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
