import streamlit as st
import math

st.header("Simple Maths")

choices = [ 'Area of Square',
            'Area of Circle',
            'Area of Triangle']

choice = st.radio('select an option', choices)
if choice == choices[0]:
    side = st.number_input("length of a side", min_value=1, max_value=100)
    area = side ** 2
    st.success(f'The total area is = {area:.2f}')

if choice == choices[1]:
    r = st.number_input("radius of circle", min_value=1, max_value=1000)
    area = math.pi * r ** 2
    st.success(f'The total area is = {area:.2f}')

if choice == choices[2]:
    c1, c2 = st.columns(2)
    base = c1.number_input('base of triangle',min_value=0)
    height = c2.number_input('height of triangle',min_value=0)
    area = .5 * base * height
    st.info(f'the total area is = {area:.2f}')
