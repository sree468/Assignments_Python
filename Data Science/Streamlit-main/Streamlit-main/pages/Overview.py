import streamlit as st

def app(data):
    st.title('Overview')
    st.write('Welcome to the Superstore Sales Dashboard!')
    st.write('This dashboard provides insights into sales, profit, customers, products, and more.')
    st.write('Use the sidebar to navigate through the 10 pages.')

    # Filters
    st.sidebar.header('Overview Filters')
    years = data['Order Date'].str[-2:].unique()
    year = st.sidebar.selectbox('Select Year', sorted(years))
    region = st.sidebar.multiselect('Select Region', options=sorted(data['Region'].unique()), default=list(data['Region'].unique()))

    # Filtered data
    filtered = data[data['Order Date'].str[-2:] == year]
    filtered = filtered[filtered['Region'].isin(region)]

    # Metrics
    total_sales = filtered['Sales'].sum()
    total_profit = filtered['Profit'].sum()
    total_orders = filtered['Order ID'].nunique()
    st.metric('Total Sales', f"${total_sales:,.2f}")
    st.metric('Total Profit', f"${total_profit:,.2f}")
    st.metric('Total Orders', total_orders)

    # Sales by Region
    st.subheader('Sales by Region')
    sales_by_region = filtered.groupby('Region')['Sales'].sum().sort_values(ascending=False)
    st.bar_chart(sales_by_region)

    # Profit by Category
    st.subheader('Profit by Category')
    profit_by_cat = filtered.groupby('Category')['Profit'].sum()
    st.bar_chart(profit_by_cat)

    # Show filtered data
    st.subheader('Sample Data')
    st.dataframe(filtered.head(10))
