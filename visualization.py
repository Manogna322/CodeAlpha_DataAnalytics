import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load your dataset
df = pd.read_csv('quotes_dataset.csv')

# 2. Set the style for clean, professional charts
sns.set_theme(style="whitegrid")

# 3. Create a Count Plot for Authors
plt.figure(figsize=(12, 6))
ax = sns.countplot(data=df, x='Author', order=df['Author'].value_counts().index, palette='crest')

# Customize chart labels and title
plt.title('Distribution of Quotes per Author', fontsize=16, fontweight='bold')
plt.xlabel('Author Name', fontsize=12)
plt.ylabel('Number of Quotes', fontsize=12)
plt.xticks(rotation=45, ha='right')

# Add values on top of the bars for clarity
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='bottom', fontsize=10, color='black', xytext=(0, 3), 
                textcoords='offset points')

plt.tight_layout()

# 4. Save and show the visualization
plt.savefig('author_quotes_visualization.png')
print("Advanced visualization saved successfully as 'author_quotes_visualization.png'!")
plt.show()