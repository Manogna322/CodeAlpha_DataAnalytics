import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
df = pd.read_csv('quotes_dataset.csv')

# 2. View basic info
print("--- DATA INFO ---")
print(df.info())

# 3. Exploratory Data Analysis: Count quotes per author
print("\n--- TOP AUTHORS ---")
author_counts = df['Author'].value_counts()
print(author_counts)

# 4. Create a simple chart to visualize the data
plt.figure(figsize=(10, 5))
sns.barplot(x=author_counts.index[:5], y=author_counts.values[:5], palette='viridis')
plt.title('Top 5 Authors by Number of Quotes')
plt.xlabel('Author')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()

# Save and show the plot
plt.savefig('top_authors.png')
print("\nChart saved successfully as 'top_authors.png'!")
plt.show()