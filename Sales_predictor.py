import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set styling for better visualizations
plt.style.use('seaborn-v0_8')
sns.set_theme()

# Load the Advertising dataset
df = pd.read_csv('Advertising.csv')

# If there's an unnamed index column, drop it
if 'Unnamed: 0' in df.columns:
    df = df.drop('Unnamed: 0', axis=1)

# Create visualizations
# 1. Correlation Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap', pad=20, size=14)
plt.tight_layout()
plt.show()

# 2. Regression plots with confidence intervals
fig, axes = plt.subplots(1, 3, figsize=(20, 6))
fig.suptitle('Relationship between Advertising Channels and Sales', size=14)

# TV vs Sales
sns.regplot(data=df, x='TV', y='Sales', ax=axes[0])
axes[0].set_title('TV Advertising vs Sales')

# Radio vs Sales
sns.regplot(data=df, x='Radio', y='Sales', ax=axes[1])
axes[1].set_title('Radio Advertising vs Sales')

# Newspaper vs Sales
sns.regplot(data=df, x='Newspaper', y='Sales', ax=axes[2])
axes[2].set_title('Newspaper Advertising vs Sales')

plt.tight_layout()
plt.show()

# Print statistical summary
print("\nStatistical Summary of the Data:")
print(df.describe())

# Print correlation with sales
print("\nCorrelation with Sales:")
correlations = df.corr()['Sales'].sort_values(ascending=False)
print(correlations)