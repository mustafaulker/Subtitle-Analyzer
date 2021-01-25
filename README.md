# Subtitle Analyzer
Downloads the subtitles of IMDB Top 100 movies, extracts them out of the ".zip" file.
Lists all words and their counts.
Analyzes the data acquired, generates a chart as desired direction.

## Known issues
- Subtitle downloader couldn't download all the subtitles in the list.
- Word analyzer couldn't analyze all the words in the word list due to char encoding issues.
- Some word's full forms and contraction forms counted separately (e.g. "I am" - "I'm", "he will" - "he'll")