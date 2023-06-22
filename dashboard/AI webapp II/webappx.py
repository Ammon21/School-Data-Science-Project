import streamlit as st
import numpy as np
import pandas as pd



name = st.text_input("Whats your name??")

age = st.slider('How old are you?', 10, 20, 1)

option = st.selectbox('Gender',
    ('Male', 'Female'))

pob = st.selectbox('Place of Birth',
    ('Ethiopia', 'Foriegn soil'))

tutor = st.selectbox('Do you take any makeup class or tutoring',
    ('yes', 'no'))

grade = st.selectbox('What grade are you in?',
    (5, 6, 7, 8, 9,10, 11, 12))

mothertongue = st.selectbox('what is your first language (mother tongue)',
    ('ethiopian lang', 'foriegn language'))


['conduct', 'age', 'gender', 'pob', 'tutor/makeup', 'grade', 'admission','mother_tongue', 'maths', 'english', 'first child', 'last child','middle child', 'authoritarian', 'authoritative', 'permissive','private', 'public', 'service', 'both', 'single']