import streamlit as st

def app(data):
    st.title('Data Download')
    st.write('Download the Superstore Sales dataset below:')
    st.download_button('Download CSV', data.to_csv(index=False), file_name='superstore_sales.csv', mime='text/csv')
