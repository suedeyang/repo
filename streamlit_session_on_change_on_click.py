import streamlit as st

"st.session_state",st.session_state

# on_change對輸入型的widget有效 像是st.slider st.number_input
# on_click對一次性的widget有效 想是 st.button st.form_submit_button


def lbs_to_kg():
    st.session_state.kg=st.session_state.lbs/2.2046
def kg_to_lbs():
    st.session_state.lbs=st.session_state.kg*2.2046

col1,buff,col2=st.columns([2,1,2])
with col1:
    pounds = st.number_input('Pounds:',key='lbs',on_change=lbs_to_kg)
with col2:
    kilogram=st.number_input('Kilograms:',key='kg',on_change=kg_to_lbs)