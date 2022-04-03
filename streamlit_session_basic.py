import streamlit as st
#import time

#st.session_state是以dictionary型態儲存的
st.subheader('原先的session 是空的')
"st.session_state:",st.session_state

if 'a_counter' not in st.session_state:
    st.session_state['a_counter']=0

if "boolean" not in st.session_state:
    st.session_state.boolean = False

st.write("--------------")
st.subheader('後來的session 是有東西的')
st.write(st.session_state)

st.write("a_counter is:",st.session_state['a_counter'])
st.write("boolean is :",st.session_state.boolean)

st.write("--------------")
st.subheader('st.session_state是以dictionary型態儲存的')
st.caption("用for迴圈取出st.session_state字典的keys")
for the_key in st.session_state.keys():
    st.write(the_key)

st.caption("用for迴圈取出st.session_state字典的values")
for the_value in st.session_state.values():
    st.write(the_value)

st.caption("用for迴圈取出st.session_state字典成對的的items")
for item in st.session_state.items():
    st.write(item)

button=st.button("update state")
"按按鈕之前",st.session_state
if button:
    st.session_state['a_counter'] += 1
    st.session_state.boolean = not st.session_state.boolean
    "after pressing button",st.session_state

codes='''
刪除st.session_states的key
for key in st.session_state.keys():
    del st.session_state[key]
st.session_state就被清空了
'''
st.code(codes)