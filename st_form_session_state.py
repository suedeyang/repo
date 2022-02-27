import streamlit as st
 
#https://docs.streamlit.io/en/stable/session_state_api.html#session-state-and-widget-state-association
#https://docs.streamlit.io/en/stable/session_state_api.html#use-callbacks-to-update-session-state
#https://docs.streamlit.io/en/stable/api.html?highlight=FORM#streamlit.form
 


def form_callback():
    st.write(st.session_state.my_slider2)
    st.write(st.session_state.my_checkbox)
    st.write("------------")
    st.write(slider_input)
    st.write(checkbox_input) 
    
with st.form(key='my_form',clear_on_submit=True):
    slider_input = st.slider('My slider', 0, 10, 5, key='my_slider2')
    checkbox_input = st.checkbox('Yes or No', key='my_checkbox')
    submit_button = st.form_submit_button(label='Submit', on_click=form_callback)
 
 
 
# python更新前端的值
cccc = 2.0
def form_callback2():
    st.session_state.my_checkbox = True
 
with st.form(key='my_form2'):
    submit_button = st.form_submit_button(label='Submit2', on_click=form_callback2)
 
 
st.write(st.session_state) 

st.write(slider_input)
st.write(checkbox_input) 