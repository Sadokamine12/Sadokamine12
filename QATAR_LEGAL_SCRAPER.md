# Qatar Legal Data Scraper & ML Tool

A professional web scraping tool that extracts legal data from [Al Meezan Qatar](https://almeezan.qa/) (Qatar's official legal portal) and structures it for machine learning applications.

## 📁 Project Structure

```
qatar_legal_scraper/
├── scraper.py                      # Main scraper module
├── __init__.py                     # Package initialization
├── requirements.txt                # Python dependencies
├── README.md                       # Detailed documentation
├── config.json                     # Configuration settings
├── example_usage.py                # Quick start examples
├── example_ml_analysis.ipynb       # Jupyter notebook with ML examples
├── sample_data_generator.py        # Generate sample data for testing
├── qatar_legal_data_sample.csv     # Sample dataset (100 records)
├── qatar_legal_data_sample.json    # Sample dataset in JSON format
└── .gitignore                      # Git ignore rules
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd qatar_legal_scraper
pip install -r requirements.txt
```

### 2. Run the Scraper

**Option A: Use the main script**
```bash
python scraper.py
```

**Option B: Use as a Python module**
```python
from qatar_legal_scraper import AlMeezanScraper

scraper = AlMeezanScraper(delay=1.0)
df = scraper.scrape_all_categories(max_pages_per_category=3)
files = scraper.save_data(df, 'qatar_legal_data')
```

**Option C: Run interactive examples**
```bash
python example_usage.py
```

### 3. Analyze Data with Machine Learning

Open the Jupyter notebook for ML examples:
```bash
jupyter notebook example_ml_analysis.ipynb
```

## 📊 Features

✅ **Web Scraping**
- Extracts laws, regulations, and legal decisions
- Handles pagination automatically
- Respects server resources with configurable delays
- Robust error handling and logging

✅ **Data Structuring**
- Exports to CSV, JSON formats
- Clean, structured data ready for ML
- Automatic feature engineering

✅ **ML-Ready Features**
- Text statistics (length, word count)
- Temporal features (decade, years since publication)
- Category encoding
- Duplicate removal

✅ **Sample Data**
- 100 sample records included for testing
- Arabic legal document format
- Representative of real data structure

## 📝 Data Schema

Each legal document contains:

| Field | Description |
|-------|-------------|
| `category` | Type (laws/regulations/decisions) |
| `title` | Full title in Arabic |
| `number` | Document number |
| `year` | Year of publication |
| `date` | Publication date |
| `url` | Direct link to document |
| `description` | Summary |
| `status` | Active/Amended status |
| `extracted_at` | Extraction timestamp |

**ML Features:**
- `category_encoded` - Numerical category
- `title_length` - Character count
- `title_word_count` - Word count
- `years_since_publication` - Document age
- `decade` - Publication decade

## 🤖 ML Use Cases

- **Text Classification**: Categorize legal documents
- **NLP**: Arabic text analysis, topic modeling
- **Time Series**: Analyze legal trends over time
- **Information Retrieval**: Build search engines
- **Clustering**: Group similar documents
- **Summarization**: Generate legal summaries

## 📚 Documentation

See [qatar_legal_scraper/README.md](qatar_legal_scraper/README.md) for complete documentation including:
- Detailed usage examples
- ML pipeline examples
- Configuration options
- Troubleshooting guide
- API reference

## 🔧 Requirements

- Python 3.8+
- requests
- beautifulsoup4
- pandas
- numpy
- lxml

## 📄 License

Educational/Research use. Please respect Al Meezan's terms of service.

## 🤝 Contributing

This project is part of a data science portfolio. Contributions and suggestions are welcome!

## 📧 Contact

**Sadok Amine Ben Khalfallah**
- Email: sadok.khalfallah94@gmail.com
- LinkedIn: [Sadok Amine Ben Khalfallah](https://www.linkedin.com/in/sadok-amine-ben-khalfallah-15a88a166/)
- Kaggle: [sadokamine12](https://www.kaggle.com/sadokamine12)

---

Built with ❤️ for Data Science & Legal Tech
