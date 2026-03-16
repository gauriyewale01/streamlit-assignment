import streamlit as st

st.title("Product Entry Form")

product_name = st.sidebar.text_input("Enter Product Name")

category = st.sidebar.selectbox(
    "Select Category",
    ["Electronics", "Clothing", "Food", "Books", "Other"]
)

price = st.sidebar.number_input("Enter Price", min_value=0.0)

if st.sidebar.button("Add Product"):
    
    st.success("Product added successfully!")

    st.subheader("Product Details")

    st.write("Product Name:", product_name)
    st.write("Category:", category)
    st.write("Price:", price)

