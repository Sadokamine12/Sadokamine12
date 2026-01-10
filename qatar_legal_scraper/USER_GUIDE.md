# Al Meezan Qatar Legal Data Scraper - Complete User Guide

## 🎯 What This Tool Does

This tool extracts complete legal data from Qatar's official legal portal (https://almeezan.qa/) and structures it into a machine learning-ready format. Perfect for:

- **Legal Research**: Analyze Qatar's legal framework
- **Data Science Projects**: Use structured legal data for ML
- **Text Analytics**: Apply NLP on Arabic legal texts
- **Trend Analysis**: Study legal developments over time

## 📦 What You Get

### 1. Complete Scraper Module (`scraper.py`)
- Extracts laws, regulations, and legal decisions
- Handles pagination automatically
- Respects server resources (configurable delays)
- Robust error handling and logging

### 2. Sample Dataset (100 Records)
- `qatar_legal_data_sample.csv` - Ready to use
- `qatar_legal_data_sample.json` - JSON format
- Representative of real Al Meezan data structure
- Perfect for testing and development

### 3. ML Analysis Tools
- Jupyter notebook with examples
- Preprocessing functions
- Feature engineering
- Classification examples

### 4. Documentation
- Comprehensive README
- API documentation
- Usage examples
- Troubleshooting guide

## 🚀 Getting Started in 3 Steps

### Step 1: Install Dependencies

```bash
cd qatar_legal_scraper
pip install -r requirements.txt
```

**Required packages:**
- requests (web scraping)
- beautifulsoup4 (HTML parsing)
- pandas (data processing)
- numpy (numerical operations)
- lxml (XML/HTML processing)

### Step 2: Run Your First Scrape

**Option A: Quick Test with Sample Data**
```bash
python sample_data_generator.py
```
Output: 100 sample legal documents in CSV and JSON

**Option B: Scrape Real Data**
```bash
python scraper.py
```
Note: This will attempt to scrape the actual Al Meezan website

**Option C: Interactive Examples**
```bash
python example_usage.py
```
Choose from 5 different examples

### Step 3: Analyze with Machine Learning

```bash
jupyter notebook example_ml_analysis.ipynb
```

Or use Python:
```python
import pandas as pd
from scraper import AlMeezanScraper

# Load sample data
df = pd.read_csv('qatar_legal_data_sample.csv')

# Analyze
print(df.groupby('category').size())
print(df['year'].describe())
```

## 📊 Data Structure Explained

### Raw Data Fields

```python
{
    "category": "laws",              # Type: laws, regulations, decisions
    "title": "قانون رقم (12)...",    # Full title in Arabic
    "number": "12",                  # Document number
    "year": 2004,                    # Year of publication
    "date": "2004-07-15",           # Publication date
    "url": "https://...",           # Direct link
    "description": "...",           # Summary
    "status": "active",             # active/amended
    "extracted_at": "2026-01-10..." # Extraction timestamp
}
```

### ML-Ready Features (Automatically Added)

```python
{
    "category_encoded": 0,           # Numeric category (0, 1, 2)
    "title_length": 38,              # Character count
    "title_word_count": 7,           # Word count
    "description_length": 52,        # Description length
    "description_word_count": 9,     # Description words
    "years_since_publication": 22,   # Age of document
    "decade": 2000                   # Publication decade
}
```

## 🎓 Machine Learning Examples

### Example 1: Load and Explore Data

```python
import pandas as pd

# Load preprocessed data
df = pd.read_csv('qatar_legal_data_sample.csv')

# Basic statistics
print(f"Total documents: {len(df)}")
print(f"\nBy category:\n{df['category'].value_counts()}")
print(f"\nYear range: {df['year'].min()} - {df['year'].max()}")

# Text statistics
print(f"\nAverage title length: {df['title_length'].mean():.1f} characters")
print(f"Average word count: {df['title_word_count'].mean():.1f} words")
```

### Example 2: Text Classification

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Prepare data
X_text = TfidfVectorizer(max_features=500).fit_transform(df['title'])
y = df['category_encoded']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_text, y, test_size=0.2, random_state=42
)

# Train classifier
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)

# Evaluate
accuracy = clf.score(X_test, y_test)
print(f"Accuracy: {accuracy:.2%}")
```

### Example 3: Time Series Analysis

```python
import matplotlib.pyplot as plt

# Documents per year
year_counts = df['year'].value_counts().sort_index()

plt.figure(figsize=(12, 6))
year_counts.plot(kind='line', marker='o')
plt.title('Legal Documents Published Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Documents')
plt.grid(True)
plt.show()
```

### Example 4: Category Analysis by Decade

```python
# Pivot table
decade_category = pd.crosstab(df['decade'], df['category'])

# Stacked bar chart
decade_category.plot(kind='bar', stacked=True, figsize=(12, 6))
plt.title('Legal Documents by Category and Decade')
plt.xlabel('Decade')
plt.ylabel('Count')
plt.legend(title='Category')
plt.show()
```

## 🔧 Advanced Usage

### Custom Scraping Parameters

```python
from scraper import AlMeezanScraper

# Initialize with custom settings
scraper = AlMeezanScraper(
    delay=2.0,        # 2 second delay between requests
    language='en'     # English content (if available)
)

# Scrape specific category
laws = scraper.extract_legislation_list(
    category='laws',
    max_pages=10      # Scrape 10 pages
)

# Get detailed content
details = scraper.extract_legislation_details(url)
```

### Custom Preprocessing

```python
# Load raw data
df = scraper.scrape_all_categories(max_pages_per_category=5)

# Apply custom preprocessing
df_custom = df.copy()

# Add custom features
df_custom['is_recent'] = df_custom['year'] >= 2010
df_custom['title_has_number'] = df_custom['title'].str.contains(r'\d+')
df_custom['season'] = df_custom['date'].apply(lambda x: 
    pd.to_datetime(x).month // 3 if pd.notna(x) else None
)

# Save
df_custom.to_csv('custom_processed_data.csv', index=False)
```

## 📈 Visualization Examples

### Create a Dashboard

```python
import matplotlib.pyplot as plt
import seaborn as sns

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Category distribution
df['category'].value_counts().plot(kind='pie', ax=axes[0,0], autopct='%1.1f%%')
axes[0,0].set_title('Distribution by Category')

# 2. Year trend
df.groupby('year').size().plot(ax=axes[0,1])
axes[0,1].set_title('Documents Published Over Time')

# 3. Title length distribution
axes[1,0].hist(df['title_length'], bins=20, edgecolor='black')
axes[1,0].set_title('Title Length Distribution')

# 4. Decade comparison
df.groupby(['decade', 'category']).size().unstack().plot(
    kind='bar', ax=axes[1,1], stacked=True
)
axes[1,1].set_title('Documents by Decade and Category')

plt.tight_layout()
plt.savefig('legal_data_dashboard.png', dpi=300)
plt.show()
```

## 🐛 Troubleshooting

### Issue: Import errors

**Problem:** `ModuleNotFoundError: No module named 'pandas'`

**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: Website not accessible

**Problem:** Cannot scrape from almeezan.qa

**Solution:**
```bash
# Use sample data instead
python sample_data_generator.py

# Or load existing sample
df = pd.read_csv('qatar_legal_data_sample.csv')
```

### Issue: Arabic text display issues

**Problem:** Garbled Arabic characters

**Solution:**
```python
# Use proper encoding when reading CSV
df = pd.read_csv('qatar_legal_data_sample.csv', encoding='utf-8-sig')

# For displaying Arabic in matplotlib
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'DejaVu Sans'
```

### Issue: Slow scraping

**Problem:** Scraping takes too long

**Solution:**
```python
# Reduce pages per category
scraper.scrape_all_categories(max_pages_per_category=2)

# Or scrape one category
laws = scraper.extract_legislation_list(category='laws', max_pages=3)
```

## 📚 Additional Resources

### For Arabic NLP
- **CAMeL Tools**: Arabic NLP toolkit
- **AraBERT**: Arabic BERT models
- **Farasa**: Arabic text processing

### For Legal ML
- **Spacy**: NLP library with legal models
- **Hugging Face**: Pre-trained transformers
- **LexNLP**: Legal-specific NLP

### Data Science Tools
- **Scikit-learn**: ML algorithms
- **TensorFlow/PyTorch**: Deep learning
- **NLTK**: Text processing

## 🎯 Project Ideas

1. **Legal Document Classifier**: Categorize documents by subject
2. **Timeline Visualizer**: Track legal changes over time
3. **Search Engine**: Find relevant laws quickly
4. **Recommendation System**: Suggest related legislation
5. **Trend Analyzer**: Predict future legal directions
6. **Citation Network**: Map relationships between laws
7. **Summarization Tool**: Generate law summaries
8. **Compliance Checker**: Identify applicable regulations

## ✅ Verification

Run the test suite to verify everything works:

```bash
python test_scraper.py
```

Expected output:
```
Tests passed: 7/7
Success rate: 100.0%
✓ All tests passed!
```

## 📞 Support

If you encounter issues:

1. Check the main README.md
2. Review example_usage.py
3. Run test_scraper.py
4. Check logs for error messages
5. Open an issue on GitHub

---

**Happy Analyzing! 🚀📊**
