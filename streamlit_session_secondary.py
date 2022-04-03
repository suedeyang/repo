import streamlit as st

"st.session_state",st.session_state

##每種widget都有效

number=st.slider("A number",1,10,key='slider')

st.write(st.session_state)

col1,buff,col2=st.columns([1,0.5,3])
option_names=["a","b","c"]

next = st.button("Next Button")
if next:
    if st.session_state["radio_option"] == 'a':
        st.session_state.radio_option = 'b' #注意這邊的等號 賦值要用 =
    elif st.session_state["radio_option"] == 'b':
        st.session_state.radio_option = 'c'
    else:
        st.session_state.radio_option = 'a'

option = col1.radio("pick an option",option_names,key="radio_option")

st.write('------------')
st.session_state

if option == "a":
    col2.write("You picked 'a' :smile:")
if option == "b":
    col2.write("You picked 'b' :heart:")
if option == "c":
    col2.write("You picked 'c' :rocket:")