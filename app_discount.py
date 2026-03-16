import streamlit as st

price=st.number_input("Enter product price")

discount_percentage=st.slider("Select price discount", 1, 50, 1)

if st.button("Calculate discounted price"):
    final_price=price-(price*discount_percentage/100)
    st.write("Final price: ",final_price)
    
    st.success(final_price)
    
    st.table([[price],[final_price]])
