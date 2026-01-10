"""
Sample Data Generator for Testing
==================================
This module generates sample legal data for testing purposes when the website is not accessible.
"""

import pandas as pd
import random
from datetime import datetime, timedelta

def generate_sample_data(n_records: int = 100) -> pd.DataFrame:
    """
    Generate sample legal data for testing
    
    Args:
        n_records: Number of sample records to generate
        
    Returns:
        DataFrame with sample legal data
    """
    
    categories = ['laws', 'regulations', 'decisions']
    
    # Arabic legal terms (sample)
    law_topics = [
        'التجارة', 'العمل', 'الصحة', 'التعليم', 'البيئة',
        'النقل', 'الإسكان', 'الاستثمار', 'الضرائب', 'الجمارك',
        'الأمن', 'العدل', 'الإعلام', 'الثقافة', 'الرياضة'
    ]
    
    law_types = [
        'قانون', 'لائحة', 'قرار', 'نظام', 'مرسوم'
    ]
    
    data = []
    
    for i in range(n_records):
        # Generate random year
        year = random.randint(1990, 2024)
        
        # Generate random date
        start_date = datetime(year, 1, 1)
        end_date = datetime(year, 12, 31)
        random_date = start_date + timedelta(
            seconds=random.randint(0, int((end_date - start_date).total_seconds()))
        )
        
        # Generate category
        category = random.choice(categories)
        
        # Generate law number
        law_number = str(random.randint(1, 200))
        
        # Generate title
        law_type = random.choice(law_types)
        topic = random.choice(law_topics)
        title = f"{law_type} رقم ({law_number}) لسنة {year} بشأن {topic}"
        
        # Generate description
        description = f"ينظم هذا {law_type} الأحكام المتعلقة ب{topic} في دولة قطر"
        
        record = {
            'category': category,
            'title': title,
            'number': law_number,
            'year': year,
            'date': random_date.strftime('%Y-%m-%d'),
            'url': f'https://almeezan.qa/LawArticles.aspx?lawID={i+1000}',
            'description': description,
            'status': random.choice(['active', 'active', 'active', 'amended']),
            'extracted_at': datetime.now().isoformat()
        }
        
        data.append(record)
    
    df = pd.DataFrame(data)
    
    # Add ML features
    df['title_length'] = df['title'].str.len()
    df['title_word_count'] = df['title'].str.split().str.len()
    df['description_length'] = df['description'].str.len()
    df['description_word_count'] = df['description'].str.split().str.len()
    df['category_encoded'] = pd.Categorical(df['category']).codes
    df['years_since_publication'] = datetime.now().year - df['year']
    df['decade'] = (df['year'] // 10) * 10
    
    return df


if __name__ == '__main__':
    print("Generating sample data...")
    df = generate_sample_data(100)
    
    # Save sample data
    df.to_csv('qatar_legal_data_sample.csv', index=False, encoding='utf-8-sig')
    df.to_json('qatar_legal_data_sample.json', orient='records', force_ascii=False, indent=2)
    
    print(f"Generated {len(df)} sample records")
    print(f"\nSample data preview:")
    print(df.head())
    print(f"\nCategory distribution:")
    print(df['category'].value_counts())
    print(f"\nFiles saved:")
    print("- qatar_legal_data_sample.csv")
    print("- qatar_legal_data_sample.json")
