"""
Sales Data Analytics Project
Run: python sales_analysis.py
Outputs: summary CSV files and PNG charts in the outputs/ folder.
Dataset is synthetic and intended for educational use.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "sales_data.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH, parse_dates=["Date"])

# 1. Data quality checks
print("DATASET OVERVIEW")
print("-" * 60)
print(df.head())
print("\nShape:", df.shape)
print("\nMissing values:\n", df.isna().sum())
print("\nDuplicate order IDs:", df["Order_ID"].duplicated().sum())

# 2. Clean data
df = df.drop_duplicates(subset="Order_ID")
df = df.dropna(subset=["Date", "Category", "Revenue_INR", "Profit_INR"])
df = df[df["Quantity"] > 0]
df["Month"] = df["Date"].dt.to_period("M").astype(str)

# 3. Key performance indicators
kpis = pd.DataFrame({
    "Metric": ["Total Orders", "Total Units Sold", "Total Revenue (INR)",
               "Total Cost (INR)", "Total Profit (INR)", "Average Order Value (INR)",
               "Overall Profit Margin (%)"],
    "Value": [
        df["Order_ID"].nunique(),
        int(df["Quantity"].sum()),
        round(df["Revenue_INR"].sum(), 2),
        round(df["Cost_INR"].sum(), 2),
        round(df["Profit_INR"].sum(), 2),
        round(df["Revenue_INR"].mean(), 2),
        round(df["Profit_INR"].sum() / df["Revenue_INR"].sum() * 100, 2)
    ]
})
kpis.to_csv(OUT / "kpi_summary.csv", index=False)

# 4. Grouped analysis
monthly = df.groupby("Month", as_index=False).agg(
    Revenue_INR=("Revenue_INR", "sum"),
    Profit_INR=("Profit_INR", "sum"),
    Orders=("Order_ID", "nunique")
)
category = df.groupby("Category", as_index=False).agg(
    Revenue_INR=("Revenue_INR", "sum"),
    Profit_INR=("Profit_INR", "sum"),
    Units_Sold=("Quantity", "sum")
).sort_values("Revenue_INR", ascending=False)
region = df.groupby("Region", as_index=False).agg(
    Revenue_INR=("Revenue_INR", "sum"),
    Profit_INR=("Profit_INR", "sum"),
    Orders=("Order_ID", "nunique")
).sort_values("Revenue_INR", ascending=False)
channel = df.groupby("Sales_Channel", as_index=False).agg(
    Revenue_INR=("Revenue_INR", "sum"),
    Profit_INR=("Profit_INR", "sum"),
    Orders=("Order_ID", "nunique")
)

monthly.to_csv(OUT / "monthly_summary.csv", index=False)
category.to_csv(OUT / "category_summary.csv", index=False)
region.to_csv(OUT / "region_summary.csv", index=False)
channel.to_csv(OUT / "channel_summary.csv", index=False)

# 5. Visualizations
plt.figure(figsize=(10, 5))
plt.plot(monthly["Month"], monthly["Revenue_INR"], marker="o", label="Revenue")
plt.plot(monthly["Month"], monthly["Profit_INR"], marker="s", label="Profit")
plt.title("Monthly Revenue and Profit")
plt.xlabel("Month")
plt.ylabel("Amount (INR)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig(OUT / "monthly_revenue_profit.png", dpi=160)
plt.close()

plt.figure(figsize=(8, 5))
plt.bar(category["Category"], category["Revenue_INR"])
plt.title("Revenue by Product Category")
plt.xlabel("Category")
plt.ylabel("Revenue (INR)")
plt.xticks(rotation=20, ha="right")
plt.tight_layout()
plt.savefig(OUT / "revenue_by_category.png", dpi=160)
plt.close()

plt.figure(figsize=(8, 5))
plt.bar(region["Region"], region["Revenue_INR"])
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue (INR)")
plt.tight_layout()
plt.savefig(OUT / "revenue_by_region.png", dpi=160)
plt.close()

plt.figure(figsize=(7, 5))
plt.bar(channel["Sales_Channel"], channel["Revenue_INR"])
plt.title("Revenue by Sales Channel")
plt.xlabel("Sales Channel")
plt.ylabel("Revenue (INR)")
plt.tight_layout()
plt.savefig(OUT / "revenue_by_channel.png", dpi=160)
plt.close()

print("\nKPI SUMMARY")
print(kpis.to_string(index=False))
print("\nCategory summary:\n", category.to_string(index=False))
print("\nRegion summary:\n", region.to_string(index=False))
print(f"\nAnalysis complete. Results saved to: {OUT}")
