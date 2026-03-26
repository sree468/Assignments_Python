import streamlit as st

def app(data):
    st.title('Shipping Analysis')
    st.write('Analyze shipping modes and their impact.')

    # Filters
    st.sidebar.header('Shipping Filters')
    ship_modes = data['Ship Mode'].unique()
    ship_mode = st.sidebar.multiselect('Ship Mode', options=ship_modes, default=list(ship_modes))
    states = data['State'].unique()
    state = st.sidebar.multiselect('State', options=states, default=list(states))

    # Filtered data
    filtered = data[data['Ship Mode'].isin(ship_mode)]
    filtered = filtered[filtered['State'].isin(state)]

    # Orders by Ship Mode
    st.subheader('Orders by Ship Mode')
    orders_by_mode = filtered.groupby('Ship Mode')['Order ID'].nunique()
    st.bar_chart(orders_by_mode)

    # Sales by Ship Mode
    st.subheader('Sales by Ship Mode')
    sales_by_mode = filtered.groupby('Ship Mode')['Sales'].sum()
    st.bar_chart(sales_by_mode)

    # Table
    st.subheader('Shipping Data Table')
    st.dataframe(filtered[['Order ID','Ship Mode','State','Sales','Profit']].head(20))
