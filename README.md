# Sentiment Analysis of Book Text

This script performs sentiment analysis on a book text to identify the most frequently used words, eliminate stop words, and analyze sentiment scores for each chapter. The script uses Python's `nltk` library for natural language processing.

## Requirements

- Python 3.x
- NLTK Library
- `nltk.corpus` (for stopwords)
- `nltk.sentiment` (for SentimentIntensityAnalyzer)
- `miracle_in_the_andes.txt` (sample book text file)

## Usage

1. Make sure you have Python 3.x installed.
2. Install the required libraries using the following command:
   ```sh
   pip install nltk
   ```
3. Download the NLTK resources (if not downloaded previously):
   ```python
   import nltk
   nltk.download('stopwords')
   nltk.download('vader_lexicon')
   ```
4. Place your book text file (e.g., `miracle_in_the_andes.txt`) in the same directory as the script.
5. Run the script using the following command:
   ```sh
   python sentiment_analysis.py
   ```

## Functionality

- The script reads the book text from the provided file.
- It applies regex to collect the most frequently used words from the book.
- Words are filtered to remove English stopwords.
- Sentiment analysis is performed on the entire book and each chapter using the VADER sentiment intensity analyzer.
- Results include sentiment scores for each chapter and an overall sentiment score for the entire book.

## Example Output

```
Chapter 0 has {'neg': 0.101, 'neu': 0.745, 'pos': 0.154, 'compound': 0.9842}
Chapter 1 has {'neg': 0.104, 'neu': 0.783, 'pos': 0.113, 'compound': 0.3953}
...
Overall Book Sentiment: {'neg': 0.076, 'neu': 0.796, 'pos': 0.128, 'compound': 0.9967}
```

## Note

- The sentiment analysis results provide insight into the emotional tone of each chapter and the overall book.
- The VADER sentiment intensity analyzer categorizes text as negative, neutral, or positive based on sentiment scores.

## License

This project is licensed under the [MIT License](LICENSE).
```
