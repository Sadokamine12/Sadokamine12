# Al Meezan Qatar Legal Data Scraper

A comprehensive Python tool to extract and structure legal data from [Al Meezan](https://almeezan.qa/), Qatar's official legal portal, for machine learning applications.

## 🎯 Features

- ✅ Extracts laws, regulations, and legal decisions from Al Meezan portal
- ✅ Structures data in ML-ready formats (CSV, JSON)
- ✅ Automatic data cleaning and preprocessing
- ✅ Handles pagination and multiple document categories
- ✅ Generates additional ML features (text length, word count, temporal features)
- ✅ Exports data schema for easy integration
- ✅ Comprehensive error handling and logging
- ✅ Respects server resources with configurable delays

## 📋 Data Structure

The scraper extracts the following fields for each legal document:

| Field | Description | Type |
|-------|-------------|------|
| `category` | Type of legislation (laws/regulations/decisions) | string |
| `title` | Full title of the legal document | string |
| `number` | Law/regulation number | string |
| `year` | Year of publication | integer |
| `date` | Publication date | string |
| `url` | Direct URL to the document | string |
| `description` | Summary or description | string |
| `status` | Document status (active/inactive) | string |
| `extracted_at` | Timestamp of data extraction | datetime |

### ML-Ready Features (Preprocessed Data)

Additional features automatically generated for machine learning:

- `category_encoded`: Numerical encoding of categories
- `title_length`: Character count of title
- `title_word_count`: Word count in title
- `description_length`: Character count of description
- `description_word_count`: Word count in description
- `years_since_publication`: Age of the document
- `decade`: Decade of publication

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. Clone this repository or download the scraper files

2. Install dependencies:

```bash
cd qatar_legal_scraper
pip install -r requirements.txt
```

## 💻 Usage

### Basic Usage

```python
from qatar_legal_scraper import AlMeezanScraper

# Initialize the scraper
scraper = AlMeezanScraper(delay=1.0, language='ar')

# Scrape all categories (laws, regulations, decisions)
df = scraper.scrape_all_categories(max_pages_per_category=3)

# Save data in multiple formats
files = scraper.save_data(df, 'qatar_legal_data')

print(f"Scraped {len(df)} legal documents")
print(f"Files saved: {files}")
```

### Advanced Usage

```python
# Scrape specific category only
laws = scraper.extract_legislation_list(category='laws', max_pages=5)

# Extract detailed content from a specific URL
details = scraper.extract_legislation_details('https://almeezan.qa/LawArticles.aspx?lawID=XXX')

# Preprocess data for machine learning
df_ml = scraper.preprocess_for_ml(df)

# Custom data processing
df_filtered = df[df['year'] >= 2000]  # Filter laws from 2000 onwards
df_sorted = df.sort_values('year', ascending=False)  # Sort by year
```

### Command Line Usage

Run the scraper directly:

```bash
python -m qatar_legal_scraper.scraper
```

Or use the main script:

```bash
cd qatar_legal_scraper
python scraper.py
```

## 📊 Output Files

The scraper generates the following files:

1. **qatar_legal_data.csv** - Raw data in CSV format
2. **qatar_legal_data.json** - Raw data in JSON format
3. **qatar_legal_data_ml_ready.csv** - Preprocessed data with ML features
4. **qatar_legal_data_schema.json** - Data schema and metadata

## 🤖 Machine Learning Use Cases

This structured legal data can be used for various ML applications:

### Text Classification
- Classify legal documents by type
- Categorize by subject matter
- Predict document status

### Natural Language Processing
- Arabic text analysis
- Legal terminology extraction
- Document summarization
- Topic modeling

### Time Series Analysis
- Track legal trends over time
- Predict future legislation patterns
- Analyze publication frequency

### Information Retrieval
- Build legal search engines
- Semantic similarity matching
- Question-answering systems

### Example ML Pipeline

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

# Load preprocessed data
df = pd.read_csv('qatar_legal_data_ml_ready.csv')

# Prepare features for classification
vectorizer = TfidfVectorizer(max_features=1000)
X_text = vectorizer.fit_transform(df['title'])

# Combine with numerical features
X_numeric = df[['year', 'title_length', 'title_word_count']]
X = pd.concat([pd.DataFrame(X_text.toarray()), X_numeric.reset_index(drop=True)], axis=1)

# Target variable
y = df['category_encoded']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Evaluate
accuracy = clf.score(X_test, y_test)
print(f"Classification Accuracy: {accuracy:.2%}")
```

## ⚙️ Configuration

### Scraper Parameters

- `delay`: Delay between requests in seconds (default: 1.0)
- `language`: Language code - 'ar' for Arabic, 'en' for English (default: 'ar')
- `max_pages_per_category`: Number of pages to scrape per category (default: 3)

### Customization

Modify selectors in `scraper.py` if the website structure changes:

```python
# Update CSS selectors for different page elements
items = soup.find_all('div', class_=['law-item', 'legislation-item'])
```

## 📝 Data Schema

Sample data structure:

```json
{
  "category": "laws",
  "title": "قانون رقم (12) لسنة 2004 بشأن...",
  "number": "12",
  "year": "2004",
  "date": "2004-07-15",
  "url": "https://almeezan.qa/LawArticles.aspx?lawID=123",
  "description": "قانون ينظم...",
  "status": "active",
  "extracted_at": "2026-01-10T22:55:00"
}
```

## 🔧 Troubleshooting

### Common Issues

**Issue**: No data scraped
- **Solution**: Check website structure, selectors may need updating
- **Solution**: Verify internet connection and website availability

**Issue**: SSL/Certificate errors
- **Solution**: Update certificates or add `verify=False` (not recommended for production)

**Issue**: Rate limiting or blocking
- **Solution**: Increase delay between requests
- **Solution**: Implement rotating user agents

**Issue**: Encoding issues with Arabic text
- **Solution**: Ensure UTF-8 encoding when saving/loading files
- **Solution**: Use `encoding='utf-8-sig'` for CSV files

## 📄 License

This tool is provided for educational and research purposes. Please ensure compliance with Al Meezan's terms of service and robots.txt when using this scraper.

## ⚠️ Ethical Considerations

- ✅ Respect server resources (use appropriate delays)
- ✅ Check robots.txt and terms of service
- ✅ Don't overload the server with requests
- ✅ Use data responsibly and ethically
- ✅ Cite the source when using the data

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📧 Contact

For questions or issues, please open an issue on GitHub or contact the repository owner.

## 🔗 Resources

- [Al Meezan Official Website](https://almeezan.qa/)
- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)

---

**Built with ❤️ for Data Science and Legal Tech**
