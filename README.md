# Subtitle Analyzer

Downloads the subtitles of IMDB Top 100 movies.  
Lists all the words in the subtitles and their counts in an Excel file. Filters stopwords. (e.g. "the", "a/an", "him",
etc.)  
Generates word/count charts based on the data obtained.

## Usage

### Requirements

- Python >= 3.6
- Run `pip install -r requirements.txt` for other dependencies.

### Execution

Run `python src/subtitle_analyzer.py` in the project directory.

### Output

Generated Excel file and Chart images will be in the data_output file under project directory.

#### Output Example

<p align="center">
    <img src="https://user-images.githubusercontent.com/48808788/126179064-154ad914-4b8a-4d96-85a4-8ed861686982.png" alt="Horizontal Chart">
</p>