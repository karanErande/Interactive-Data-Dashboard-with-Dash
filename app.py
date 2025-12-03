import pandas as pd

# Load dataset
data = pd.read_csv("data.csv")

print("Dataset Loaded Successfully")
print(data.head())
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Interactive Data Dashboard", layout="wide")

st.title("📊 Interactive Data Dashboard")
st.write("A mini project using Python & Streamlit")

data = pd.read_csv("data.csv")

st.sidebar.header("Filters")

category = st.sidebar.selectbox(
    "Select Category",
    ["All"] + list(data["Category"].unique())
)

sales_range = st.sidebar.slider(
    "Select Sales Range",
    int(data["Sales"].min()),
    int(data["Sales"].max()),
    (int(data["Sales"].min()), int(data["Sales"].max()))
)

filtered_data = data.copy()

if category != "All":
    filtered_data = filtered_data[filtered_data["Category"] == category]

filtered_data = filtered_data[
    (filtered_data["Sales"] >= sales_range[0]) &
    (filtered_data["Sales"] <= sales_range[1])
]

st.subheader("Filtered Dataset")
st.dataframe(filtered_data)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Sales Over Time")
    fig1 = px.line(filtered_data, x="Date", y="Sales", markers=True)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Sales by Category")
    fig2 = px.bar(filtered_data, x="Category", y="Sales", color="Category")
    st.plotly_chart(fig2, use_container_width=True)

st.subheader("Profit Distribution")
fig3 = px.pie(filtered_data, values="Profit", names="Category")
st.plotly_chart(fig3)

st.markdown("---")
st.caption("Mini Project: Interactive Data Dashboard using Streamlit")
