import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
df = pd.read_csv("Gender Inequality Index.csv", encoding="latin1")

# Count countries in each Human Development category
counts = df["HUMAN DEVELOPMENT"].value_counts()

# Create bar chart
plt.figure(figsize=(8, 5))
counts.plot(kind="bar")

plt.title("Distribution of Human Development Categories")
plt.xlabel("Human Development Category")
plt.ylabel("Number of Countries")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
