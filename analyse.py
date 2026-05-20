import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Users\vignesh.m\OneDrive\Attachments\project 1\car sales data.xlsx"

df = pd.read_excel(file_path)

print("\n--- DATA PREVIEW ---")
print(df.head())


df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month_name()


total_revenue = df['Revenue (INR)'].sum()
total_units = df['Units Sold'].sum()
avg_revenue = df['Revenue (INR)'].mean()

print("\n--- KPI METRICS ---")
print("Total Revenue:", total_revenue)
print("Total Units Sold:", total_units)
print("Average Revenue:", avg_revenue)

top_models = df.groupby('Car Model')['Units Sold'].sum().sort_values(ascending=False)

print("\n--- TOP CAR MODELS ---")
print(top_models)

plt.figure()
top_models.head(10).plot(kind='bar')
plt.title("Top 10 Car Models by Sales")
plt.ylabel("Units Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()