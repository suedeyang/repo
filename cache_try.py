import streamlit as st
import time

@st.cache(suppress_st_warning=True)
def expensive_computation(a, b):
    st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
    time.sleep(2)  # 👈 This makes the function take 2s to run
    return a * b

a = 233
b = st.slider("Pick a Number",0,10)
res = expensive_computation(a, b)

st.write("Result:", res)