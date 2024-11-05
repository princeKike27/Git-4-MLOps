# import modules
import streamlit as st 


# title
st.title('Streamlit Demo - Kike 27')

# header
st.header('Heading of Streamlit')

# subheader
st.subheader('Sub-Heading of Streamlit')

# text
st.text('This is an Example Text')

# success message
st.success('Success')
# warning message
st.warning('warning')
# info message
st.info('information')
# error message
st.error('Error')


# checkbox
if st.checkbox('Select / Unselect'):
    st.text('User selected the checkbox')
else:
    st.text('User has not selected the checkbox')

# radio button
state = st.radio('What is your favorite color ?', 
                 ('Red', 'Green', 'Blue'))

if state == 'Green':
    st.success('That is the color of Nature!!!')


# selectbox
occupation = st.selectbox('What do you do?', 
                          ('Student', 'Engineer', 'Physicist'))

st.text(f'You are an {occupation.upper()}')

# if users click on a button
if st.button('Example Button'):
    st.info('User clicked Button!!!')


# SIDEBAR
st.sidebar.header('Heading of Sidebar')
st.sidebar.text('Created by Kike27')