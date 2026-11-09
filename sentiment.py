import pandas as pd

# 1. Load your existing quotes dataset
df = pd.read_csv('quotes_dataset.csv')

# 2. Simple keyword-based sentiment analyzer (avoids NLTK/regex block)
positive_words = ['good', 'great', 'success', 'love', 'life', 'light', 'better', 'best', 'truth', 'free', 'smile']
negative_words = ['bad', 'wrong', 'hate', 'pain', 'hurt', 'dark', 'death', 'fail', 'sad', 'sorrow']

def get_simple_sentiment(text):
    text_lower = str(text).lower()
    pos_count = sum(word in text_lower for word in positive_words)
    neg_count = sum(word in text_lower for word in negative_words)
    
    if pos_count > neg_count:
        return 'Positive'
    elif neg_count > pos_count:
        return 'Negative'
    else:
        return 'Neutral'

# 3. Apply the sentiment analysis to every quote
df['Sentiment'] = df['Quote'].apply(get_simple_sentiment)

# 4. View the results
print("--- SENTIMENT ANALYSIS RESULTS ---")
print(df[['Quote', 'Author', 'Sentiment']].head(10))

# 5. Count the sentiments
print("\n--- SENTIMENT SUMMARY ---")
print(df['Sentiment'].value_counts())

# 6. Save the results to a new CSV file
df.to_csv('quotes_with_sentiment.csv', index=False)
print("\nNew dataset saved successfully as 'quotes_with_sentiment.csv'!")