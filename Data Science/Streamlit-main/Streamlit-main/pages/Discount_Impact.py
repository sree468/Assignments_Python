import streamlit as st

def app(data):
    st.title('Discount Impact')
    st.write('Analyze the impact of discounts on sales and profit.')

    # Filters
    st.sidebar.header('Discount Filters')
    discount_range = st.sidebar.slider('Discount Range', float(data['Discount'].min()), float(data['Discount'].max()), (float(data['Discount'].min()), float(data['Discount'].max())))

    # Filtered data
    filtered = data[(data['Discount'] >= discount_range[0]) & (data['Discount'] <= discount_range[1])]

    # Sales vs Discount
    st.subheader('Sales vs Discount')
    st.scatter_chart(filtered[['Discount','Sales']])

    # Profit vs Discount
    st.subheader('Profit vs Discount')
    st.scatter_chart(filtered[['Discount','Profit']])

    # Table
    st.subheader('Discount Data Table')
    st.dataframe(filtered[['Order ID','Discount','Sales','Profit']].head(20))
