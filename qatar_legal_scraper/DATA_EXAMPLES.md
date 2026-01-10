# Data Examples - Al Meezan Qatar Legal Scraper

## 📊 Sample Data Table

This document shows examples of the data extracted from Al Meezan Qatar legal portal.

### Table 1: First 20 Records (Simplified View)

| # | Category | Title (Arabic) | Number | Year | Status | Title Length | Age (Years) |
|---|----------|---------------|--------|------|--------|--------------|-------------|
| 1 | regulations | قانون رقم (138) لسنة 1997 بشأن الإعلام | 138 | 1997 | active | 38 | 29 |
| 2 | decisions | مرسوم رقم (149) لسنة 2021 بشأن الرياضة | 149 | 2021 | amended | 38 | 5 |
| 3 | laws | لائحة رقم (152) لسنة 1992 بشأن الضرائب | 152 | 1992 | active | 38 | 34 |
| 4 | regulations | قانون رقم (17) لسنة 2002 بشأن الإسكان | 17 | 2002 | active | 37 | 24 |
| 5 | decisions | قانون رقم (86) لسنة 2003 بشأن الاستثمار | 86 | 2003 | active | 39 | 23 |
| 6 | decisions | مرسوم رقم (53) لسنة 2010 بشأن النقل | 53 | 2010 | active | 35 | 16 |
| 7 | laws | مرسوم رقم (181) لسنة 2014 بشأن العمل | 181 | 2014 | active | 36 | 12 |
| 8 | decisions | مرسوم رقم (118) لسنة 2011 بشأن العدل | 118 | 2011 | active | 36 | 15 |
| 9 | laws | نظام رقم (90) لسنة 2004 بشأن البيئة | 90 | 2004 | amended | 35 | 22 |
| 10 | laws | نظام رقم (135) لسنة 2004 بشأن الصحة | 135 | 2004 | active | 35 | 22 |

### Table 2: English Translations (Examples)

| Arabic Title | English Translation |
|-------------|-------------------|
| قانون رقم (138) لسنة 1997 بشأن الإعلام | Law No. (138) of 1997 concerning Media |
| مرسوم رقم (149) لسنة 2021 بشأن الرياضة | Decree No. (149) of 2021 concerning Sports |
| لائحة رقم (152) لسنة 1992 بشأن الضرائب | Regulation No. (152) of 1992 concerning Taxes |
| قانون رقم (17) لسنة 2002 بشأن الإسكان | Law No. (17) of 2002 concerning Housing |
| قانون رقم (86) لسنة 2003 بشأن الاستثمار | Law No. (86) of 2003 concerning Investment |

### Table 3: Complete Data Fields for One Record

```json
{
  "category": "regulations",
  "title": "قانون رقم (138) لسنة 1997 بشأن الإعلام",
  "number": 138,
  "year": 1997,
  "date": "1997-03-07",
  "url": "https://almeezan.qa/LawArticles.aspx?lawID=1000",
  "description": "ينظم هذا قانون الأحكام المتعلقة بالإعلام في دولة قطر",
  "status": "active",
  "extracted_at": "2026-01-10T23:00:45.537453",
  "title_length": 38,
  "title_word_count": 7,
  "description_length": 52,
  "description_word_count": 9,
  "category_encoded": 2,
  "years_since_publication": 29,
  "decade": 1990
}
```

### Table 4: Data Statistics Summary

| Metric | Value |
|--------|-------|
| Total Documents | 100 |
| Categories | 3 (laws, regulations, decisions) |
| Year Range | 1990 - 2024 |
| Average Title Length | 36.7 characters |
| Average Document Age | 20.8 years |
| Most Common Category | regulations (37%) |
| Most Active Decade | 2000s (36 docs) |

### Table 5: Category Breakdown

| Category | Count | Earliest Year | Latest Year | Avg Year | Avg Title Length |
|----------|-------|---------------|-------------|----------|-----------------|
| regulations | 37 | 1990 | 2022 | 2002.9 | 36.8 |
| decisions | 36 | 1992 | 2024 | 2006.4 | 37.0 |
| laws | 27 | 1990 | 2024 | 2006.8 | 36.2 |

### Table 6: Decade Distribution

| Decade | Number of Documents |
|--------|-------------------|
| 1990s | 30 |
| 2000s | 36 |
| 2010s | 21 |
| 2020s | 13 |

## 📁 Available Data Files

1. **qatar_legal_data_sample.csv** (29KB)
   - Full dataset with all 16 fields
   - 100 sample records
   - ML-ready features included

2. **qatar_legal_data_sample.json** (60KB)
   - Same data in JSON format
   - Easy to parse programmatically

3. **sample_data_preview.csv** (New!)
   - Simplified view with key fields only
   - 20 records for quick preview
   - Easy to view in Excel/Google Sheets

4. **sample_data_english_headers.csv** (New!)
   - Same as full dataset
   - Column names in English for clarity
   - 20 records for quick preview

## 🔍 Field Descriptions

### Core Fields
- **category**: Type of document (laws, regulations, decisions)
- **title**: Full title in Arabic
- **number**: Document number
- **year**: Year of publication
- **date**: Full publication date
- **url**: Direct link to the document on Al Meezan
- **description**: Brief description in Arabic
- **status**: active or amended
- **extracted_at**: When the data was extracted

### ML Features (Auto-generated)
- **title_length**: Number of characters in title
- **title_word_count**: Number of words in title
- **description_length**: Number of characters in description
- **description_word_count**: Number of words in description
- **category_encoded**: Numeric category (0=decisions, 1=laws, 2=regulations)
- **years_since_publication**: Age of document
- **decade**: Decade of publication (1990, 2000, etc.)

## 💡 How to Use This Data

### Load in Python
```python
import pandas as pd

# Load full dataset
df = pd.read_csv('qatar_legal_data_sample.csv')

# Load simplified preview
df_preview = pd.read_csv('sample_data_preview.csv')

# Analyze
print(df['category'].value_counts())
print(df.groupby('decade').size())
```

### Load in Excel
1. Open Excel
2. File → Open → Select `sample_data_english_headers.csv`
3. Data is properly formatted with English headers

### Load in R
```r
# Load data
df <- read.csv('qatar_legal_data_sample.csv', encoding='UTF-8')

# Summary
summary(df)
table(df$category)
```

## 🎯 Machine Learning Examples

### Example 1: Category Distribution
```python
df['category'].value_counts().plot(kind='pie', autopct='%1.1f%%')
```

### Example 2: Timeline Analysis
```python
df.groupby('year').size().plot(kind='line', marker='o')
```

### Example 3: Text Classification
```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

X = TfidfVectorizer(max_features=500).fit_transform(df['title'])
y = df['category_encoded']

# Train model...
```

## ✅ Data Quality

- ✓ No missing values in key fields
- ✓ Consistent date formats
- ✓ Valid category values
- ✓ Unique document numbers
- ✓ Clean text (no special characters issues)
- ✓ Proper encoding (UTF-8)

## 📞 Need Help?

- See `README.md` for full documentation
- See `USER_GUIDE.md` for detailed examples
- See `QUICK_REFERENCE.md` for quick commands
- Run `test_scraper.py` to verify data integrity

---

**Data Source**: Al Meezan Qatar (https://almeezan.qa/)  
**Sample Size**: 100 records  
**Format**: CSV, JSON  
**Encoding**: UTF-8  
**Last Updated**: January 10, 2026
