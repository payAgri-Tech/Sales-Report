import streamlit as st
import plotly.graph_objects as go
import plotly.subplots as sp
import pandas as pd

# Set up the Streamlit page
st.set_page_config(page_title="Sales Summary Report", layout="wide")

# Define sales data
sales_data = pd.DataFrame({
    'Date': ['2024-08-24', '2024-08-29', '2024-08-30', '2024-08-31', '2024-09-01'],
    'Client': ['Nutrilla Feed', 'Rainbow', 'Suryanarayanan', 'Nutrilla Feed', 'Rainbow'],
    'Sales Value': [3050000, 8670000, 2900000, 2000000, 1500000],
    'Payment Received': [3045000, 8443165, 2900000, 2000000, 1500000],
    'Contract Quantity': [105, 300, 100, 50, 75],
    'Actual Quantity Lifted': [105, 292.27, 102.72, 49.5, 74.8],
    'Margin Percentage': ['3.68%', '10.26%', '3.60%', '4.5%', '5.0%']
})

# Custom CSS for styling
st.markdown("""
    <style>
    .reportview-container, .sidebar .sidebar-content {
        background-color: #FFFFFF;
    }
    .st-cp, .st-cq, .st-cr {
        color: #2755FF;
    }
    .st-cs {
        background-color: #CCE3EB;
    }
    </style>
""", unsafe_allow_html=True)

# Main title and introduction
st.title("Sales Report")
st.write("""
    Welcome to the Sales Summary Report. This report provides a comprehensive overview of recent sales achievements, 
    focusing on effective contract management, financial performance, and operational efficiency.
""")

st.divider()

# Company Achievements Summary
st.header("Company Achievements Summary")
st.write("A summary of our company's recent performance, highlighting key sales metrics and financial outcomes.")

# Display Contract Details and Payment Highlights
col1, col2 = st.columns(2)

with col1:
    st.subheader("Contract Details")
    st.metric("Total Contract Value", "₹14,250,000")
    st.metric("Total Contract Quantity", "505 MT")
    st.metric("Average Contract Price / Kg", "₹28.9")

with col2:
    st.subheader("Payment Highlights")
    st.metric("Total Payments Received", "₹14,388,165")
    st.write("**Key Payment Dates:** 8/24/2024, 8/29/2024")
    st.metric("Total Profit Margin", "₹249,995")

st.divider()

# Display Financial Performance
st.header("Financial Performance")

col3, col4 = st.columns(2)

with col3:
    st.subheader("Quantity and Value")
    st.metric("Total Actual Quantity Lifted", "499.99 MT")
    st.metric("Total Transaction Value", "₹14,470,483")

with col4:
    st.subheader("Financial Efficiency")
    st.metric("Balance Payment Expected", "₹124,417")
    st.metric("TDS to be Collected", "₹3,438")

st.divider()

# Dispatch Efficiency
st.subheader("Dispatch Efficiency")
st.write("**Load Dispatched Dates:** 8/24/2024, 8/30/2024, 8/31/2024, 9/01/2024")

# Margin Analysis
st.subheader("Margin Analysis")
st.metric("Total Margin Value", "₹249,995")
st.metric("Overall Margin %", "17.54%")
st.metric("Overall Markup Margin %", "1.80%")

st.divider()

# Summary of Achievements
st.header("Summary of Achievements")
with st.expander("Click to expand"):
    st.write("""
        - **Effective Contract Execution**: Managed contracts totaling ₹14,615,000 with a robust quantity of 505 MT.
        - **Strong Financial Performance**: Achieved total payments of ₹14,388,165 and a transaction value of ₹14,470,483.
        - **Operational Excellence**: Efficient payment collection and dispatch operations with balanced financial management.
        - **Profitability and Growth**: Maintained a healthy margin of 17.54% and a consistent markup margin of 1.80%, reflecting strong profitability and operational efficiency.
    """)

st.divider()

# Display Sales Data Table
st.subheader("Sales Data")
st.dataframe(sales_data, use_container_width=True)

st.divider()

# Visualization setup
st.header("Sales Performance Dashboard")

# Data for Pie Charts
buyers = ["Nutrilla Feed", "Rainbow", "Suryanarayanan"]
sales_values = [3045000, 8670000, 2900000]
payment_amounts = [1425000, 2992500, 2950000, 2850000, 4175000]
payment_dates = ["8/12/2024", "8/24/2024", "8/29/2024 (x3)"]

# Creating subplots: 1 row, 2 columns with domain type for pie charts
fig_pie = sp.make_subplots(rows=1, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}]],
                    subplot_titles=("Sales Distribution by Buyer", "Payment Distribution"))

# Pie chart: Sales Distribution by Buyer
fig_pie.add_trace(go.Pie(labels=buyers, values=sales_values, hole=0.3,
                     marker=dict(colors=["#5A9BD5", "#70AD47", "#2F5597"])), row=1, col=1)

# Pie chart: Payment Distribution
fig_pie.add_trace(go.Pie(labels=payment_dates, values=payment_amounts, hole=0.3,
                     marker=dict(colors=["#A3C1DA", "#5A9BD5", "#2F5597", "#70AD47", "#A9D18E"])), row=1, col=2)

# Update layout
fig_pie.update_layout(title_text="Sales and Payment Distribution Analysis", height=500, width=1000, showlegend=True)

# Show the figure
st.plotly_chart(fig_pie, use_container_width=True)

# Data for Area and Scatter Charts
dates_cumulative_margin = ["8/24/2024", "8/28/2024", "8/29/2024"]
margins = [52500, 146135, 51360]
cumulative_margins = [sum(margins[:i+1]) for i in range(len(margins))]

dates_sales_payment = ["8/12/2024", "8/24/2024", "8/29/2024", "8/29/2024", "8/29/2024"]
sales_values = [0, 3045000, 8390000, 2900000, 0]
payments_received = [1425000, 2992500, 2950000, 2850000, 4175000]
cumulative_sales = [sum(sales_values[:i+1]) for i in range(len(sales_values))]
cumulative_payments = [sum(payments_received[:i+1]) for i in range(len(payments_received))]

# Data for Scatter Plots
prices_per_kg = [29, 28.9, 29]
quantity_lifted_scatter = [105, 292.27, 102.72]
margin_percentages = [3.68, 10.26, 3.60]

# Buyers for scatter plot
buyers_scatter = ["Nutrilla Feed", "Rainbow", "Suryanarayanan"]

# Creating subplots: 2 rows, 2 columns
fig = sp.make_subplots(rows=2, cols=2, subplot_titles=("Cumulative Margin Over Time", "Total Sales and Payment Progression",
                                                    "Price vs. Quantity Lifted", "Margin Percentage vs. Buyer"))

# Area chart: Cumulative Margin Over Time
fig.add_trace(go.Scatter(x=dates_cumulative_margin, y=cumulative_margins, fill='tozeroy', mode='lines+markers',
                         name="Cumulative Margin", line=dict(color="#5A9BD5")), row=1, col=1)

# Area chart: Total Sales and Payment Progression
fig.add_trace(go.Scatter(x=dates_sales_payment, y=cumulative_sales, fill='tozeroy', mode='lines+markers',
                         name="Cumulative Sales", line=dict(color="#70AD47")), row=1, col=2)
fig.add_trace(go.Scatter(x=dates_sales_payment, y=cumulative_payments, fill='tozeroy', mode='lines+markers',
                         name="Cumulative Payments", line=dict(color="#2F5597")), row=1, col=2)

# Scatter plot: Price vs. Quantity Lifted
fig.add_trace(go.Scatter(x=prices_per_kg, y=quantity_lifted_scatter, mode='markers',
                         name="Price vs. Quantity", marker=dict(size=10, color="#A3C1DA")), row=2, col=1)

# Scatter plot: Margin Percentage vs. Buyer
fig.add_trace(go.Scatter(x=buyers_scatter, y=margin_percentages, mode='markers',
                         name="Margin % vs. Buyer", marker=dict(size=10, color="#5A9BD5")), row=2, col=2)

# Update layout for all charts
fig.update_layout(title_text="Comprehensive Financial and Sales Analysis", height=700, width=1000, showlegend=True)
fig.update_xaxes(title_text="Dates", row=1, col=1)
fig.update_xaxes(title_text="Dates", row=1, col=2)
fig.update_xaxes(title_text="Price per Kg", row=2, col=1)
fig.update_xaxes(title_text="Buyers", row=2, col=2)
fig.update_yaxes(title_text="Cumulative Margin (₹)", row=1, col=1)
fig.update_yaxes(title_text="Amount (₹)", row=1, col=2)
fig.update_yaxes(title_text="Quantity Lifted (MT)", row=2, col=1)
fig.update_yaxes(title_text="Margin Percentage (%)", row=2, col=2)

# Show the figure
st.plotly_chart(fig, use_container_width=True)
