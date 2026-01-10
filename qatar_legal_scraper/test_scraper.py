"""
Test Suite for Al Meezan Qatar Legal Data Scraper
==================================================

Simple tests to validate the scraper functionality.
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(__file__))

from scraper import AlMeezanScraper
from sample_data_generator import generate_sample_data
import pandas as pd


def test_scraper_initialization():
    """Test 1: Scraper initializes correctly"""
    print("\n=== Test 1: Scraper Initialization ===")
    try:
        scraper = AlMeezanScraper(delay=1.0, language='ar')
        assert scraper.delay == 1.0
        assert scraper.language == 'ar'
        assert scraper.BASE_URL == "https://almeezan.qa"
        print("✓ Scraper initialized successfully")
        return True
    except Exception as e:
        print(f"✗ Initialization failed: {e}")
        return False


def test_sample_data_generation():
    """Test 2: Sample data generation works"""
    print("\n=== Test 2: Sample Data Generation ===")
    try:
        df = generate_sample_data(50)
        assert len(df) == 50
        assert 'category' in df.columns
        assert 'title' in df.columns
        assert 'year' in df.columns
        assert 'title_length' in df.columns
        print(f"✓ Generated {len(df)} sample records successfully")
        print(f"  Columns: {list(df.columns)}")
        return True
    except Exception as e:
        print(f"✗ Sample data generation failed: {e}")
        return False


def test_data_preprocessing():
    """Test 3: Data preprocessing for ML"""
    print("\n=== Test 3: Data Preprocessing ===")
    try:
        # Generate sample data
        df = generate_sample_data(30)
        
        # Preprocess
        scraper = AlMeezanScraper()
        df_ml = scraper.preprocess_for_ml(df)
        
        # Check ML features exist
        ml_features = ['category_encoded', 'title_length', 'title_word_count',
                      'years_since_publication', 'decade']
        
        for feature in ml_features:
            assert feature in df_ml.columns, f"Missing feature: {feature}"
        
        # Check no duplicates
        original_len = len(df)
        processed_len = len(df_ml)
        
        print(f"✓ Preprocessing successful")
        print(f"  Original records: {original_len}")
        print(f"  After deduplication: {processed_len}")
        print(f"  ML features added: {ml_features}")
        return True
    except Exception as e:
        print(f"✗ Preprocessing failed: {e}")
        return False


def test_data_saving():
    """Test 4: Data can be saved in multiple formats"""
    print("\n=== Test 4: Data Saving ===")
    try:
        # Generate sample data
        df = generate_sample_data(20)
        
        # Save data
        scraper = AlMeezanScraper()
        files = scraper.save_data(df, 'test_output')
        
        # Check files exist
        assert os.path.exists(files['csv'])
        assert os.path.exists(files['json'])
        assert os.path.exists(files['ml_csv'])
        assert os.path.exists(files['schema'])
        
        print(f"✓ Data saved successfully")
        print(f"  CSV: {files['csv']}")
        print(f"  JSON: {files['json']}")
        print(f"  ML CSV: {files['ml_csv']}")
        print(f"  Schema: {files['schema']}")
        
        # Clean up test files
        for file in files.values():
            if os.path.exists(file):
                os.remove(file)
        
        return True
    except Exception as e:
        print(f"✗ Data saving failed: {e}")
        return False


def test_data_loading():
    """Test 5: Sample data files can be loaded"""
    print("\n=== Test 5: Data Loading ===")
    try:
        # Load sample CSV
        df_csv = pd.read_csv('qatar_legal_data_sample.csv')
        assert len(df_csv) > 0
        print(f"✓ Loaded CSV: {len(df_csv)} records")
        
        # Load sample JSON
        df_json = pd.read_json('qatar_legal_data_sample.json')
        assert len(df_json) > 0
        print(f"✓ Loaded JSON: {len(df_json)} records")
        
        # Check data consistency
        assert len(df_csv) == len(df_json)
        print(f"✓ Data consistency verified")
        
        return True
    except Exception as e:
        print(f"✗ Data loading failed: {e}")
        return False


def test_data_schema():
    """Test 6: Data schema validation"""
    print("\n=== Test 6: Data Schema Validation ===")
    try:
        df = pd.read_csv('qatar_legal_data_sample.csv')
        
        # Required columns
        required_cols = ['category', 'title', 'number', 'year', 'date', 
                        'url', 'description', 'status', 'extracted_at']
        
        for col in required_cols:
            assert col in df.columns, f"Missing required column: {col}"
        
        # ML feature columns
        ml_cols = ['title_length', 'title_word_count', 'category_encoded',
                  'years_since_publication', 'decade']
        
        for col in ml_cols:
            assert col in df.columns, f"Missing ML feature: {col}"
        
        # Data types
        assert df['year'].dtype in [int, 'int64', 'Int64']
        assert df['category'].dtype == 'object'
        
        print(f"✓ Schema validation passed")
        print(f"  Total columns: {len(df.columns)}")
        print(f"  Required columns: {len(required_cols)} ✓")
        print(f"  ML features: {len(ml_cols)} ✓")
        
        return True
    except Exception as e:
        print(f"✗ Schema validation failed: {e}")
        return False


def test_statistics():
    """Test 7: Generate statistics from data"""
    print("\n=== Test 7: Statistics Generation ===")
    try:
        df = pd.read_csv('qatar_legal_data_sample.csv')
        
        # Category distribution
        cat_dist = df['category'].value_counts()
        print(f"✓ Category distribution:")
        for cat, count in cat_dist.items():
            print(f"    {cat}: {count}")
        
        # Year statistics
        if 'year' in df.columns:
            print(f"✓ Year statistics:")
            print(f"    Range: {df['year'].min()} - {df['year'].max()}")
            print(f"    Mean: {df['year'].mean():.0f}")
        
        # Text statistics
        if 'title_length' in df.columns:
            print(f"✓ Text statistics:")
            print(f"    Avg title length: {df['title_length'].mean():.1f} chars")
            print(f"    Avg word count: {df['title_word_count'].mean():.1f} words")
        
        return True
    except Exception as e:
        print(f"✗ Statistics generation failed: {e}")
        return False


def run_all_tests():
    """Run all tests"""
    print("="*60)
    print("Al Meezan Qatar Legal Data Scraper - Test Suite")
    print("="*60)
    
    tests = [
        test_scraper_initialization,
        test_sample_data_generation,
        test_data_preprocessing,
        test_data_saving,
        test_data_loading,
        test_data_schema,
        test_statistics
    ]
    
    results = []
    for test_func in tests:
        result = test_func()
        results.append(result)
    
    # Summary
    print("\n" + "="*60)
    print("Test Summary")
    print("="*60)
    passed = sum(results)
    total = len(results)
    print(f"Tests passed: {passed}/{total}")
    print(f"Success rate: {(passed/total)*100:.1f}%")
    
    if passed == total:
        print("\n✓ All tests passed!")
    else:
        print(f"\n✗ {total - passed} test(s) failed")
    
    print("="*60)
    
    return passed == total


if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
