# sales.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Interactive Superstore Sales Dashboard (Dummy Data)")

# -----------------------
# 1️⃣ Create Dummy Data
# -----------------------
data = pd.DataFrame({
    'Region': ['East', 'West', 'Central', 'South']*5,
    'Category': ['Furniture', 'Office Supplies', 'Technology', 'Furniture', 'Technology']*4,
    'Product': [f"Product {i}" for i in range(1, 21)],
    'Sales': [1000, 1500, 2000, 1200, 1800]*4,
    'Profit': [200, 300, 500, 150, 400]*4,
    'Quantity': [10, 15, 20, 12, 18]*4,
    'Customer': [f"Customer {i}" for i in range(1, 21)]
})

# -----------------------
# 2️⃣ Interactive Filters
# -----------------------
st.sidebar.header("🔧 Filters (Interactive)")

regions = st.sidebar.multiselect("Select Region", options=data['Region'].unique(), default=data['Region'].unique())
categories = st.sidebar.multiselect("Select Category", options=data['Category'].unique(), default=data['Category'].unique())
products = st.sidebar.multiselect("Select Product", options=data['Product'].unique(), default=data['Product'].unique())

filtered_data = data[
    (data['Region'].isin(regions)) &
    (data['Category'].isin(categories)) &
    (data['Product'].isin(products))
]

# -----------------------
# 3️⃣ KPI Metrics
# -----------------------
st.subheader("📌 Key Performance Indicators")
total_sales = filtered_data['Sales'].sum()
total_profit = filtered_data['Profit'].sum()
total_orders = filtered_data.shape[0]
total_quantity = filtered_data['Quantity'].sum()
avg_order_value = total_sales / total_orders if total_orders else 0
profit_margin = (total_profit / total_sales)*100 if total_sales else 0
total_customers = filtered_data['Customer'].nunique()

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Sales", f"${total_sales:,}")
col2.metric("📈 Total Profit", f"${total_profit:,}")
col3.metric("🧾 Total Orders", total_orders)

col4, col5, col6 = st.columns(3)
col4.metric("📦 Total Quantity", total_quantity)
col5.metric("🛒 Avg Order Value", f"${avg_order_value:,.2f}")
col6.metric("📊 Profit Margin", f"{profit_margin:.2f}%")

# -----------------------
# 4️⃣ Sales by Category (Bar Chart)
# -----------------------
st.subheader("🏷 Sales by Category")
category_sales = filtered_data.groupby('Category')['Sales'].sum().reset_index()
fig1 = px.bar(category_sales, x='Category', y='Sales', text='Sales', title="Sales by Category")
st.plotly_chart(fig1, use_container_width=True)

# -----------------------
# 5️⃣ Profit by Category (Bar Chart)
# -----------------------
st.subheader("📊 Profit by Category")
category_profit = filtered_data.groupby('Category')['Profit'].sum().reset_index()
fig2 = px.bar(category_profit, x='Category', y='Profit', text='Profit', title="Profit by Category", color='Category')
st.plotly_chart(fig2, use_container_width=True)

# -----------------------
# 6️⃣ Sales by Region (Pie Chart)
# -----------------------
st.subheader("🌍 Sales by Region")
region_sales = filtered_data.groupby('Region')['Sales'].sum().reset_index()
fig3 = px.pie(region_sales, names='Region', values='Sales', title="Sales Distribution by Region")
st.plotly_chart(fig3, use_container_width=True)

# -----------------------
# 7️⃣ Top Products Table
# -----------------------
st.subheader("🏆 Top Products by Sales")
top_products = filtered_data.groupby('Product')[['Sales','Profit']].sum().sort_values('Sales', ascending=False).head(10).reset_index()
st.table(top_products)

# -----------------------
# 8️⃣ Quantity by Category (Bar Chart)
# -----------------------
st.subheader("📦 Quantity Sold by Category")
category_quantity = filtered_data.groupby('Category')['Quantity'].sum().reset_index()
fig4 = px.bar(category_quantity, x='Category', y='Quantity', text='Quantity', title="Quantity by Category")
st.plotly_chart(fig4, use_container_width=True)

# -----------------------
# 9️⃣ Profit vs Sales Scatter
# -----------------------
st.subheader("💹 Profit vs Sales (Scatter)")
product_data = filtered_data.groupby('Product')[['Sales','Profit']].sum().reset_index()
fig5 = px.scatter(product_data, x='Sales', y='Profit', text='Product', size='Sales', color='Profit', title="Profit vs Sales per Product")
st.plotly_chart(fig5, use_container_width=True)

# -----------------------
# 🔟 Top Customers by Sales Table
# -----------------------
st.subheader("👥 Top Customers by Sales")
top_customers = filtered_data.groupby('Customer')[['Sales','Profit']].sum().sort_values('Sales', ascending=False).head(10).reset_index()
st.table(top_customers)