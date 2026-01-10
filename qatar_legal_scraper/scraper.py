"""
Al Meezan Qatar Legal Data Scraper
===================================
This module extracts legal data from https://almeezan.qa/ and structures it
for machine learning applications.

Features:
- Extracts laws, regulations, and legal decisions
- Structures data in ML-ready format (CSV/JSON)
- Handles pagination and multiple document types
- Includes data cleaning and preprocessing
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import time
import logging
from typing import List, Dict, Optional
from datetime import datetime
import re
from urllib.parse import urljoin

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class AlMeezanScraper:
    """Scraper for Al Meezan Qatar Legal Portal"""
    
    BASE_URL = "https://almeezan.qa"
    
    def __init__(self, delay: float = 1.0, language: str = 'ar'):
        """
        Initialize the scraper
        
        Args:
            delay: Delay between requests in seconds (respect the server)
            language: Language code ('ar' for Arabic, 'en' for English)
        """
        self.delay = delay
        self.language = language
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
    def fetch_page(self, url: str) -> Optional[BeautifulSoup]:
        """
        Fetch and parse a webpage
        
        Args:
            url: URL to fetch
            
        Returns:
            BeautifulSoup object or None if failed
        """
        try:
            time.sleep(self.delay)
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            return BeautifulSoup(response.content, 'html.parser')
        except Exception as e:
            logger.error(f"Error fetching {url}: {e}")
            return None
    
    def extract_legislation_list(self, category: str = 'laws', max_pages: int = 5) -> List[Dict]:
        """
        Extract list of legislation items
        
        Args:
            category: Type of legislation (laws, regulations, decisions)
            max_pages: Maximum number of pages to scrape
            
        Returns:
            List of dictionaries containing legislation metadata
        """
        legislation_items = []
        
        # Al Meezan URL patterns (may need adjustment based on actual site structure)
        category_urls = {
            'laws': f'{self.BASE_URL}/LawPage.aspx',
            'regulations': f'{self.BASE_URL}/RegulationsPage.aspx',
            'decisions': f'{self.BASE_URL}/DecisionsPage.aspx'
        }
        
        base_url = category_urls.get(category, category_urls['laws'])
        
        for page_num in range(1, max_pages + 1):
            logger.info(f"Scraping {category} page {page_num}...")
            
            # Construct URL with page number
            page_url = f"{base_url}?page={page_num}" if page_num > 1 else base_url
            soup = self.fetch_page(page_url)
            
            if not soup:
                logger.warning(f"Failed to fetch page {page_num}")
                continue
            
            # Extract legislation items from the page
            # Note: Selectors may need adjustment based on actual HTML structure
            items = soup.find_all('div', class_=['law-item', 'legislation-item']) or \
                    soup.find_all('tr', class_=['law-row', 'item-row']) or \
                    soup.find_all('a', href=re.compile(r'LawArticles|ViewLaw'))
            
            if not items:
                logger.info(f"No items found on page {page_num}, trying alternative selectors")
                # Try alternative extraction methods
                items = soup.find_all('a', href=True)
                items = [item for item in items if 'law' in item.get('href', '').lower() or 
                        'legislation' in item.get('href', '').lower()]
            
            for item in items:
                try:
                    legislation_data = self._parse_legislation_item(item, category)
                    if legislation_data:
                        legislation_items.append(legislation_data)
                except Exception as e:
                    logger.error(f"Error parsing item: {e}")
                    continue
            
            logger.info(f"Extracted {len(legislation_items)} items so far")
            
            # Check if there's a next page
            if not soup.find('a', class_=['next-page', 'pagination-next']):
                break
        
        return legislation_items
    
    def _parse_legislation_item(self, item, category: str) -> Optional[Dict]:
        """
        Parse individual legislation item
        
        Args:
            item: BeautifulSoup element
            category: Category of legislation
            
        Returns:
            Dictionary with legislation data
        """
        data = {
            'category': category,
            'title': '',
            'number': '',
            'year': '',
            'date': '',
            'url': '',
            'description': '',
            'status': 'active',
            'extracted_at': datetime.now().isoformat()
        }
        
        # Extract title
        title_elem = item.find(['h3', 'h4', 'span', 'strong']) or item
        data['title'] = title_elem.get_text(strip=True) if title_elem else ''
        
        # Extract URL
        if item.name == 'a':
            data['url'] = urljoin(self.BASE_URL, item.get('href', ''))
        else:
            link = item.find('a', href=True)
            if link:
                data['url'] = urljoin(self.BASE_URL, link.get('href', ''))
        
        # Extract number and year from title
        # Pattern: "قانون رقم (12) لسنة 2004" or "Law No. (12) of 2004"
        number_match = re.search(r'(?:رقم|No\.?)\s*\(?(\d+)\)?', data['title'])
        year_match = re.search(r'(?:لسنة|of|year)\s*(\d{4})', data['title'])
        
        if number_match:
            data['number'] = number_match.group(1)
        if year_match:
            data['year'] = year_match.group(1)
        
        # Extract date if available
        date_elem = item.find(['span', 'div'], class_=['date', 'publish-date'])
        if date_elem:
            data['date'] = date_elem.get_text(strip=True)
        
        # Extract description
        desc_elem = item.find(['p', 'div'], class_=['description', 'summary'])
        if desc_elem:
            data['description'] = desc_elem.get_text(strip=True)
        
        return data if data['title'] else None
    
    def extract_legislation_details(self, url: str) -> Optional[Dict]:
        """
        Extract detailed content of a legislation document
        
        Args:
            url: URL of the legislation document
            
        Returns:
            Dictionary with detailed legislation data
        """
        soup = self.fetch_page(url)
        if not soup:
            return None
        
        details = {
            'url': url,
            'full_text': '',
            'articles': [],
            'chapters': [],
            'metadata': {}
        }
        
        # Extract full text
        content_div = soup.find(['div', 'article'], class_=['content', 'law-content', 'main-content'])
        if content_div:
            details['full_text'] = content_div.get_text(separator='\n', strip=True)
        
        # Extract articles
        articles = soup.find_all(['div', 'section'], class_=['article', 'law-article'])
        for article in articles:
            article_data = {
                'number': '',
                'title': '',
                'text': article.get_text(strip=True)
            }
            
            # Extract article number
            article_num = article.find(['span', 'strong'], class_=['article-number', 'number'])
            if article_num:
                article_data['number'] = article_num.get_text(strip=True)
            
            details['articles'].append(article_data)
        
        # Extract chapters
        chapters = soup.find_all(['div', 'section'], class_=['chapter', 'law-chapter'])
        for chapter in chapters:
            chapter_data = {
                'number': '',
                'title': chapter.find(['h2', 'h3', 'strong']).get_text(strip=True) if chapter.find(['h2', 'h3', 'strong']) else '',
                'text': chapter.get_text(strip=True)
            }
            details['chapters'].append(chapter_data)
        
        # Extract metadata
        meta_fields = soup.find_all(['div', 'span'], class_=['meta', 'metadata', 'info'])
        for field in meta_fields:
            key = field.find(['strong', 'label'])
            if key:
                key_text = key.get_text(strip=True).rstrip(':')
                value_text = field.get_text(strip=True).replace(key_text, '').strip()
                details['metadata'][key_text] = value_text
        
        return details
    
    def scrape_all_categories(self, max_pages_per_category: int = 3) -> pd.DataFrame:
        """
        Scrape all categories of legislation
        
        Args:
            max_pages_per_category: Maximum pages to scrape per category
            
        Returns:
            pandas DataFrame with all legislation data
        """
        all_data = []
        categories = ['laws', 'regulations', 'decisions']
        
        for category in categories:
            logger.info(f"Scraping category: {category}")
            items = self.extract_legislation_list(category, max_pages_per_category)
            all_data.extend(items)
            logger.info(f"Total items collected: {len(all_data)}")
        
        df = pd.DataFrame(all_data)
        return df
    
    def preprocess_for_ml(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Preprocess data for machine learning
        
        Args:
            df: Raw dataframe
            
        Returns:
            Preprocessed DataFrame ready for ML
        """
        # Create a copy
        df_ml = df.copy()
        
        # Clean text fields
        text_columns = ['title', 'description']
        for col in text_columns:
            if col in df_ml.columns:
                df_ml[col] = df_ml[col].fillna('')
                df_ml[col] = df_ml[col].str.strip()
                # Remove extra whitespace
                df_ml[col] = df_ml[col].str.replace(r'\s+', ' ', regex=True)
        
        # Convert year to numeric
        if 'year' in df_ml.columns:
            df_ml['year'] = pd.to_numeric(df_ml['year'], errors='coerce')
        
        # Create category encoding
        if 'category' in df_ml.columns:
            df_ml['category_encoded'] = pd.Categorical(df_ml['category']).codes
        
        # Create text length features
        if 'title' in df_ml.columns:
            df_ml['title_length'] = df_ml['title'].str.len()
            df_ml['title_word_count'] = df_ml['title'].str.split().str.len()
        
        if 'description' in df_ml.columns:
            df_ml['description_length'] = df_ml['description'].str.len()
            df_ml['description_word_count'] = df_ml['description'].str.split().str.len()
        
        # Add temporal features
        if 'year' in df_ml.columns:
            current_year = datetime.now().year
            df_ml['years_since_publication'] = current_year - df_ml['year']
            df_ml['decade'] = (df_ml['year'] // 10) * 10
        
        # Remove duplicates
        df_ml = df_ml.drop_duplicates(subset=['title', 'number', 'year'], keep='first')
        
        return df_ml
    
    def save_data(self, df: pd.DataFrame, base_filename: str = 'qatar_legal_data'):
        """
        Save data in multiple formats
        
        Args:
            df: DataFrame to save
            base_filename: Base name for output files
        """
        # Save as CSV
        csv_file = f'{base_filename}.csv'
        df.to_csv(csv_file, index=False, encoding='utf-8-sig')
        logger.info(f"Saved CSV: {csv_file}")
        
        # Save as JSON
        json_file = f'{base_filename}.json'
        df.to_json(json_file, orient='records', force_ascii=False, indent=2)
        logger.info(f"Saved JSON: {json_file}")
        
        # Save preprocessed version
        df_ml = self.preprocess_for_ml(df)
        ml_csv_file = f'{base_filename}_ml_ready.csv'
        df_ml.to_csv(ml_csv_file, index=False, encoding='utf-8-sig')
        logger.info(f"Saved ML-ready CSV: {ml_csv_file}")
        
        # Save data schema
        schema = {
            'total_records': len(df),
            'columns': list(df.columns),
            'dtypes': {col: str(dtype) for col, dtype in df.dtypes.items()},
            'null_counts': df.isnull().sum().to_dict(),
            'sample_record': df.iloc[0].to_dict() if len(df) > 0 else {}
        }
        
        schema_file = f'{base_filename}_schema.json'
        with open(schema_file, 'w', encoding='utf-8') as f:
            json.dump(schema, f, indent=2, ensure_ascii=False, default=str)
        logger.info(f"Saved schema: {schema_file}")
        
        return {
            'csv': csv_file,
            'json': json_file,
            'ml_csv': ml_csv_file,
            'schema': schema_file
        }


def main():
    """Main execution function"""
    logger.info("Starting Al Meezan Qatar Legal Data Scraper")
    
    # Initialize scraper
    scraper = AlMeezanScraper(delay=1.0, language='ar')
    
    # Scrape data
    logger.info("Scraping all categories...")
    df = scraper.scrape_all_categories(max_pages_per_category=3)
    
    logger.info(f"Total records scraped: {len(df)}")
    logger.info(f"Columns: {list(df.columns)}")
    
    # Save data
    if len(df) > 0:
        files = scraper.save_data(df, 'qatar_legal_data')
        logger.info(f"Data saved successfully: {files}")
        
        # Display summary statistics
        logger.info("\n=== Data Summary ===")
        logger.info(f"Total records: {len(df)}")
        if 'category' in df.columns:
            logger.info(f"\nRecords by category:")
            logger.info(df['category'].value_counts().to_string())
        if 'year' in df.columns:
            logger.info(f"\nYear range: {df['year'].min()} - {df['year'].max()}")
    else:
        logger.warning("No data was scraped. Please check the website structure and selectors.")
    
    logger.info("Scraping completed!")


if __name__ == '__main__':
    main()
