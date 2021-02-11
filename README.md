# Subtitle Analyzer
Downloads the subtitles of IMDB Top 100 movies, extracts them out of the ".zip" file.
Lists all words and their counts. Filters stopwords. (e.g. "the", "a/an", "him", etc.)
Analyzes the data obtained, generates a chart in the desired direction for the Top 100 words.

## Usage
Run `python subtitle_analyzer.py` in the project folder.

### Execution environment
- Only compatible with > py 3.6
- 'movie_list.txt' & 'stopwords.txt' files must be in the 'lists' folder, which must be inside execution direction.

#### Known issues
- Subtitle downloader couldn't download all the subtitles in the list.
- Word analyzer couldn't analyze all the words in the word list due to char encoding issues.
- ~~Some word's full forms and contraction forms counted separately (e.g. "I am" - "I'm", "he will" - "he'll")~~
- ~~Stopwords should be expanded. (i.e. counts, letters)~~