# Sales Data Analytics Project using Python

## Project overview
This beginner-friendly data analytics project analyzes a synthetic retail sales dataset using Python, Pandas, and Matplotlib. It explores revenue, profit, monthly trends, product categories, regions, and sales channels.

## Folder structure
- `data/sales_data.csv` — 500 sample orders (synthetic educational data)
- `sales_analysis.py` — complete analysis script
- `outputs/` — generated summaries and charts after running the script
- `project_report.docx` — editable project report

## Requirements
- Python 3.9+
- pandas
- matplotlib
- python-docx (only needed if regenerating the report)

Install the analysis libraries:
```bash
pip install pandas matplotlib
```

## How to run
1. Extract the ZIP file.
2. Open a terminal in the project folder.
3. Run `python sales_analysis.py`.
4. Review the `outputs/` folder for CSV summaries and PNG charts.

## Analysis questions
1. What are total revenue and total profit?
2. Which product category earns the most revenue?
3. Which region generates the highest revenue?
4. How do revenue and profit change month by month?
5. Which sales channel contributes more revenue?
6. What is the overall profit margin?

## Methodology
1. Load the CSV dataset with Pandas.
2. Check missing values and duplicate order IDs.
3. Remove duplicate orders and rows with missing critical fields.
4. Create a month feature from the order date.
5. Calculate KPIs and group sales by month, category, region, and channel.
6. Export summary tables and create charts with Matplotlib.

## Important note
The data is simulated, not real company data. Treat the results as a demonstration of the analytics workflow, not as evidence about an actual retailer.
