import streamlit as st

st.title("Machine Learning Models")

model = st.selectbox(
    "Choose Model",
    [
        "Linear Regression",
        "Logistic Regression",
        "KNN",
        "Naive Bayes"
    ]
)

st.write("Selected:", model)

if st.button("Run"):
    st.success(f"{model} executed successfully!")