"""
Quick Start Example - Al Meezan Qatar Legal Data Scraper
=========================================================

This script demonstrates basic usage of the scraper.
"""

from scraper import AlMeezanScraper
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def example_1_basic_scraping():
    """Example 1: Basic scraping of all categories"""
    print("\n" + "="*60)
    print("Example 1: Basic Scraping")
    print("="*60)
    
    # Initialize scraper
    scraper = AlMeezanScraper(delay=1.0, language='ar')
    
    # Scrape data (limited to 2 pages per category for demo)
    df = scraper.scrape_all_categories(max_pages_per_category=2)
    
    print(f"\nScraped {len(df)} records")
    
    if len(df) > 0:
        # Save data
        files = scraper.save_data(df, 'qatar_legal_data')
        print(f"\nFiles saved: {files}")
        
        # Display sample
        print(f"\nSample records:")
        print(df.head(3))
    
    return df


def example_2_specific_category():
    """Example 2: Scrape specific category only"""
    print("\n" + "="*60)
    print("Example 2: Scrape Laws Only")
    print("="*60)
    
    scraper = AlMeezanScraper(delay=1.0)
    
    # Scrape only laws
    laws = scraper.extract_legislation_list(category='laws', max_pages=3)
    
    print(f"\nFound {len(laws)} laws")
    
    if laws:
        print(f"\nFirst law: {laws[0]}")
    
    return laws


def example_3_preprocessing():
    """Example 3: Data preprocessing for ML"""
    print("\n" + "="*60)
    print("Example 3: ML Preprocessing")
    print("="*60)
    
    # Use sample data generator if scraping fails
    try:
        from sample_data_generator import generate_sample_data
        df = generate_sample_data(50)
        print("Using sample data for demonstration")
    except:
        scraper = AlMeezanScraper()
        df = scraper.scrape_all_categories(max_pages_per_category=1)
    
    if len(df) > 0:
        scraper = AlMeezanScraper()
        df_ml = scraper.preprocess_for_ml(df)
        
        print(f"\nML-ready dataset shape: {df_ml.shape}")
        print(f"\nColumns: {list(df_ml.columns)}")
        print(f"\nML features added:")
        ml_features = [col for col in df_ml.columns if col not in ['category', 'title', 'number', 'year', 'date', 'url', 'description', 'status', 'extracted_at']]
        for feature in ml_features:
            print(f"  - {feature}")
        
        # Save ML-ready data
        df_ml.to_csv('preprocessed_data.csv', index=False, encoding='utf-8-sig')
        print(f"\nML-ready data saved to 'preprocessed_data.csv'")
    
    return df_ml


def example_4_statistics():
    """Example 4: Generate statistics from scraped data"""
    print("\n" + "="*60)
    print("Example 4: Data Statistics")
    print("="*60)
    
    try:
        import pandas as pd
        df = pd.read_csv('qatar_legal_data_ml_ready.csv')
    except:
        # Use sample data
        from sample_data_generator import generate_sample_data
        df = generate_sample_data(100)
        print("Using sample data for demonstration")
    
    print(f"\n=== Dataset Summary ===")
    print(f"Total records: {len(df)}")
    
    if 'category' in df.columns:
        print(f"\n=== By Category ===")
        print(df['category'].value_counts())
    
    if 'year' in df.columns:
        print(f"\n=== By Year ===")
        print(f"Earliest: {df['year'].min()}")
        print(f"Latest: {df['year'].max()}")
        print(f"Mean: {df['year'].mean():.0f}")
    
    if 'title_length' in df.columns:
        print(f"\n=== Text Statistics ===")
        print(f"Average title length: {df['title_length'].mean():.1f} characters")
        print(f"Average word count: {df['title_word_count'].mean():.1f} words")
    
    return df


def main():
    """Run all examples"""
    print("\n" + "="*60)
    print("Al Meezan Qatar Legal Data Scraper - Examples")
    print("="*60)
    
    choice = input("\nChoose an example to run:\n"
                  "1. Basic scraping (all categories)\n"
                  "2. Scrape specific category (laws only)\n"
                  "3. Data preprocessing for ML\n"
                  "4. Generate statistics\n"
                  "5. Run all examples\n"
                  "\nEnter choice (1-5): ")
    
    examples = {
        '1': example_1_basic_scraping,
        '2': example_2_specific_category,
        '3': example_3_preprocessing,
        '4': example_4_statistics,
    }
    
    if choice == '5':
        # Run all examples
        for func in examples.values():
            try:
                func()
            except Exception as e:
                print(f"Error in example: {e}")
    elif choice in examples:
        try:
            examples[choice]()
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Invalid choice!")
    
    print("\n" + "="*60)
    print("Examples completed!")
    print("="*60)


if __name__ == '__main__':
    main()
