# Chinese Character Parser

## Overview
This Python tool analyzes Chinese characters from a text file, utilizing the Unihan database for character metadata and `hanzipy` for decomposition into radical components. It retrieves details such as Mandarin pronunciation and definitions, and decomposes characters into their graphical and radical parts, exporting the results in a CSV format for easy analysis or integration with other data handling applications.

## Features
- Load Chinese characters from a simple text file.
- Fetch character information from a local JSON formatted Unihan database.
- Decompose characters into radical and graphical components using `hanzipy`.
- Output the information into a structured CSV file with detailed annotations for each component.

## Installation

To get started with the Chinese Character Parser, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/M3C3I/ChineseCharacterParser.git
   ```

2. Install the required dependencies:
   ```bash
   pip install hanzipy
   ```

## Usage

To run the program, ensure you have a text file named `input.txt` in the same directory as the script, with one Chinese character per line. Then execute the script:

```bash
python ChineseCharacterParser.py
```

The output will be a CSV file named `output.csv` containing detailed character analysis.

## Input File Format

The `input.txt` file should contain one Chinese character per line, like this:

```
爱
橄
黃
```

## Output Format

The `output.csv` will contain the following columns:
- `Number`: Unique identifier for each character (e.g., 1, 1a, 1b, etc.)
- `Character`: The Chinese character being analyzed.
- `Mandarin`: Mandarin pronunciation of the character.
- `Definition`: Definition of the character.
- `PrimaryRadical`: The primary radical of the character.
- `RadicalMandarin`: Mandarin pronunciation of the primary radical.
- `HanzipyStrokes`: Graphical components of the character as determined by `hanzipy`.
- `HanzipyRadicals`: Detailed radical components, each in a new line with its details.

## Contributing

Contributions to the Chinese Character Parser are welcome! Please feel free to fork the repository, make changes, and submit pull requests.
