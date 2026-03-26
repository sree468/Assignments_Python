import streamlit as st

def app(data):
    st.title('Customer Segments')
    st.write('Analyze customer segments and their performance.')

    # Filters
    st.sidebar.header('Customer Segment Filters')
    segments = data['Segment'].unique()
    segment = st.sidebar.multiselect('Segment', options=segments, default=list(segments))
    regions = data['Region'].unique()
    region = st.sidebar.multiselect('Region', options=regions, default=list(regions))

    # Filtered data
    filtered = data[data['Segment'].isin(segment)]
    filtered = filtered[filtered['Region'].isin(region)]

    # Sales by Segment
    st.subheader('Sales by Segment')
    sales_by_segment = filtered.groupby('Segment')['Sales'].sum()
    st.bar_chart(sales_by_segment)

    # Profit by Segment
    st.subheader('Profit by Segment')
    profit_by_segment = filtered.groupby('Segment')['Profit'].sum()
    st.bar_chart(profit_by_segment)

    # Table
    st.subheader('Customer Segment Data Table')
    st.dataframe(filtered[['Customer Name','Segment','Region','Sales','Profit']].head(20))
