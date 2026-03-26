import streamlit as st

def app(data):
    st.title('Sales Analysis')
    st.write('Analyze sales trends and breakdowns.')

    # Filters
    st.sidebar.header('Sales Filters')
    categories = data['Category'].unique()
    category = st.sidebar.multiselect('Category', options=categories, default=list(categories))
    subcats = data[data['Category'].isin(category)]['Sub-Category'].unique()
    subcat = st.sidebar.multiselect('Sub-Category', options=subcats, default=list(subcats))
    states = data['State'].unique()
    state = st.sidebar.multiselect('State', options=states, default=list(states))

    # Filtered data
    filtered = data[data['Category'].isin(category)]
    filtered = filtered[filtered['Sub-Category'].isin(subcat)]
    filtered = filtered[filtered['State'].isin(state)]

    # Sales by Sub-Category
    st.subheader('Sales by Sub-Category')
    sales_by_subcat = filtered.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False)
    st.bar_chart(sales_by_subcat)

    # Sales by State (Top 10)
    st.subheader('Top 10 States by Sales')
    sales_by_state = filtered.groupby('State')['Sales'].sum().sort_values(ascending=False).head(10)
    st.bar_chart(sales_by_state)

    # Table
    st.subheader('Sales Data Table')
    st.dataframe(filtered[['Order Date','State','Category','Sub-Category','Sales','Quantity']].head(20))
