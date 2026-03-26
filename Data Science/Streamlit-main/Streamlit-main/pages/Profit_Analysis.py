import streamlit as st

def app(data):
    st.title('Profit Analysis')
    st.write('Analyze profit trends and breakdowns.')

    # Filters
    st.sidebar.header('Profit Filters')
    years = data['Order Date'].str[-2:].unique()
    year = st.sidebar.selectbox('Select Year', sorted(years))
    categories = data['Category'].unique()
    category = st.sidebar.multiselect('Category', options=categories, default=list(categories))

    # Filtered data
    filtered = data[data['Order Date'].str[-2:] == year]
    filtered = filtered[filtered['Category'].isin(category)]

    # Profit by Sub-Category
    st.subheader('Profit by Sub-Category')
    profit_by_subcat = filtered.groupby('Sub-Category')['Profit'].sum().sort_values(ascending=False)
    st.bar_chart(profit_by_subcat)

    # Profit by State (Top 10)
    st.subheader('Top 10 States by Profit')
    profit_by_state = filtered.groupby('State')['Profit'].sum().sort_values(ascending=False).head(10)
    st.bar_chart(profit_by_state)

    # Table
    st.subheader('Profit Data Table')
    st.dataframe(filtered[['Order Date','State','Category','Sub-Category','Profit']].head(20))
