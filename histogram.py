import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Gender Inequality Index.csv", encoding="latin1")

gii = pd.to_numeric(df["GII VALUE"], errors="coerce")

plt.figure(figsize=(8,5))
plt.hist(gii.dropna(), bins=15)

plt.title("Distribution of Gender Inequality Index")
plt.xlabel("GII Value")
plt.ylabel("Number of Countries")

plt.show()