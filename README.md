
# About Writer

A Python script that automatically adds professional "about" statements to source code files across 100+ programming languages and file formats. Features include cross-platform compatibility, intelligent comment handling, and robust error management.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Overview](#file-overview)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features
- Universal support for 100+ file formats
- Cross-platform: Windows, macOS, Linux
- Smart comment detection for each file type

## Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/elxecutor/About-Writer.git
cd About-Writer
pip install -r requirements.txt
```

## Usage
1. Process a single file:
	```bash
	python about_comment.py /path/to/file.py "John Doe"
	```
2. Process a directory with specific extensions:
	```bash
	python about_comment.py ./project/ "Jane Smith" -x py,js,html,css
	```

## File Overview
- `about_comment.py`: Main script for adding about statements
- `LICENSE`: MIT license
- `README.md`: Project documentation
- `temp_test.py`: Example/test script

## Contributing
We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md) for details.

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
For questions or support, please open an issue or contact the maintainer via [X](https://x.com/elxecutor/).
