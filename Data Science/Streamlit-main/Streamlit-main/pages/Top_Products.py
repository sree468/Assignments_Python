import streamlit as st

def app(data):
    st.title('Top Products')
    st.write('Explore top performing products by sales and profit.')

    # Filters
    st.sidebar.header('Top Products Filters')
    categories = data['Category'].unique()
    category = st.sidebar.multiselect('Category', options=categories, default=list(categories))

    # Filtered data
    filtered = data[data['Category'].isin(category)]

    # Top 10 Products by Sales
    st.subheader('Top 10 Products by Sales')
    top_sales = filtered.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
    st.bar_chart(top_sales)

    # Top 10 Products by Profit
    st.subheader('Top 10 Products by Profit')
    top_profit = filtered.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(10)
    st.bar_chart(top_profit)

    # Table
    st.subheader('Top Products Data Table')
    st.dataframe(filtered[['Product Name','Category','Sales','Profit']].head(20))
