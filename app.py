import streamlit as st

st.set_page_config(
    page_title="Simple Calculator",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 Simple Calculator")
st.write("Perform basic arithmetic operations.")

# Inputs
num1 = st.number_input("Enter First Number", value=0.0)
num2 = st.number_input("Enter Second Number", value=0.0)

operation = st.selectbox(
    "Select Operation",
    (
        "Addition (+)",
        "Subtraction (-)",
        "Multiplication (×)",
        "Division (÷)"
    )
)

if st.button("Calculate"):
    if operation == "Addition (+)":
        result = num1 + num2

    elif operation == "Subtraction (-)":
        result = num1 - num2

    elif operation == "Multiplication (×)":
        result = num1 * num2

    elif operation == "Division (÷)":
        if num2 == 0:
            st.error("❌ Cannot divide by zero.")
            st.stop()
        result = num1 / num2

    st.success(f"Result: {result}")

st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
