import streamlit as st 

st.set_page_config(page_title = 'MyStreamlit',page_icon='./tiger.jpg')

mymenu = st.sidebar.selectbox('My Menu', ('Home','FillForm','Downloads'))
st.title("Onlei Technologies")
st.header("By Yash prasoon")
st.text("This is  tutorial on streamlit library")
st.image('./tiger.jpg')

if(mymenu == 'Home'):

    st.video("https://www.youtube.com/watch?reload=9&v=iri5LLriFHs")

    st.markdown("<center><h1>Welcome</h1></center>",unsafe_allow_html = True)

elif(mymenu == 'FillForm'):
    with st.form('My Form'):
        name = st.text_input('Enter name')
        dob = st.date_input("Choose Date of birth")
        marks = st.slider('choose marks')
        k =st.form_submit_button('Submit form')
        if k :
            st.write('Name = ', name, 'DOB: ',dob,'Marks : ',marks)

elif(mymenu == 'Downloads'):
    st.header("Downloads")
    st.download_button('Download Now','Hello this is a downloaded data','onlei.txt')

    





        

