import streamlit as st

st.set_page_config(page_title="LivelihoodStack", layout="wide")
st.title("🛠️ LivelihoodStack: SHG/FPO Toolkit")

menu = st.sidebar.selectbox("Choose Module", ["📊 Finance", "📅 Training", "🧾 Business Plan"])

if menu == "📊 Finance":
    st.header("Finance Management")
    income = st.number_input("Monthly Income (₹)", min_value=0)
    expense = st.number_input("Monthly Expenses (₹)", min_value=0)
    savings = income - expense
    st.success(f"Estimated Monthly Savings: ₹{savings}")

elif menu == "📅 Training":
    st.header("Training Plan Tracker")
    module = st.text_input("Training Module Name")
    date = st.date_input("Scheduled Date")
    if st.button("Add Training"):
        st.success(f"✅ Added: {module} on {date}")

elif menu == "🧾 Business Plan":
    st.header("Business Plan Tracker")
    idea = st.text_area("Business/Product Idea")
    market = st.text_input("Target Market")
    progress = st.selectbox("Progress Status", ["Not Started", "In Progress", "Completed"])
    if st.button("Save Plan"):
        st.success(f"📌 Saved: '{idea}' for market '{market}' as {progress}")
