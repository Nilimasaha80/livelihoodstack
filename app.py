import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="LivelihoodStack", layout="wide")

st.title("🛠️ LivelihoodStack: SHG/FPO Toolkit")

menu = st.sidebar.selectbox("Choose Module", ["💰 Finance", "📅 Training", "🧾 Business Plan"])

if menu == "💰 Finance":
    st.header("📊 Advanced Finance Tracker")

    st.subheader("Income Sources")
    income_sources = {
        "Product Sales": st.number_input("Product Sales (₹)", min_value=0),
        "Grants/Subsidies": st.number_input("Grants/Subsidies (₹)", min_value=0),
        "Loan Received": st.number_input("Loan Received (₹)", min_value=0),
        "Other Income": st.number_input("Other Income (₹)", min_value=0),
    }

    st.subheader("Expenses")
    expenses = {
        "Raw Materials": st.number_input("Raw Materials (₹)", min_value=0),
        "Transportation": st.number_input("Transportation (₹)", min_value=0),
        "Loan Repayment": st.number_input("Loan Repayment (₹)", min_value=0),
        "Wages": st.number_input("Wages (₹)", min_value=0),
        "Miscellaneous": st.number_input("Miscellaneous Expenses (₹)", min_value=0),
    }

    total_income = sum(income_sources.values())
    total_expense = sum(expenses.values())
    net_savings = total_income - total_expense

    st.markdown("---")
    st.success(f"**Total Income:** ₹{total_income}")
    st.success(f"**Total Expense:** ₹{total_expense}")
    st.info(f"**Net Savings:** ₹{net_savings}")

    st.subheader("💡 Financial Summary Chart")
    fig, ax = plt.subplots()
    ax.bar(["Income", "Expense"], [total_income, total_expense], color=["green", "red"])
    ax.set_ylabel("Amount (₹)")
    st.pyplot(fig)

    if st.button("💾 Download Summary as CSV"):
        df = pd.DataFrame([
            {"Type": "Income", "Amount": total_income},
            {"Type": "Expense", "Amount": total_expense},
            {"Type": "Net Savings", "Amount": net_savings}
        ])
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("Download CSV", csv, "finance_summary.csv", "text/csv")

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
