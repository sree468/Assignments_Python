import streamlit as st

def app(data):
    st.title('Regional Performance')
    st.write('Analyze performance by region and state.')

    # Filters
    st.sidebar.header('Regional Performance Filters')
    regions = data['Region'].unique()
    region = st.sidebar.multiselect('Region', options=regions, default=list(regions))
    states = data[data['Region'].isin(region)]['State'].unique()
    state = st.sidebar.multiselect('State', options=states, default=list(states))

    # Filtered data
    filtered = data[data['Region'].isin(region)]
    filtered = filtered[filtered['State'].isin(state)]

    # Sales by State
    st.subheader('Sales by State')
    sales_by_state = filtered.groupby('State')['Sales'].sum().sort_values(ascending=False)
    st.bar_chart(sales_by_state)

    # Profit by State
    st.subheader('Profit by State')
    profit_by_state = filtered.groupby('State')['Profit'].sum().sort_values(ascending=False)
    st.bar_chart(profit_by_state)

    # Table
    st.subheader('Regional Data Table')
    st.dataframe(filtered[['Region','State','Sales','Profit']].head(20))
