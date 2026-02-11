# Exploratory Data Analysis Report: Retail Sales Dataset

## 1. Executive Summary

This report analyzes a retail sales dataset containing **11,362 transactions** over a period spanning **2022 to 2024**.

- **Total Revenue:** **$1.47M** was generated across 8 distinct product categories.
- **Top Performers:** **Furniture** and **Electric household essentials** are the highest-grossing categories. **Online sales** dominate the market, accounting for the vast majority of revenue.
- **Customer Behavior:** The average transaction value is **$129.64**. Discounts appear to have a **negligible impact** on average order size, suggesting they may not be effectively driving larger purchases but do contribute to nearly half of total sales.
- **Key Findings:** Sales show strong seasonality with a significant peak in **late 2023/early 2024**. A small number of customers contribute a disproportionately large share of revenue.

---

## 2. Key Business Questions & Answers

### Q1: What are our best and worst-performing product categories and items?
**Answer:** 
- **Furniture** is the top category by total sales, followed closely by **Electric household essentials**. 
- **Patisserie** is the lowest-performing category. 
- At the item level, `Item_2_BEV` is the most frequently sold item, while `Item_3_EHE` is the least sold.

### Q2: How do sales performance and customer spending differ by location?
**Answer:** 
- **Online** channels are the dominant source of revenue, generating **$1.23M** compared to **$0.24M** for **In-store** sales. 
- This indicates a strong digital preference among your customer base.

### Q3: Are promotions/discounts effective at increasing sales value?
**Answer:** 
- **No.** The average transaction value with a discount ($130.72) is **virtually identical** to the average without a discount ($130.13). 
- This strongly suggests that discounts are being applied to transactions that would have occurred anyway, rather than incentivizing customers to spend more. 
- While discounts are applied to a significant portion of sales, they are not driving higher basket sizes.

### Q4: Who are our most valuable customers?
**Answer:**
Customer segmentation reveals a clear top tier:
- **Customer `CUST_24`** is the highest spender at over **$64,608**
- Followed by `CUST_05`, `CUST_16`, and `CUST_13`
- These top 10 customers represent a massive concentration of revenue and are critical for retention efforts.

### Q5: Are there any seasonal trends in our sales data?
**Answer:**
- **Yes.** There is a clear and dramatic upward trend in monthly sales starting in **late 2023**, peaking sharply in **early 2024**.
- This could be due to successful holiday campaigns, new product launches, or overall business growth. This is a key period to analyze further.

### Q6: What factors are most correlated with high `total_spent`?
**Answer:**
- The heatmap shows a **very strong positive correlation (0.78)** between `quantity` and `total_spent`. 
- Unsurprisingly, buying more items leads to spending more money.
- Interestingly, `price_per_unit` has a **very weak correlation** with `total_spent`. 
- This indicates that customers are not necessarily buying more expensive items to increase their order value; they are buying in higher volumes.

---

## 3. Visual Analysis & Insights

### 3.1 Sales by Category & Item
**Visual:** Bar charts of `total_spent` by category and item.

**Insight:** There is a clear performance hierarchy. Focus inventory and marketing efforts on high-performing categories like Furniture and Electronics. Investigate the low sales in the Patisserie category—is it a pricing, placement, or demand issue?

### 3.2 Monthly Sales Trend
**Visual:** Line chart of `total_spent` over time.

**Insight:** **This is the most critical finding.** The sales trend is not flat; it shows exponential growth in the final months of the dataset.

**Action:** Immediately investigate the drivers of this peak. Was it a specific marketing campaign, a new product release, or a seasonal event? Replicating this success should be a top priority.

### 3.3 Sales by Location
**Visual:** Bar chart comparing Online vs. In-store sales.

**Insight:** The business is overwhelmingly digital-first.

**Action:** While maintaining a strong online presence, consider strategies to drive in-store traffic, such as "buy online, pick up in-store" (BOPIS) or in-store exclusive promotions.

### 3.4 Impact of Discounts
**Visual:** Bar chart comparing sales with/without discounts and correlation analysis.

**Insight:** Discounts are **cannibalizing revenue** without increasing order value. The total sales with discounts ($496k) and without ($491k) are nearly equal, but the average order size is the same. This means you are giving up profit margin unnecessarily.

**Action:** Re-evaluate your discounting strategy. Consider shifting from blanket percentage discounts to "Spend $X, get $Y off" promotions to genuinely increase basket size, or limit discounts to moving excess inventory.

### 3.5 Customer Value Analysis
**Visual:** Bar chart of total spent per customer.

**Insight:** Your revenue is heavily dependent on a small cohort of high-value customers.

**Action:** Implement a **VIP loyalty program** for the top 10-20 customers. Personalized outreach, early access to new products, and dedicated customer service can help retain these key accounts.

### 3.6 Payment Method Preference
**Visual:** Pie chart of sales by payment method.

**Insight:** **Digital Wallets** (e.g., Apple Pay, Google Pay, PayPal) are the preferred method of payment, accounting for nearly half of all transactions. Credit Cards are second.

**Action:** Ensure your checkout process is optimized for digital wallets to reduce friction. Investigate the relatively low usage of Cash to see if it can be de-emphasized or if accepting it is still cost-effective.

---

## 4. Summary of Recommendations

| # | Recommendation | Expected Impact |
|---|----------------|-----------------|
| 1 | **Revise Discount Strategy:** Immediately test removing discounts or changing the offer structure to "minimum spend" thresholds | Protect profit margins and increase basket size |
| 2 | **Leverage Seasonal Success:** Deep-dive into the sales data from late 2023/early 2024 to identify the "secret sauce" | Build a replicable marketing playbook for future campaigns |
| 3 | **Focus on Retention:** Launch a targeted retention campaign for top 10 customers by lifetime value | Increase customer lifetime value (CLV) and reduce churn |
| 4 | **Category Management:** Investigate underperforming categories (Patisserie); prioritize inventory for top categories (Furniture, Electronics) | Optimize product mix and inventory turnover |
| 5 | **Channel Strategy:** Optimize online experience while testing low-cost strategies to drive in-store foot traffic | Maximize revenue across all channels |
| 6 | **Checkout Optimization:** Prioritize Digital Wallet integration and streamline the payment process | Reduce cart abandonment, improve conversion rates |

---

## 5. Key Metrics Summary

| Metric | Value |
|--------|-------|
| **Total Revenue** | $1,472,998.50 |
| **Total Transactions** | 11,362 |
| **Average Order Value** | $129.64 |
| **Average Quantity per Transaction** | 5.54 |
| **Average Price Per Unit** | $23.36 |
| **Unique Customers** | 25 |
| **Unique Products (Items)** | 200 |
| **Sales Period** | 2022 – 2024 |
| **Top Category** | Furniture |
| **Top Payment Method** | Digital Wallet (~50%) |
| **Top Location** | Online (~84% of revenue) |

---

## 6. Conclusion

The dataset reveals a **high-growth, digitally-native retail business** with a healthy average order value. However, there are clear opportunities to improve profitability through smarter discounting and to secure future revenue through customer retention strategies.

The **explosive growth in late 2023** is the single most important signal in this data. Understanding and replicating this success should be the immediate focus for the strategy team.