# Qatar Legal Scraper - Quick Reference

## 🚀 Quick Start

```bash
# 1. Install
cd qatar_legal_scraper
pip install -r requirements.txt

# 2. Generate sample data
python sample_data_generator.py

# 3. Run tests
python test_scraper.py

# 4. Analyze data
python example_usage.py
```

## 📝 Common Commands

### Generate Sample Data
```bash
python sample_data_generator.py
```
Output: `qatar_legal_data_sample.csv`, `qatar_legal_data_sample.json`

### Run Scraper
```python
from scraper import AlMeezanScraper

scraper = AlMeezanScraper(delay=1.0)
df = scraper.scrape_all_categories(max_pages_per_category=3)
files = scraper.save_data(df)
```

### Load Data
```python
import pandas as pd

# Load sample data
df = pd.read_csv('qatar_legal_data_sample.csv')

# Or load scraped data
df = pd.read_csv('qatar_legal_data_ml_ready.csv')
```

### Basic Analysis
```python
# Statistics
print(df['category'].value_counts())
print(df['year'].describe())

# Filter
recent = df[df['year'] >= 2010]
laws_only = df[df['category'] == 'laws']

# Export
df.to_excel('legal_data.xlsx', index=False)
```

## 📊 Data Fields

| Field | Type | Description |
|-------|------|-------------|
| `category` | str | laws/regulations/decisions |
| `title` | str | Document title (Arabic) |
| `number` | str | Document number |
| `year` | int | Publication year |
| `date` | str | Publication date |
| `url` | str | Document URL |
| `description` | str | Summary |
| `status` | str | active/amended |
| `category_encoded` | int | 0, 1, or 2 |
| `title_length` | int | Character count |
| `title_word_count` | int | Word count |
| `years_since_publication` | int | Document age |
| `decade` | int | 1990, 2000, 2010, etc. |

## 🤖 ML Quick Examples

### Classification
```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X = TfidfVectorizer(max_features=500).fit_transform(df['title'])
y = df['category_encoded']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)
print(f"Accuracy: {clf.score(X_test, y_test):.2%}")
```

### Clustering
```python
from sklearn.cluster import KMeans

X = TfidfVectorizer(max_features=300).fit_transform(df['title'])
kmeans = KMeans(n_clusters=5, random_state=42)
df['cluster'] = kmeans.fit_predict(X)
```

### Visualization
```python
import matplotlib.pyplot as plt

# Timeline
df.groupby('year').size().plot(kind='line', marker='o')
plt.title('Documents Over Time')
plt.show()

# Category pie chart
df['category'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.show()
```

## 🔧 Configuration

### Scraper Settings
```python
scraper = AlMeezanScraper(
    delay=1.0,      # Delay between requests (seconds)
    language='ar'   # Language: 'ar' or 'en'
)
```

### Categories
- `'laws'` - Legal laws (قوانين)
- `'regulations'` - Regulations (لوائح)
- `'decisions'` - Decisions (قرارات)

## 📁 File Structure

```
qatar_legal_scraper/
├── scraper.py              # Main scraper
├── sample_data_generator.py # Generate test data
├── example_usage.py        # Usage examples
├── test_scraper.py         # Test suite
├── requirements.txt        # Dependencies
├── README.md              # Full documentation
├── USER_GUIDE.md          # Detailed guide
├── config.json            # Configuration
└── *.csv, *.json          # Data files
```

## ⚡ Tips & Tricks

### Tip 1: Start with Sample Data
```bash
python sample_data_generator.py
```
No internet required, instant results

### Tip 2: Filter Before Processing
```python
# Only recent laws
recent_laws = df[(df['category'] == 'laws') & (df['year'] >= 2015)]
```

### Tip 3: Export for Excel
```python
df.to_excel('legal_data.xlsx', index=False, encoding='utf-8')
```

### Tip 4: Combine Features
```python
from sklearn.preprocessing import StandardScaler

# Combine text and numeric features
text_features = TfidfVectorizer().fit_transform(df['title'])
numeric_features = StandardScaler().fit_transform(
    df[['year', 'title_length', 'title_word_count']]
)
```

## 🐛 Common Issues

| Issue | Solution |
|-------|----------|
| Import errors | `pip install -r requirements.txt` |
| Can't access website | Use `sample_data_generator.py` |
| Arabic text broken | Use `encoding='utf-8-sig'` |
| Slow scraping | Reduce `max_pages_per_category` |

## 📚 Resources

- **Main Docs**: `README.md`
- **User Guide**: `USER_GUIDE.md`
- **Examples**: `example_usage.py`
- **Notebook**: `example_ml_analysis.ipynb`
- **Tests**: `test_scraper.py`

## 🎯 Next Steps

1. ✅ Generate sample data
2. ✅ Run tests to verify
3. ✅ Explore data with pandas
4. ✅ Try ML examples
5. ✅ Build your own analysis

---

**Need Help?** Check `USER_GUIDE.md` for detailed instructions
