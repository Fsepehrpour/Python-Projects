import streamlit as st
from src.GUI.password_generator import PinCodeGenerator, RandomPasswordGenerator, MemorablePasswordGenerator


st.image('images/banner.jpeg')
st.title(':zap: Password Generator')


option = st.radio(
    'Select the type of your preferred password generator:', 
    ("Random Password", "Pincode", "Memorable Password")
)

if option == "Pincode":
    length = st.slider('Select the length of your pincode', 6, 16)
    generator = PinCodeGenerator(length)
elif option == "Random Password":
    length = st.slider('Select the length of your password', 8, 16)
    include_numbers = st.toggle('Include numbers:')
    include_symbols = st.toggle('Include symbols:')
    generator = RandomPasswordGenerator(length, include_numbers, include_symbols)
elif option == "Memorable Password":
    no_of_words = st.slider('Select the number of words your password to have', 2, 5)
    separator = st.text_input('Words separator', value='_')
    capitalization = st.toggle('Capital words included in password?')
    generator = MemorablePasswordGenerator(no_of_words, separator, capitalization, None)

password = generator.generate()
st.write(f'your password is ```{password}```')
