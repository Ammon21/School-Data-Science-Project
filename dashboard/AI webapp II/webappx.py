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

mothertongue = st.selectbox('Admission type inquiry',
    ('paid', 'scholarship'))

math = st.number_input('What is your maths grade of the previous semester')

english = st.number_input('What is your english grade of the previous semester')

birth = st.radio(
    "What\'s your favorite movie genre",
    ('First child', 'middle child', 'last child'))

fx = 0
fm = 0
fl = 0


if birth == 'First child':
    fx = 1
elif birth == 'middle child':
    fm=1
else:
    fl=1    

st.write(fx,fm,fl)      

parenting = st.radio(
    "How do you describe your relationship with your parents (Parrenting Style)",
    ('Authoritative', 'Authoritarian', 'Permissive', 'Uninvolved'))

transport_type = st.selectbox('What is your transport type',
    ('Private Car', 'Public Tranportation', 'Service', 'on Foot'))


birth = st.radio(
    "Do you live with both parents",
    ('yes', 'no'))


#['conduct', 'age', 'gender', 'pob', 'tutor/makeup', 'grade', 'admission','mother_tongue', 'maths', 'english', 'first child', 'last child','middle child', 'authoritarian', 'authoritative', 'permissive','private', 'public', 'service', 'both', 'single']