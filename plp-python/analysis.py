import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

 
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

 
print("First 5 rows:")
print(df.head())

print("\nData types and missing values:")
print(df.info())
 
print("\nMissing values per column:")
print(df.isnull().sum())

 
print("\nBasic statistics:")
print(df.describe())

 
grouped = df.groupby('species')['petal length (cm)'].mean()
print("\nMean petal length by species:")
print(grouped)

# Step 7: Visualizations

# 1. Line chart  
plt.figure(figsize=(8,4))
plt.plot(df.index, df['sepal length (cm)'], label='Sepal length')
plt.title('Sepal Length Trend')
plt.xlabel('Sample index')
plt.ylabel('Sepal length (cm)')
plt.legend()
plt.show()

# 2. Bar chart 
plt.figure(figsize=(6,4))
grouped.plot(kind='bar', color='skyblue')
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Mean Petal Length (cm)')
plt.show()

# 3. Histogram of sepal width
plt.figure(figsize=(6,4))
plt.hist(df['sepal width (cm)'], bins=15, color='lightgreen')
plt.title('Sepal Width Distribution')
plt.xlabel('Sepal width (cm)')
plt.ylabel('Frequency')
plt.show()

# 4. Scatter plot 
plt.figure(figsize=(6,4))
species_colors = {'setosa':'red', 'versicolor':'green', 'virginica':'blue'}
for sp in df['species'].unique():
    subset = df[df['species'] == sp]
    plt.scatter(subset['sepal length (cm)'], subset['petal length (cm)'], label=sp, color=species_colors[sp])
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal length (cm)')
plt.ylabel('Petal length (cm)')
plt.legend()
plt.show()
