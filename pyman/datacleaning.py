import pandas as pd

data = {
    'Name': ['Manu', 'Maggi', 'Kalpu', 'Sree', 'John', 'None'],
    'Age': [23,30,None,35,29,37],
    'City': ['Los  Anageles', 'New York', 'Chicago', 'New York', 'Los Anageles','Chicago'],
    'Salary': [70000,60000,75000,85000,80000,70000]
}
df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Name'] = df['Name'].fillna(df['Name'].mode()[0])

df['City'] = df['City'].replace('Los Anageles', ' Los Anageles')

print("\nDataset after handling missing values:")
print(df)

df = df.drop_duplicates()

print("\nDataset after removing duplicates:")
print(df)

df.columns = df.columns.str.strip().str.lower().str.replace(' ','_')

print("\nDataset after standardizing columns names:")
print(df)

df['age'] = pd.to_numeric(df['age'],errors = 'coerce')
df['salary'] = pd.to_numeric(df['salary'],errors = 'coerce')

df = df[df['salary'] >= 50000]

print("\nDataset after removing outliers:")
print(df)

print("\nFinal cleaned dataset:")
print(df)

