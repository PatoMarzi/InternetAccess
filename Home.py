import streamlit as st
import numpy as np
import pandas as pd


# Set the page config
st.set_page_config(page_title='Glide',
                   page_icon='./assets/images/logo.jpg', layout='centered')

# Set the title for the web application
st.header('We are :blue[Glide]', divider='blue')

st.image('./assets/images/logo.jpg')

with st.expander('ABOUT US'):
    st.markdown(body='''
                Glide Connections™ is a small company established in 2014. Headquartered in Rosario, the company started its journey with a clear mission: to revolutionize the way people connect. As the years passed, Glide Connections™ experienced rapid growth, expanding its influence and impact beyond Rosario to establish a nationwide presence.
                ''')
    st.markdown(body='''
                The company's commitment to innovation and seamless communication has fueled its ascent, making it a formidable player in the technology landscape. The story of Glide Connections™ is one of ambition, adaptability, and a relentless pursuit of creating meaningful connections that transcend geographical boundaries.
                ''')

with st.expander('OUR MISSION'):
    st.markdown(body='''
                At Glide Connections™, we believe in the transformative power of technology to bring people closer, fostering a global network united by shared experiences and enriched relationships.

                ''')

with st.expander('THIS PROJECT'):

    st.markdown(body='''
                For this new project, we were required to analyze the behaviour of different Internet connection types nationwide, to be on the lookout for potential customers
                as well as understanding the strenghts and weaknesses in order to provide a better
                service for our clientes.                
                ''')

    st.markdown(body='''
                In addition, we were required to measure two different KPIs:
                ''')
    st.markdown(body='''
                 - The first KPI measures the increment of <a target = "_self" style = 'text-decoration: none' href = './Internet_Access' >Internet access per 100 households for each province</a> This helps us determine whether there is an increase in demand for the internet, regardless of the type of connection, and if we have lost any customers in that region.
                 - The second KPI focuses on the <a target = "_self" style = 'text-decoration: none' href = './Wireless_Connections' >number of wireless connections</a> and its attemp to increase that number for the next quarter. Even though wireless connection is one of the most popular nowadays, Argentina is surprisingly behind when it comes to having a high-speed, reliable wireless infrastructure
                ''', unsafe_allow_html=True)
