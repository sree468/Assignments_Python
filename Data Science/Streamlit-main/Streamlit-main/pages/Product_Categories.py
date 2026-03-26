import streamlit as st

def app(data):
    st.title('Product Categories')
    st.write('Analyze product categories and sub-categories.')

    # Filters
    st.sidebar.header('Product Category Filters')
    categories = data['Category'].unique()
    category = st.sidebar.multiselect('Category', options=categories, default=list(categories))
    subcats = data[data['Category'].isin(category)]['Sub-Category'].unique()
    subcat = st.sidebar.multiselect('Sub-Category', options=subcats, default=list(subcats))

    # Filtered data
    filtered = data[data['Category'].isin(category)]
    filtered = filtered[filtered['Sub-Category'].isin(subcat)]

    # Sales by Category
    st.subheader('Sales by Category')
    sales_by_cat = filtered.groupby('Category')['Sales'].sum()
    st.bar_chart(sales_by_cat)

    # Sales by Sub-Category
    st.subheader('Sales by Sub-Category')
    sales_by_subcat = filtered.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False)
    st.bar_chart(sales_by_subcat)

    # Table
    st.subheader('Product Category Data Table')
    st.dataframe(filtered[['Category','Sub-Category','Product Name','Sales','Profit']].head(20))
