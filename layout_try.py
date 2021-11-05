#https://discuss.streamlit.io/t/change-font-size-in-st-write/7606

import streamlit as st
st.set_page_config(layout="wide")

st.markdown("""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
<style>
.big-font {
    font-size:300px !important;
}
</style>
""", unsafe_allow_html=True)

AQI=1234

st.markdown('<button type="button" class="btn btn-primary">Primary</button>', unsafe_allow_html=True)
st.markdown('<p class="big-font">Hello World !!</p>', unsafe_allow_html=True)

st.markdown(f'<h1 class="display-7">{AQI}</h1>' , unsafe_allow_html=True)
st.markdown(f'<button type="button" class="btn btn-primary">{AQI}</button>' , unsafe_allow_html=True)