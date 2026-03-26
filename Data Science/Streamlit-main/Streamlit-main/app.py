import streamlit as st
import pandas as pd

# Load data
data = pd.read_csv('data/superstore_sales.csv')

# Sidebar navigation
st.sidebar.title('Superstore Sales App')
pages = [
    'Overview',
    'Sales_Analysis',
    'Profit_Analysis',
    'Customer_Segments',
    'Product_Categories',
    'Regional_Performance',
    'Shipping_Analysis',
    'Discount_Impact',
    'Top_Products',
    'Data_Download'
]
page = st.sidebar.radio('Go to', pages)

# Page loader
def load_page(page):
    if page == 'Overview':
        import pages.Overview as pg
        pg.app(data)

    elif page == 'Sales_Analysis':
        import pages.Sales_Analysis as pg
        pg.app(data)

    elif page == 'Profit_Analysis':
        import pages.Profit_Analysis as pg
        pg.app(data)

    elif page == 'Customer_Segments':
        import pages.Customer_Segments as pg
        pg.app(data)

    elif page == 'Product_Categories':
        import pages.Product_Categories as pg
        pg.app(data)

    elif page == 'Regional_Performance':
        import pages.Regional_Performance as pg
        pg.app(data)

    elif page == 'Shipping_Analysis':
        import pages.Shipping_Analysis as pg
        pg.app(data)

    elif page == 'Discount_Impact':
        import pages.Discount_Impact as pg
        pg.app(data)

    elif page == 'Top_Products':
        import pages.Top_Products as pg
        pg.app(data)

    elif page == 'Data_Download':
        import pages.Data_Download as pg
        pg.app(data)

    else:
        st.write('Page not found.')

load_page(page)

# ✅ FIXED TEXT DISPLAY
st.markdown(""" 
This dashboard provides deep insights into:
- 📈 Sales trends and patterns
- 🌍 Regional performance metrics
- 📦 Product analysis
- 👥 Customer insights
- 💰 Profitability analysis
- 📅 Time series forecasts
- 🔄 Year-over-year comparisons
- 🔍 Raw data exploration

**Navigate using the sidebar pages to explore different analyses.**
""")

st.info("💡 Tip: Use the filters and dropdowns on each page to customize your analysis!")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Pages", "10", "📄")
with col2:
    st.metric("Data Updates", "Real-time", "⚡")
with col3:
    st.metric("Regions Covered", "4", "🗺️")