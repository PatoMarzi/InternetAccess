import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.set_page_config(page_title='Glide - Go Wireless',
                   page_icon='assets\images\logo.jpg', layout='centered')


df = pd.read_csv('Wireless.csv', sep=',')


st.markdown(f''' 
            ## Comparison of WiFi connection vs other types of connections
            
            ''')

st.dataframe(df, hide_index=True)

views = st.radio(':blue[Select The Data To Visualize]',
                 [':white[Number of Connection Type by Year]',':white[Wifi Connections percentaje]'], horizontal=True)





if views == ':white[Number of Connection Type by Year]':

    df['Quarter'] = df['Quarter'].astype('str')
    options = ['ADSL', 'Cable modem', 'Optic Fiber', 'Wireless']
    period = st.slider(
        label=':red[Desired Year]', min_value=2014, max_value=2022, step=1, value=None)
    
    connection = st.selectbox(
        label='Select the connection type to visualize', options=options)



    fig = plt.figure(figsize=(12, 7))
    plt.title('')
    sns.set_style('darkgrid')


    sns.barplot(data=df[df['Year'] == period], x='Quarter', y=connection,
                hue='Quarter', errorbar=None)
    plt.legend(title='Quarter', loc='upper center', shadow=True)
    plt.ylim(0, 100)
    plt.xticks(ticks=[])
    st.pyplot(fig)

elif views ==':white[Wifi Connections percentaje]':
    
    period = st.slider(
        label=':red[Desired Year]', min_value=2014, max_value=2022, step=1, value=None)
    
    filtered_df = df[df['Year'] == period]

    df['Year'] = df['Year'].astype('int16')
    
    options = ['ADSL', 'Cable modem', 'Optic Fiber', 'Wireless']
    
    
    totalConnections = filtered_df[options].sum()
    explode = (0, 0, 0, 0.2)

    fig, ax = plt.subplots(figsize = (14, 6))

    ax.pie(totalConnections, labels = totalConnections.index, autopct = '%1.2f%%', startangle = 30, explode = explode, shadow = True, textprops = {'fontsize': '16'}, radius = 1)
    st.pyplot(fig)
    
