import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Sales Dashboard", layout="wide")

# 1. Title
st.title("📊 Sales Analytics Dashboard")
st.markdown("Explore the cleaned sales dataset and get key insights.")

# 2. Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("Cleaned_Sales_dataSet.csv")
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df.set_index('date', inplace=True)
    return df

df = load_data()

# Sidebar options
st.sidebar.header("Filters")
category_filter = st.sidebar.multiselect("Select Category", df['category'].unique(), default=df['category'].unique())
location_filter = st.sidebar.multiselect("Select Location", df['location'].unique(), default=df['location'].unique())
discount_filter = st.sidebar.selectbox("Discount Applied?", ["All", "True", "False"])

filtered_df = df[df['category'].isin(category_filter) & df['location'].isin(location_filter)]
if discount_filter != "All":
    filtered_df = filtered_df[filtered_df['discount_applied'] == discount_filter]

# 3. Dataset Overview
st.subheader("Dataset Overview")
st.dataframe(filtered_df.head())

st.write("**Columns & Data Types:**")
st.write(filtered_df.dtypes)

st.write("**Summary Statistics:**")
st.write(filtered_df.describe())

# 4. Total Revenue & Average Order Value
total_revenue = filtered_df['total_spent'].sum()
avg_order_value = filtered_df.groupby('transaction_id')['total_spent'].sum().mean()

st.subheader("💰 Key Metrics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"${total_revenue:,.2f}")
col2.metric("Average Order Value", f"${avg_order_value:,.2f}")
col3.metric("Unique Customers", filtered_df['customer_id'].nunique())
col4.metric("Total Transactions", len(filtered_df))

# 5. Sales by Product Category
st.subheader("📦 Sales by Product Category")
category_sales = filtered_df.groupby("category")["total_spent"].sum().sort_values()
fig, ax = plt.subplots(figsize=(10,6))
category_sales.plot(kind="bar", ax=ax)
ax.set_ylabel("Total Spent")
ax.set_xlabel("Category")
ax.set_title("Sales Amount by Product Category")
st.pyplot(fig)

# 6. Sales by Item
st.subheader("🛒 Sales by Product Item")
items_sales = filtered_df.groupby("item")["total_spent"].sum().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(20,6))
items_sales.plot(kind="bar", ax=ax)
ax.set_ylabel("Total Spent")
ax.set_xlabel("Item")
plt.xticks(rotation=90)
st.pyplot(fig)

# 7. Monthly Sales Trend
st.subheader("📈 Monthly Sales Trend")
monthly_sales = filtered_df['total_spent'].resample('ME').sum()
fig, ax = plt.subplots(figsize=(12,6))
monthly_sales.plot(kind='line', ax=ax)
ax.set_ylabel("Total Spent")
ax.set_xlabel("Month")
ax.set_title("Monthly Sales Trend")
st.pyplot(fig)

# 8. Sales by Location
st.subheader("🏠 Sales by Location")
location_sales = filtered_df.groupby("location")["total_spent"].sum().sort_values()
fig, ax = plt.subplots(figsize=(10,6))
location_sales.plot(kind="bar", ax=ax)
ax.set_ylabel("Total Spent")
ax.set_xlabel("Location")
st.pyplot(fig)

# 9. Impact of Discounts
st.subheader("🎯 Impact of Discounts")
discount_sales = filtered_df.groupby('discount_applied')['total_spent'].sum()
fig, ax = plt.subplots(figsize=(8,6))
discount_sales.plot(kind="bar", ax=ax)
ax.set_ylabel("Total Spent")
ax.set_xlabel("Discount Applied")
ax.set_title("Total Sales by Discount Applied")
st.pyplot(fig)

avg_discount_yes = filtered_df[filtered_df['discount_applied']=='True']['total_spent'].mean()
avg_discount_no = filtered_df[filtered_df['discount_applied']=='False']['total_spent'].mean()
st.write(f"Average Sales with Discount: ${avg_discount_yes:,.2f}")
st.write(f"Average Sales without Discount: ${avg_discount_no:,.2f}")

# 10. Correlation Heatmap
st.subheader("🧩 Correlation Between Numeric Variables")
numeric_cols = filtered_df[['total_spent', 'quantity', 'price_per_unit']]
fig, ax = plt.subplots(figsize=(8,6))
sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm', ax=ax)
ax.set_title("Correlation Heatmap")
st.pyplot(fig)

# 11. Top Customers by Lifetime Value
st.subheader("👑 Top Customers by Lifetime Value")
customer_value = filtered_df.groupby('customer_id')['total_spent'].sum().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(12,6))
customer_value.plot(kind='bar', ax=ax)
ax.set_ylabel("Total Spent")
ax.set_xlabel("Customer ID")
ax.set_title("Total Spent by Customer")
st.pyplot(fig)
st.write("Top 10 Customers:")
st.write(customer_value.head(10))

# 12. Payment Method Distribution
st.subheader("💳 Payment Method Distribution")
payment_sales = filtered_df.groupby('payment_method')['total_spent'].sum()
fig, ax = plt.subplots(figsize=(8,8))
payment_sales.plot(kind='pie', autopct='%1.1f%%', ax=ax)
ax.set_ylabel("")
st.pyplot(fig)

# 13. Summary
st.subheader("📝 Summary of Key Findings")
st.markdown("""
- **Top Categories:** Furniture & Electronics  
- **Channel:** Online dominates (~84%)  
- **Discounts:** Don’t increase basket size  
- **Sales spike:** Late 2023  
- **VIP Customers:** Top 10 drive major revenue  
- **Payment Preference:** Digital wallets
""")
st.markdown("✅ Recommendations: Revise discount strategy, investigate growth spike, launch loyalty program, optimize categories, improve in-store sales, streamline digital payments.")
