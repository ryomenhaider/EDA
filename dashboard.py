# sales_dashboard.py

import streamlit as st
import pandas as pd
import numpy as np

# -------------------------
# 1. App Title
# -------------------------
st.title("📊 Sales Analytics Dashboard")
st.markdown(
    """
    This dashboard provides interactive visualizations and KPIs for your sales dataset.
    """
)

# -------------------------
# 2. Load Dataset
# -------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("Cleaned_Sales_dataSet.csv")
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df.set_index('date', inplace=True)
    return df

df = load_data()

st.subheader("Raw Data")
st.dataframe(df.head(10))

# -------------------------
# 3. Dataset Info & Stats
# -------------------------
st.subheader("Dataset Overview")
st.write("Number of Transactions:", len(df))
st.write("Total Revenue: $", df['total_spent'].sum())
st.write("Average Order Value (AOV): $", df.groupby('transaction_id')['total_spent'].sum().mean())
st.write("Number of Unique Customers:", df['customer_id'].nunique())
st.write("Time Period:", df.index.min(), "to", df.index.max())
st.write("Unique Categories:", df['category'].unique())
st.write("Unique Items:", df['item'].unique())
st.write("Unique Locations:", df['location'].unique())
st.write("Unique Payment Methods:", df['payment_method'].unique())

# -------------------------
# 4. Sales by Product Category
# -------------------------
st.subheader("💼 Sales by Product Category")
category_sales = df.groupby("category")["total_spent"].sum().sort_values(ascending=False)
st.bar_chart(category_sales)

# -------------------------
# 5. Sales by Individual Item
# -------------------------
st.subheader("🛒 Sales by Item")
items_sales = df.groupby("item")["total_spent"].sum().sort_values(ascending=False)
st.bar_chart(items_sales)

# -------------------------
# 6. Monthly Sales Trend
# -------------------------
st.subheader("📈 Monthly Sales Trend")
monthly_sales = df['total_spent'].resample('M').sum()
st.line_chart(monthly_sales)

# -------------------------
# 7. Sales by Location
# -------------------------
st.subheader("📍 Sales by Location")
location_sales = df.groupby("location")["total_spent"].sum().sort_values(ascending=False)
st.bar_chart(location_sales)

# -------------------------
# 8. Discounts Impact
# -------------------------
st.subheader("💸 Impact of Discounts on Sales")
discount_sales = df.groupby('discount_applied')['total_spent'].sum()
st.bar_chart(discount_sales)

discountYesMean = df[df['discount_applied'] == 'True']['total_spent'].mean()
discountNoMean = df[df['discount_applied'] == 'False']['total_spent'].mean()

st.write(f"Average Sales with Discount: ${discountYesMean:,.2f}")
st.write(f"Average Sales without Discount: ${discountNoMean:,.2f}")

# -------------------------
# 9. Correlation Between Numeric Variables
# -------------------------
st.subheader("📊 Correlation Heatmap")
numeric_cols = df[['total_spent', 'quantity', 'price_per_unit']]
st.dataframe(numeric_cols.corr())

# -------------------------
# 10. Top Customers
# -------------------------
st.subheader("🏆 Top Customers by Lifetime Value")
customer_value = df.groupby('customer_id')['total_spent'].sum().sort_values(ascending=False)
st.bar_chart(customer_value)
st.write("Top 10 Customers:")
st.dataframe(customer_value.head(10))

# -------------------------
# 11. Payment Method Distribution
# -------------------------
st.subheader("💳 Payment Method Distribution")
payment_distribution = df.groupby('payment_method')['total_spent'].sum()
st.bar_chart(payment_distribution)

# -------------------------
# 12. Summary & Recommendations
# -------------------------
st.subheader("📌 Summary of Key Findings")
st.markdown("""
**Key Insights:**
- Furniture & Electronics are top categories; Patisserie underperforms.
- Online sales dominate (~84% of revenue).
- Discounts reduce margin, don’t increase basket size.
- Sales spiked in late 2023 — investigate the cause.
- Top 10 customers drive massive revenue — VIP retention needed.
- Digital wallets are preferred — optimize checkout.

**Recommendations:**
- Revise discount strategy
- Investigate 2023 growth spike
- Launch VIP loyalty program
- Optimize category mix
- Improve in-store strategy
- Streamline digital wallet payments
""")
