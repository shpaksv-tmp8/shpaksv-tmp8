import streamlit as st

if st.checkbox('RuntimeWarning'):
    raise RuntimeWarning('Manually raised RuntimeWarning')
