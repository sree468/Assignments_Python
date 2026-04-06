import streamlit as st
import pandas as pd
df = pd.read_csv("Superstore sales dataset.csv",
                 encoding='latin1')
print(df.head())

total_sales=df['Sales'].sum()
total_profit=df['Profit'].sum()
total_orders=df['Order ID'].nunique()

total_quantity=df['Quantity'].sum()
averge_order_values=total_sales/total_orders
profit_margin=total_profit/total_sales

total_customers=df['Customer ID'].nunique()
sales_per_customer=total_sales/total_customers
profit_per_customer=total_profit/total_customers

st.title("SuperStore Sales Dashboard")
col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Total Orders", f"{total_orders}")  
col4, col5, col6 = st.columns(3)
col4.metric("Total Quantity", f"{total_quantity}")
col5.metric("Average Order Value", f"${averge_order_values:,.2f}")
col6.metric("Profit Margin", f"{profit_margin:.2%}")
col7, col8,col9 = st.columns(3)
col7.metric("Total Customers", f"{total_customers}")
col8.metric("Sales per Customer", f"${sales_per_customer:,.2f}")
col9.metric("Profit per Customer", f"${profit_per_customer:,.2f}")



st.metric("Totalsales",1000,-100)



### displaying the full dataframe
st.dataframe(df)
## descriptive statistics 
st.dataframe(df.describe())
## correlation analys 
st.dataframe(df[df.describe().columns].corr())

####

# df['Month'] = df['Order Date'].dt.to_period('M')

import plotly.express as px

# # ---- Sales Trend ----
# st.subheader("📈 Monthly Sales Trend")
# monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()
# monthly_sales['Month'] = monthly_sales['Month'].astype(str)
# fig1 = px.line(monthly_sales, x='Month', y='Sales', title="Monthly Sales Trend")
# st.plotly_chart(fig1, use_container_width=True)

# # ---- Profit Trend ----
# st.subheader("📊 Monthly Profit Trend")
# monthly_profit = df.groupby('Month')['Profit'].sum().reset_index()
# monthly_profit['Month'] = monthly_profit['Month'].astype(str)
# fig2 = px.line(monthly_profit, x='Month', y='Profit', title="Monthly Profit Trend", line_shape='linear', markers=True)
# st.plotly_chart(fig2, use_container_width=True)

# # ---- Sales by Category ----
# st.subheader("🏷 Sales by Category")
# category_sales = df.groupby('Category')['Sales'].sum().reset_index()
# fig3 = px.bar(category_sales, x='Category', y='Sales', title="Sales by Category", text='Sales')
# st.plotly_chart(fig3, use_container_width=True)

# # ---- Top 10 Products ----
# st.subheader("🏆 Top 10 Products by Sales")
# top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10).reset_index()
# st.table(top_products)

# # ---- Sales by Region ----
# st.subheader("🌍 Sales by Region")
# region_sales = df.groupby('Region')['Sales'].sum().reset_index()
# fig4 = px.pie(region_sales, names='Region', values='Sales', title="Sales Distribution by Region")
# st.plotly_chart(fig4, use_container_width=True)
# ---- Monthly Profit Trend ----
st.subheader("📊 Monthly Profit Trend")
monthly_profit = pd.DataFrame({
    'Month': [f"2023-{i:02d}" for i in range(1, 13)],
    'Profit': [0]*12
})
fig2 = px.line(monthly_profit, x='Month', y='Profit', title="Monthly Profit Trend", markers=True)
st.plotly_chart(fig2, use_container_width=True)

# ---- Sales by Category ----
st.subheader("🏷 Sales by Category")
category_sales = pd.DataFrame({
    'Category': ['Furniture', 'Office Supplies', 'Technology'],
    'Sales': [10, 20, 30]
})
fig3 = px.bar(category_sales, x='Category', y='Sales', title="Sales by Category")
st.plotly_chart(fig3, use_container_width=True)

# ---- Top Products Table ----
st.subheader("🏆 Top Products by Sales")
top_products = pd.DataFrame({
    'Product Name': [f"Product {i}" for i in range(1, 6)],
    'Sales': [0]*5
})
st.table(top_products)

# ---- Sales by Region ----
st.subheader("🌍 Sales by Region")
region_sales = pd.DataFrame({
    'Region': ['East', 'West', 'Central', 'South'],
    'Sales': [0, 0, 0, 0]
})
fig4 = px.pie(region_sales, names='Region', values='Sales', title="Sales Distribution by Region")
st.plotly_chart(fig4, use_container_width=True)