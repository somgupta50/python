import streamlit as st

st.header('Welcome to Streamlit')
st.subheader('By Som Gupta')

st.sidebar.title('Cool sidebar with options')
st.sidebar.success('Done!')

st.text('BCA 3rd Year')
st.success('some text area')
st.error('Error messege')
st.warning('Warning Message')

btn=st.button('Dont click')
if btn:
    st.error('what have you done')
    st.write('this is not what is needed to be done')

countries=[' India ',' SriLanka ',' Nepal ',' Japan ']
c=st.selectbox("select the country",countries)
st.write(f'You have selected{c}')

name=st.text_input("what is your name",value="Som")
st.write(f'Your Name: {name}')

age=st.slider('What is your age',min_value=10,max_value=100,step=2,value=20)
if age>50:
    st.error('You are too old for this')
elif age<15:
    st.warning('you are too young for this')
else:
    st.success('you are ready for this')